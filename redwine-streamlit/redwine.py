import requests
import json
import streamlit as st
import numpy as np
import pandas as pd 

# url = 'http://localhost:5000/predict'
# url = 'http://redwineapp.centralindia.azurecontainer.io:5000/predict'
url ='http://34.201.5.16:5000/predict'



st.title("Red wine prediction system")

col1, col2,col3 = st.beta_columns(3)

fixed_acidity = np.float(col1.text_input("Fixed Acidity",7.4))
volatile_acidity = np.float(col2.text_input("Volatile Acidity",0.7))
citric_acid = np.float(col3.text_input("Citric Acid",0))
residual_sugar = np.float(col1.text_input("Residual Sugar",1.9))
chlorides = np.float(col2.text_input("Chlorides",0.076))
free_sulphur_dioxide = np.float(col3.text_input("Free Sulphur dioxide",11))
total_sulphur_dioxide = np.float(col1.text_input("Total Sulphur dioxide",34))
density = np.float(col2.text_input("Density",0.9978))
ph = np.float(col3.text_input("PH",3.51))
sulphates = np.float(col1.text_input("Sulphates",0.56))
alcohol = np.float(col2.text_input("Alchol",9.4))

features_num = ['fixed acidity', 'volatile acidity', 'citric acid',
       'residual sugar', 'chlorides', 'free sulfur dioxide',
       'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

result = st.button("Predict Red Wine Quality")

sample = [fixed_acidity,
volatile_acidity ,
citric_acid ,
residual_sugar ,
chlorides ,
free_sulphur_dioxide ,
total_sulphur_dioxide ,
density ,
ph ,
sulphates ,
alcohol 
]


if result:
    j_data = json.dumps(sample)
    # Set the content type in the request headers
    
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)
    predictions =  json.loads(r.text)
    predictions = predictions["prediction"].replace("[[","")
    predictions = predictions.replace("]]","")

    st.write("The predicted wine quality is " + predictions)




