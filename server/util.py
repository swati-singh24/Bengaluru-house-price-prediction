import json
import pickle
import numpy as np

# Global variables declare kar rahe hain jo load_saved_artifacts se populate honge
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        # data columns list mein se location ka index dhundh rahe hain
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    # Numpy array bana rahe hain jitne columns hain utne zeros ke saath
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    
    # Agar location list mein mili, toh uss specific index ko 1 (One-Hot Encoded) kar do
    if loc_index >= 0:
        x[loc_index] = 1

    # Model se predict karwa rahe hain aur round off kar rahe hain 2 decimals tak
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # columns.json ko read kar rahe hain
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        # Pehle 3 columns (sqft, bath, bhk) hain, uske baad saari locations hain
        __locations = __data_columns[3:]

    # Aapki pickle file ko load kar rahe hain
    with open("./artifacts/price_prediction_model.pickle", "rb") as f:
        __model = pickle.load(f)
        
    print("loading saved artifacts...done")

# File ko execute karke test karne ke liye ye block hai
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names()[:5])  # Pehli 5 locations print karke check karega