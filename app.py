# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 00:09:55 2023

@author: seanr
"""

from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__,template_folder='templates')

with open("xgb_model.pkl", "rb") as f:
    xgb_model = pickle.load(f)
    
scalar=pickle.load(open('scaling.pkl','rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])

def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=xgb_model.predict(final_input)[0]
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)