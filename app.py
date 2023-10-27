import streamlit as st
import pandas as pd

# Specify the path to your CSV file
file_path = 'oecd-our-world-dataset.csv'

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# extract a list of indicators from the Indicator column in df
indicators = df['Indicator'].unique().tolist()

# create a selectbox to choose an indicator
indicator = st.selectbox(
    'Select Indicator',
    indicators
)
# filter the dataframe to only include rows with the selected indicator
df = df[df['Indicator'] == indicator]

# display the dataframe as a table in Streamlit
st.table(df)