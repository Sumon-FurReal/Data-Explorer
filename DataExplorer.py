import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
        "Select Plot Type:", ["scatter", "line",
                              "bar", "hist", "box", "heatmap"]
    )

# Scatter plot
    if plot_type == "scatter":
        plt.figure(figsize=(8, 6))
        plt.scatter(data[x_axis], data[y_axis])
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        st.pyplot()

# Line chart
    elif plot_type == "line":
        plt.figure(figsize=(8, 6))
        plt.plot(data[x_axis], data[y_axis])
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        st.pyplot()

# Bar chart
    elif plot_type == "bar":
        plt.figure(figsize=(10, 6))
        sns.barplot(x=x_axis, y=y_axis, data=data)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        st.pyplot()

# Histogram
    elif plot_type == "hist":
        plt.figure(figsize=(8, 6))
        plt.hist(data[x_axis], bins=10, edgecolor='black')
        plt.xlabel(x_axis)
        plt.ylabel("Frequency")
        st.pyplot()

# Box Plot
    elif plot_type == "box":
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=x_axis, y=y_axis, data=data)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        st.pyplot()

# Heat Map
    elif plot_type == "heatmap":
        plt.figure(figsize=(10, 8))
        heatmap_data = data.pivot_table(
            index=x_axis, columns=y_axis, values=columns[0])
        sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu")
        st.pyplot()

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