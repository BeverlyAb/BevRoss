import streamlit as st
import pandas as pd
import matplotlib
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np

# read data
meteor_CSV = pd.read_csv('./Data/meteorite-landings.csv')
df =  meteor_CSV.copy()
# clean data
df = df[(df['reclong']<=180) & (df['reclong']>=-180) ] # should only be btwn -180 to 180
df = df[(df['reclat']!= 0) | (df['reclong']!= 0)]      # can't have lat or long of 0
df = df.dropna() # removes rows with any missing col
df.isnull().sum() # checks the number of missing values in each column 

numeric_df = df.select_dtypes(include=["float32","float64","int32","int64"])
subtitles = ['Raw Meteor Data', 'Description', 'Correlation', 'Covariance', 'Misc']
subaction = [df, df.describe(), numeric_df.corr(), numeric_df.cov(),'']   

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

if side_radio == 'Misc':
    hist_data = [df['year']]
    group_labels = ['meteor distribution']
    fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])
    fig.update_layout(title='Meteor distribution over Years')
    st.plotly_chart(fig)

    start_year, end_year = st.slider('Years', value=(1000,2023))
    map_df = df.loc[df['year'].between(start_year,end_year)]
    st.header('Meteor landings')
    map_df = pd.DataFrame({'lat': map_df['reclat'], 'lon': map_df['reclong']})
    st.map(map_df)
