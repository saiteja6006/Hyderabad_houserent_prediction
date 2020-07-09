# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 16:07:25 2020

@author: saite
"""

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'localities': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
@app.route('/get_furnish_names', methods=['GET'])
def get_furnish_names():
    response = jsonify({
        'furnish': util.get_furnish_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
@app.route('/get_tenants_names', methods=['GET'])
def get_tenants_names():
     response = jsonify({
        'Tenants': util.get_tenants_names()
    })
     response.headers.add('Access-Control-Allow-Origin', '*')

     return response

@app.route('/predict_rent_price', methods=['GET', 'POST'])
def predict_rent_price():
    
    localities = request.form['localities']
    furnish= request.form['furnish']
    Tenants= request.form['Tenants']
    bathrooms = int(request.form['bathrooms'])
    area = float(request.form['area'])
    bhk = int(request.form['bhk'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(localities,furnish,Tenants,bathrooms,area,bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Rent Prediction...")
    util.load_saved_artifacts()
    app.run()