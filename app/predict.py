import numpy as np
import pandas as pd
import joblib

model = joblib.load('models/TMDB_BO.joblib')


def get_form_data(data):

    feature_values = {
        'number_of_genres': 2,
        'runtime': 100, 
        'cast_count': 20, 
        'crew_count': 40, 
        'has_collection': 1,
        'speaks_english': 1,
        'budget': 20000000,
        'popularity': 7.3,
    }

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]
    return feature_values

def predict(data, debug=False):
    values = get_form_data(data)

    if debug:
        print(f'Feature values: {values}\n')

    columns_order = ['number_of_genres', 'runtime', 'cast_count', 'crew_count', 
    'has_collection', 'speaks_english', 'budget', 'popularity']       

    values = np.array([values[feature] for feature in columns_order], dtype=object)

    if debug:
        print('ordered feature values: ')
        print(list(zip(columns_order, values)))

    pred = model.predict(values.reshape(1,-1))
    return str(pred[0])