import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from CSV file
df = pd.read_csv('StockDataAPI3/hist_index_value.csv')
df['date'] = pd.to_datetime(df['date'])

# Define the Streamlit app
st.title('Peak Core Fintech Index')

# Create the Plotly figure
fig = px.line(df, x='date', y='0', title='Price Chart')

# Display the Plotly figure in the Streamlit app
st.plotly_chart(fig)