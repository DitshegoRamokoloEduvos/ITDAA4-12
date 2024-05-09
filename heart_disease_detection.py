# import all the app dependencies
import pandas as pd
import numpy as np
import sklearn
import streamlit as st
import joblib
import matplotlib
from IPython import get_ipython
from PIL import Image

# load the encoder and model object
model = joblib.load("rta_model_deploy3.joblib")
encoder = joblib.load("ordinal_encoder2.joblib")

st.set_option('deprecation.showPyplotGlobalUse', False)

# 1: heart disease, 0: healthy

st.set_page_config(page_title="Heart disease Prediction App",
        page_icon="🚧", layout="wide")

#creating option list for dropdown menu

options_sex = [ 'Gender','1=male', '0=female']

options_cp = ['chest pain type','0=typical angina', "1=atypical angina", "2=no-anginal pain", "3=asymptomatic"]


options_fbs = ['fasting blood sugar','1=true', '0=false']


options_restecg = ['resting eletrocardiographic results','normal',
              'abnormal','ventricular hypertrophy']


options_exang = ['exercise induced angina','1=yes','0=no']


options_slope = ['The Slope of the Peak Exercise ST segment','0=upsloping','1=flat','2=downsloping']


options_ca = ['Number of Major Vessels Coloured by Fluoroscopy','0=low','1=mild', '2=moderate', '3=high', '4=severe']


options_thal = ['Status of the heart','1=normal', '2=fixed defect', '3=reversible defect','0=unknown']


# features list
features = ['age','sex','cp','trestbps','chol','fbs',
    'restecg','thalach','exang','oldpeak','slope','ca','thal']
# Give a title to web app using html syntax
st.markdown("<h1 style='text-align: center;'>Heart Disease Prediction App 🚧</h1>", unsafe_allow_html=True)

# define a main() function to take inputs from user in form based approach
def main():
    with st.form("heart_disease_detection_form"):
       st.subheader("Please enter the following inputs:")
        
       age = st.slider("Age of the Patient in Years:",1,100, value=0, format="%d")
       sex = st.selectbox("Sex of the Patient:", options=options_sex)
       cp = st.selectbox("Chest Pain Type:", options=options_cp)
       trestbps = st.slider("Resting Blood Pressure (in mm Hg on admission to the Hospital):",1,400, value=0, format="%d")
       chol = st.slider("serum cholestoral in mg/dl:", 0, 600, value=0, format="%d")
       fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl:",options=options_fbs)
       restecg = st.selectbox("Resting electrocardiographic results:", options=options_restecg)
       thalach = st.slider("Maximum Heart Rate Acchieved:", 0, 500, value=0, format="%d")
       exang = st.selectbox("Exercise Induced Angina:",options=options_exang)
       oldpeak = st.number_input("ST Depression Induced by Exercise relative to rest:", 0.0, 2.0, value=0.0, format="%d")
       slope = st.selectbox("The Slope od the Peak Exercise ST Segment:", options=options_slope)
       ca = st.selectbox("Number of Major Vessels colored by fluoroscopy:", options=options_ca)
       thal = st.selectbox("Status of the heart:", options=options_thal)
       
        
       submit = st.form_submit_button("Predict")

# encode using ordinal encoder and predict
    if submit:
       input_array = np.array([
                  sex, cp, fbs, restecg, exang, slope, ca, thal], ndmin=2)
        
       encoded_arr = list(encoder.transform(input_array).ravel())
        
       num_arr = [age, trestbps, chol, thalach, oldpeak]
       pred_arr = np.array(num_arr + encoded_arr).reshape(1,-1)        
      
# predict the target from all the input features
       prediction = model.predict(pred_arr)
        
       if prediction == 1:
           st.write(f"The patient has heart disease⚠")
       else:
           st.write(f"The patient is healthy")
        
       st.write("Developed By: Ditshego Ramokolo")
       st.markdown("""Reach out to me on: 
       [Kaggle](https://www.kaggle.com/DitshegoRamokoloEduvos) 
       """)
#a,b,c = st.columns([0.2,0.6,0.2])
#with b:
# st.image("banner-picture.jpeg", use_column_width=True)

# description about the project and code files       
st.subheader("🧾Description:")
st.text("""The dataset used in this project is a subset of the Heart Disease dataset from the
Original Heart Disease datarepo.
""")

st.markdown("Source of the dataset: [Click Here](https://archive.ics.uci.edu/dataset/45/heart+disease)")

st.subheader("🧭 Problem Statement:")
st.text("""This allows doctors to enter the details of patients (fill in the columnschosen for the model) to determine whether the patient likely suffers from heart disease so they may decide to send the patient for further tests or treatment.
""")

st.markdown("Please find GitHub repository link of project: [Click Here](https://github.com/DitshegoRamokoloEduvos/Heart-Disease-Detection-Project)")          
  
# run the main function        
if __name__ == '__main__':
  main()