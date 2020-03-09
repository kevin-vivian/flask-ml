<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template, url_for
from flask_restful import reqparse
import pickle
import numpy as np
from model import NLPModel
import logging.config
import os

app = Flask(__name__)

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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict',methods=['POST'])
def predict():

    # vectorize the user's query and make a prediction
    features = np.array([x for x in request.form.values()])
    uq_vectorized = model.vectorizer_transform(features)
    prediction = model.predict(uq_vectorized)
    pred_proba = model.predict_proba(uq_vectorized)


    # Output either 'Negative' or 'Positive' along with the score
    
    if prediction == 0:
        pred_text = 'negative'
    else:
        pred_text = 'positive'

    # round the predict proba value and set to new variable
    confidence = round(pred_proba[0], 3)

    # create JSON object
    output = {'prediction': pred_text, 'confidence': confidence}
    # return render_template('index.html', prediction_text='Printing {}'.format(uq_vectorized))
    return render_template('index.html', prediction_text='Prediction is {}'.format(output['prediction']))

if __name__ == '__main__':
=======
from flask import Flask, render_template, url_for, request
from flask_restful import reqparse
import pickle
import numpy as np
from model import NLPModel
import logging.config
import os

app = Flask(__name__)

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
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

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
    return render_template('home.html', prediction_text='Prediction is {} '.format(output['prediction']))

if __name__ == '__main__':
>>>>>>> b0b2ff59d0f53ce1aa4fc545ef7ef6ac9f422421
    app.run(debug=True)