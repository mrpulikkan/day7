#Loading the required libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

#Calling the model we saved above:

pickle_in = open('d7try1.pkl', 'rb')
classifier = pickle.load(pickle_in)
#Creating the UI for the application:

st.sidebar.header('Advertisement and Sales Realtio Using multivarient linera Regression')
select = st.sidebar.selectbox('Select Form', ['Form 1'], key='1')
if not st.sidebar.checkbox("Hide", True, key='1'):
    st.title('Price Prediction')
    name = st.text_input("Name:")
    TV= st.number_input("Advertising rate for TV adds :")
    radio = st.number_input("Advertising rate for Radio adds  :")
    newspaper =  st.number_input("Advertising rate for News paper adds :")
 
   
    
    submit = st.button('Predict')
    if submit:
        prediction = classifier.predict([[TV, radio, newspaper]])
        st.write('Sales : ', prediction)
