import streamlit as st
import pandas as pd
import altair as alt 

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

# add a label to the page to indicate the legend item is selectable
st.write('Click on a legend item to toggle the visibility of the corresponding line.')

# add an altair chart to the page
# references :
# https://altair-viz.github.io/index.html
# https://docs.streamlit.io/library/api-reference/charts/st.altair_chart

# Define a selection type for the legend
legend_selection = alt.selection_point(fields=['Country'], bind='legend')

# Base chart definition
base_chart = alt.Chart(df).encode(
    x='Time:O',
    y='Value:Q',
    color=alt.condition(legend_selection, 'Country:N', alt.value('lightgray')),
    opacity=alt.condition(legend_selection, alt.value(1), alt.value(0.2))
).add_params(
    legend_selection
)

# Create lines and circles using the base chart
lines = base_chart.mark_line()
circles = base_chart.mark_circle()

# Combine the charts
chart = lines + circles

st.altair_chart(chart)
# display the dataframe as a table in Streamlit
st.table(df)

