# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 16:16:36 2020

@author: saite
"""

import pickle
import json
import numpy as np

__localities = None
__furnish = None
__Tenants =None
__data_columns = None
__model = None

def get_estimated_price(localities,furnish,Tenants,bathrooms,area,bhk):
    try:
        loc_index = __data_columns.index(localities.lower())
        fur_index = __data_columns.index(furnish.lower())
        ten_index = __data_columns.index(Tenants.lower())
    except:
        loc_index =  3
        fur_index =  3
        ten_index =  3

    x = np.zeros(len(__data_columns))
    x[0] = bathrooms
    x[1] = area
    x[2] = bhk
    if loc_index >= 0 & fur_index >= 0 & ten_index >= 0:
        x[loc_index] = 1
        x[fur_index] = 2
        x[ten_index] = 3

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __localities
    global __furnish
    global __Tenants

    with open("C:/Users/saite/OneDrive/Desktop/hyderabad rent/Server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __localities = __data_columns[4:38]  
        __furnish = __data_columns[39:41]
        __Tenants = __data_columns[41:]
    global __model
    if __model is None:
        with open('C:/Users/saite/OneDrive/Desktop/hyderabad rent/Server/artifacts/Hyderabad_house_rent.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __localities
def get_furnish_names():
    return __furnish
def get_tenants_names():
    return __Tenants

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_furnish_names)
    print(get_tenants_names)
    print(get_estimated_price('begumpet','furnish','family',2, 1000,3))
    print(get_estimated_price('kondapur','semi-furnished','family',1,1250,3))
    print(get_estimated_price('lbnager,nh','unfurnished','bachelors',2, 1000,2)) # other location
    