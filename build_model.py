<<<<<<< HEAD
from model import NLPModel
import pandas as pd
from sklearn.model_selection import train_test_split
import os

def build_model():
    model = NLPModel()

    with open(os.getcwd()+'/sentiment_data/train.tsv') as f:
        data = pd.read_csv(f, sep='\t')

    pos_neg = data[(data['Sentiment'] == 0) | (data['Sentiment'] == 4)]

    pos_neg['Binary'] = pos_neg.apply(
        lambda x: 0 if x['Sentiment'] == 0 else 1, axis=1)

    model.vectorizer_fit(pos_neg.loc[:, 'Phrase'])
    print('Vectorizer fit complete')

    X = model.vectorizer_transform(pos_neg.loc[:, 'Phrase'])
    print('Vectorizer transform complete')
    y = pos_neg.loc[:, 'Binary']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model.train(X_train, y_train)
    print('Model training complete')

    model.pickle_clf()
    model.pickle_vectorizer()

    # model.plot_roc(X_test, y_test, size_x=12, size_y=12)


if __name__ == "__main__":
=======
from model import NLPModel
import pandas as pd
from sklearn.model_selection import train_test_split
import os

def build_model():
    model = NLPModel()

    with open(os.getcwd()+'/sentiment_data/train.tsv') as f:
        data = pd.read_csv(f, sep='\t')

    pos_neg = data[(data['Sentiment'] == 0) | (data['Sentiment'] == 4)]

    pos_neg['Binary'] = pos_neg.apply(
        lambda x: 0 if x['Sentiment'] == 0 else 1, axis=1)

    model.vectorizer_fit(pos_neg.loc[:, 'Phrase'])
    print('Vectorizer fit complete')

    X = model.vectorizer_transform(pos_neg.loc[:, 'Phrase'])
    print('Vectorizer transform complete')
    y = pos_neg.loc[:, 'Binary']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model.train(X_train, y_train)
    print('Model training complete')

    model.pickle_clf()
    model.pickle_vectorizer()

    # model.plot_roc(X_test, y_test, size_x=12, size_y=12)


if __name__ == "__main__":
>>>>>>> b0b2ff59d0f53ce1aa4fc545ef7ef6ac9f422421
    build_model()