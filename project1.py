import streamlit as st
import pandas as pd

def show_project1():

        st.title('Diabetes Prediction using Random Forests Classifier')     
        st.write('''The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information. This can be useful for healthcare professionals in identifying patients who may be at risk of developing diabetes and in developing personalized treatment plans. Additionally, the dataset can be used by researchers to explore the relationships between various medical and demographic factors and the likelihood of developing diabetes.''')
        st.write('Data preparation constituted of feature selection, data scaling, imputing and encoding etc. A supervised machine learning framework was built and the RandomForest regressor')
        st.write('Libraries used')
        st.write('Mathematical and data processing Libraries : scikit-learn, pandas, statsmodels, numpy')
        st.write('Visualization Libraries : seaborn, matplotlib, plotly')
        st.write('deployment / dashboarding : Streamlit')
        st.info('Check out the app [here](https://diabetes-9nwebg4dxjhdgxn9rr7wpv.streamlit.app/) ')
        st.image('diabetes.png')
        st.caption('Screenshot of the front page')