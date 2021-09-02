import streamlit as st
import numpy as np
from tensorflow import keras

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

result = st.button("Predict Red Wine Quality")
sample = np.array([fixed_acidity,
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
])
model = keras.models.load_model('redwine_model.h5')
if result:
    
    st.write("The predicted wine quality is " + \
        str(model.predict(sample[np.newaxis,...]).flatten()))




