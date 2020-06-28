from __future__ import division, print_function
from flask import Flask
from flask import Flask, render_template, request


#import requests

import numpy as np
import os
import pickle
import sklearn

	
# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)





app = Flask(__name__)



model = pickle.load(open('models/model.pkl', 'rb'))
@app.route('/')
def index():
    return render_template('mlmodel.html')




@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('mlmodel.html', prediction_text='Employee Salary should be $ {}'.format(output))






if __name__ == '__main__':
    app.run(debug=True)



