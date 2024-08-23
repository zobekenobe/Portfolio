import streamlit as st
import pandas as pd

def show_project2():

        st.title('Wine Quality Classification using Machine Learning')     
        st.write('''The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones). ''')
        st.write('Data preparation constituted of feature selection, data scaling, imputing and encoding etc. A supervised machine learning framework was built and the RandomForest Classifier to predict if the given wine is great or not.')
        st.write('Libraries used')
        st.write('Mathematical and data processing Libraries : scikit-learn, pandas, statsmodels, numpy')
        st.write('Visualization Libraries : seaborn, matplotlib, plotly')
        st.write('deployment / dashboarding : Streamlit')
        st.info('Check out the app [here](https://47vl8xbmwtqe8hndogbaws.streamlit.app/) ')
        st.image('wine.png')
        st.caption('Screenshot of the front page')