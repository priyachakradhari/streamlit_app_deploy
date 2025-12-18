import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as px


st.title("The Webapp Project - Data Analysis Application")
st.subheader("Let's Perform the data analsyis for the given dataset")

# load the dataser
dataset_options = ['iris', 'titanic', 'diamonds', 'tips']
select_dataset = st.selectbox("select the dataset", dataset_options)

if select_dataset == 'iris':
    df = sns.load_dataset('iris')
elif select_dataset == 'titanic':
    df = sns.load_dataset('titanic')    
elif select_dataset == 'diamonds':
    df = sns.load_dataset('diamonds')
elif select_dataset == 'tips':
    df = sns.load_dataset('tips')    

upload_dataset = st.file_uploader('Upload dataset', type = ['csv', 'xlsx'])

if upload_dataset is not None:
    df = pd.read_csv(upload_dataset)

st.text('The head of the dataset')
st.write(df.head())    


st.text('Shape of the dataset')
st.write(df.shape)

st.text('the stats of the dataset')
st.write(df.describe())

st.text('Checking Null Value')
st.write(df.isnull().sum().sort_values(ascending=False))

X_axis = st.selectbox('X-axis', df.columns)
y_axis = st.selectbox('y-axis', df.columns)
plot_type = st.selectbox('Select the plot', ['line', 'bar', 'kde', 'scatter', 'hist', 'box'])

if plot_type == 'line':
    st.line_chart(df[[X_axis, y_axis]])
elif plot_type == 'bar':
    st.bar_chart(df[[X_axis, y_axis]])    
elif plot_type == 'box':
    df[[X_axis, y_axis]].plot(kind = 'box')
    st.pyplot()    
elif plot_type == 'kde':
    df[[X_axis, y_axis]].plot(kind = 'kde')
    st.pyplot()
elif plot_type == 'scatter':
    st.scatter_chart(df[[X_axis, y_axis]])
elif plot_type == 'hist':
    df[X_axis].plot(kind = 'hist')
    st.pyplot()    

hue_column = st.selectbox("Select the hue column", df.columns)
st.pyplot(sns.pairplot(df, hue = hue_column, markers = 'o'))   

st.subheader('Heatmap')
st.pyplot(sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm', linewidths=2))

