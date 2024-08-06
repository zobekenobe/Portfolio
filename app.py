import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
st.write(st.__version__)
st.write(pd.__version__)


st.title('Portfolio')
project = st.sidebar.selectbox('Project List', ('Choose a Project','Cybersecurity', "Machine Learning", 'Natural Language Processing'))

if project == 'Cybersecurity':
    st.text('You have chosen Cybersecurity')
elif project == 'Machine Learning':
    st.text('You have chosen Machine Learning')
elif project == 'Natural Language Processing':
    st.text("You have chosen Natural Language Processing")