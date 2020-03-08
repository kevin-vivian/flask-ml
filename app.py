from flask import Flask, Blueprint, request, jsonify, render_template, render_template_string
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from model import NLPModel
import logging.config
import os

app = Flask(__name__)
api = Api(app)

# create parser
parser = reqparse.RequestParser()
parser.add_argument('query')

model = NLPModel()

clf_path = os.getcwd()+'/models/SentimentClassifier.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)

vec_path = os.getcwd()+'/models/TFIDFVectorizer.pkl'
with open(vec_path, 'rb') as f:
    model.vectorizer = pickle.load(f)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    # vectorize the user's query and make a prediction
    features = np.array([x for x in request.form.values()])
    uq_vectorized = model.vectorizer_transform(features)
    prediction = model.predict(uq_vectorized)
    pred_proba = model.predict_proba(uq_vectorized)


    # Output either 'Negative' or 'Positive' along with the score

    if prediction == 0:
        pred_text = 'Negative'
    else:
        pred_text = 'Positive'

    # round the predict proba value and set to new variable
    confidence = round(pred_proba[0], 3)

    # create JSON object
    output = {'prediction': pred_text, 'confidence': confidence}
    # return render_template('index.html', prediction_text='Printing {}'.format(uq_vectorized))
    return render_template('index.html', prediction_text='Prediction is {}'.format(output))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

# Setup the Api resource routing here
# Route the URL to the resource
# api.add_resource(PredictSentiment, '/predict_api')

if __name__ == '__main__':
    app.run(debug=True)