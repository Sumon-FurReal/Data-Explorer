import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Title and info
st.title("Data Explorer :crystal_ball:")
st.info("The DataExplorer is an interactive web application designed to empower users to perform Exploratory Data Analysis (EDA) with ease and efficiency. With this intuitive tool, users can upload their datasets in CSV format, and the application will swiftly process and visualize the data to gain valuable insights.")


# Loading the data
def load_data():
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data
    return None


data = load_data()
if data is not None:
    st.header("Data loaded successfully! :sunglasses:")

# Data symmary
if data is not None:
    st.write("Data Summary")
    data_df = pd.DataFrame(data)
    st.write("Data info :", data_df.describe())
    st.write("Number of Rows :", data.shape[0])
    st.write("Number of Columns :", data.shape[1])
    st.write("Data Sample :")
    st.dataframe(data.head(21))


# Data visualization
if data is not None:
    st.header("Interactive Visualizations :bar_chart:")
    columns = data.columns.tolist()
    x_axis = st.selectbox("Select X-axis :", columns)
    y_axis = st.selectbox("Select Y-axis :", columns)

    plot_type = st.selectbox(
        "Select Plot Type:", ["Scatter", "Line",
                              "Bar", "Hist", "Box", "Heatmap"]
    )


# Scatter plot
    if plot_type == "Scatter":
        fig = px.scatter(data, x=x_axis, y=y_axis, color_discrete_sequence=px.colors.qualitative.Safe)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig)


# Line chart
    elif plot_type == "Line":
        fig = px.line(data, x=x_axis, y=y_axis, color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig)

# Bar chart
    elif plot_type == "Bar":
        fig = px.bar(data, x=x_axis, y=y_axis, color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig)

# Histogram
    elif plot_type == "Hist":
        fig = px.histogram(data, x=x_axis ,  color_discrete_sequence=px.colors.sequential.Pastel)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig)

# Box Plot
    elif plot_type == "Box":
        fig = px.box(data, x=x_axis, y=y_axis, color_discrete_sequence=px.colors.sequential.YlGnBu)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig)


# Heat Map
    elif plot_type == "Heatmap":
        fig = px.density_heatmap(data, x=x_axis, y=y_axis , color_continuous_scale='Viridis')
        st.plotly_chart(fig)


# Data Filtering
if data is not None:
    st.header("Data Filtering :hourglass_flowing_sand:")
    st.write("Filter data based on column value:")
    filter_column = st.selectbox("Select Column:", columns)

    # Get unique values of the selected column
    unique_values = data[filter_column].unique().tolist()

    # Convert user input to appropriate data type
    if pd.api.types.is_numeric_dtype(data[filter_column]):
        filter_value = st.number_input("Enter Value:", value=0)
    else:
        filter_value = st.selectbox("Select Value:", unique_values)

    # Filter the data
    filtered_data = data[data[filter_column] == filter_value]
    st.dataframe(filtered_data)

st.set_option('deprecation.showPyplotGlobalUse', False)
