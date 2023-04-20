import streamlit as st
import pandas as pd

# read data
meteor_CSV = pd.read_csv('./Data/meteorite-landings.csv')
df =  meteor_CSV.copy()
numeric_df = df.select_dtypes(include=["float32","float64","int32","int64"])


st.title('Raw Meteor Data')
df
st.subheader('Description')
st.write(df.describe())
c1, c2 = st.columns(2)
with c1:
    st.subheader('Correlation')
    st.write(numeric_df.corr())
with c2:
    st.subheader('Covariance')
    st.write(numeric_df.cov())



