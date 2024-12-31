# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the Streamlit App
st.title('Simple Data Dashboard')

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display a preview of the data
    st.subheader('Data Preview')
    st.write(df.head())  # Display the first few rows of the DataFrame

    # Display a summary of the data
    st.subheader('Data Summary')
    st.write(df.describe())  # Show statistical summary of the DataFrame

    # Filter data based on user input
    st.subheader('Filter Data')
    columns = df.columns.tolist()  # Get a list of column names from the DataFrame
    selected_column = st.selectbox('Select Column to Filter by', columns)  # Dropdown for selecting a column
    unique_values = df[selected_column].unique()  # Get unique values from the selected column
    selected_value = st.selectbox('Select Value', unique_values)  # Dropdown for selecting a value to filter by
    filtered_df = df[df[selected_column] == selected_value]  # Filter DataFrame by the selected value
    st.write(filtered_df)  # Display the filtered DataFrame

    # Plot data based on user-selected columns
    st.subheader('Plot Data')
    x_column = st.selectbox('Select X Axis', columns)  # Dropdown for selecting X-axis column
    y_column = st.selectbox('Select Y Axis', columns)  # Dropdown for selecting Y-axis column

    # Generate the plot when the button is clicked
    if st.button('Generate Plot'):
        st.line_chart(filtered_df.set_index(x_column)[y_column])  # Create a line chart based on the selected columns

# Message to display when no file is uploaded
else:
    st.write('Waiting for CSV file to be uploaded...')