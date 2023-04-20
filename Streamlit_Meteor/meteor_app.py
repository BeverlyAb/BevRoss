import streamlit as st
import pandas as pd

# read data
meteor_CSV = pd.read_csv('./Data/meteorite-landings.csv')
df =  meteor_CSV.copy()
# clean data
df = df[(df['reclong']<=180) & (df['reclong']>=-180) ] # should only be btwn -180 to 180
df = df[(df['reclat']!= 0) | (df['reclong']!= 0)]      # can't have lat or long of 0
df = df.dropna() # removes rows with any missing col
df.isnull().sum() # checks the number of missing values in each column 

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
