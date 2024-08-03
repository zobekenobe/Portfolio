import streamlit as st
import pandas as pd


st.title('Portfolio')
project = st.sidebar.selectbox('Project List', ('Choose a Project','Cybersecurity', "Machine Learning", 'Natural Language Processing'))

if project == 'Cybersecurity':
    st.text('You have chosen Cybersecurity')
elif project == 'Machine Learning':
    st.text('You have chosen Machine Learning')
elif project == 'Natural Language Processing':
    st.text("You have chosen Natural Language Processing")