import json
import pickle
import numpy as np
import pandas as pd  # Make sure pandas is imported

__data_columns = None
__data_columns_lower = None  # lowercase version for matching
__model = None


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __data_columns_lower
    global __model

    with open("server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __data_columns_lower = [col.lower() for col in __data_columns]

    with open("server/artifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("loading saved artifacts...done")


def get_estimated_price(location, sqft, bhk, bath):
    location = location.lower()  # match against lowercase list

    try:
        loc_index = __data_columns_lower.index(location)
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # Column names remain original case so the model recognizes them
    input_df = pd.DataFrame([x], columns=__data_columns)
    prediction = __model.predict(input_df)[0]  # store prediction
    return round(max(prediction, 0), 2)  # avoid negative prices


def get_location_names():
    # This will return the list exactly as in training (original case)
    return __data_columns[3:]


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st phase jp nagar', 1000, 3, 3))
    print(get_estimated_price('1ST PHASE JP NAGAR', 1000, 3, 3))