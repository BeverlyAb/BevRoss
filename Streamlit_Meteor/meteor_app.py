import streamlit as st
import pandas as pd

# read data
meteor_CSV = pd.read_csv('./Data/meteorite-landings.csv')
df =  meteor_CSV.copy()
numeric_df = df.select_dtypes(include=["float32","float64","int32","int64"])

subtitles = ['Raw Meteor Data', 'Description', 'Correlation', 'Covariance']
subaction = [df, df.describe(), numeric_df.corr(), numeric_df.cov()]   

with st.sidebar:
    st.title('Display')
    side_radio = st.radio(
        "Select your data",

        (subtitle for subtitle in subtitles)
    )


for i in range(len(subtitles)):
    if side_radio == subtitles[i]:
        st.subheader(subtitles[i])
        st.write(subaction[i])
