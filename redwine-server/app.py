# Dependencies
from flask import Flask, request, jsonify

import traceback
import numpy as np
from tensorflow import keras
import pandas as pd
import pickle

# Your API definition
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return("Predict here")

@app.route('/predict', methods=['POST'])
def predict():
    if model:
        try:
            json_ = request.get_json()
            sample_df = pd.DataFrame([json_],columns = features_num)
            prediction = model.predict(preprocessor.transform(sample_df))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
   port = 5000  

   features_num = ['fixed acidity', 'volatile acidity', 'citric acid',
       'residual sugar', 'chlorides', 'free sulfur dioxide',
       'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

   preprocessor = pickle.load(open('preprocessor.p',"rb"))
   print("I am here")
   model = keras.models.load_model('redwine_model.h5')    
   if model:
       print("model found")
   else:
       print("model not found")


   app.run(host='0.0.0.0',port=port, debug=True)