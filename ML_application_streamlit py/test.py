
import streamlit as st
import seaborn as sns
import matplotlib.pyplot  as plt
import pandas as pd

dataset_loc = "data/Tweets.csv"
st.sidebar.success("Analyze how travelers in February 2015 expressed their feelings on Twitter")
df = pd.read_csv(dataset_loc)
st.write(sns.countplot(x='airline_sentiment', data=df))
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()