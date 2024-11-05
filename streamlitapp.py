# Import necessary libraries
import streamlit as st
import seaborn as sns 
import plotly.express as px
import pandas as pd

# --- Title and Introduction ---
st.title("Plotly and Streamlit Interactive Visualizations")

# Author information
st.markdown("<h5 style='color: teal;'>Created by:</h6>", unsafe_allow_html=True)
st.markdown("<p style='color: white;'>1. 54_Anushritha_N </p>", unsafe_allow_html=True)


tips = sns.load_dataset('tips')  # Loading the dataset
print(tips.head())  # This will show the first 5 rows of the tips dataset

#--- Task 1: Visualization ---
st.subheader("Task 1: Visualization")
# Visualizations using Plotly
fig1 = px. bar(tips, x="day", y="tip")
fig1.show()
st.plotly_chart(fig1)

# --- Task 2: Bar Chart ---
st.subheader("Task 2: Bar Chart")
#Bar Chart: Average Tip by Day (With Color)
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white',  # Clean white background
)
fig2.show()
st.plotly_chart(fig2)
# ---Task 3: Scatter plot ---
st.subheader("Task 3:Scatter plot")
# Scatter Plot: Total Bill vs. Tip (Color-coded by Gender)
fig3 = px.scatter (
tips, x='total_bill', y='tip', color='sex',
title='Total Bill vs Tip(colored by gender)',
labels={'total_bill': 'Total Bill ($)' , 'tip': 'Tip ($)'},
template='plotly_dark', #using a cool dark theme 
size='size', #size of the points based on the size of the group
)
fig3.show()
st.plotly_chart(fig3)

# --- Task 4: Box Plot ---
st.subheader("Task 4: Box Plot")
# Box Plot: Distribution of Total Bill by Day (With Color by Time)
fig4 = px.box(
    tips, x='day',y='total_bill',color='time',
    title='Total Bill Distribution by Day and Time',
    labels={'total_bill': 'Total Bill ($)', 'day':'Day'},
    template='ggplot2', #classic theme for a beautiful look
)
fig4.show()
st.plotly_chart(fig4)

# --- Task 5: Histogram ---
st.subheader("Task 5: Histogram")
# Histogram: Tip Distribution (With Color)
fig5=px.histogram(
    tips, x='tip', color='sex',
    title='Distribution of Tips(Colored by Gender)',
    labels={'tip': 'Tips ($)', 'sex':'Gender'},
    template='plotly_white', #clean and bright look
)
fig5.show()
st.plotly_chart(fig5)
