import pickle
import json
import numpy as np

with open("./columns.json", "r") as f:
    __data_columns = json.load(f)['data_columns']
    __locations = __data_columns[3:]

with open('banglore_home_model.pickle', 'rb') as f:
    model = pickle.load(f)

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())

    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(model.predict([x])[0],2)

def get_location_names():
    return __locations