import streamlit as st
import pandas as pd
import numpy as np

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="CSV Data Analyzer",
    layout="wide"
)

st.title("📊 CSV Data Analyzer App")
st.write("Upload a CSV file and perform basic data analysis without writing code.")

# -----------------------
# File upload
# -----------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # -----------------------
    # Basic info
    # -----------------------
    st.subheader("📌 Dataset Information")
    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    # -----------------------
    # Missing value handling
    # -----------------------
    st.subheader("🧹 Handle Missing Values")

    option = st.selectbox(
        "Choose a method",
        ["Do Nothing", "Drop Rows", "Fill with Mean (numeric only)"]
    )

    if option == "Drop Rows":
        df = df.dropna()
        st.success("Rows with missing values removed.")

    elif option == "Fill with Mean (numeric only)":
        numeric_cols = df.select_dtypes(include=np.number).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        st.success("Missing values filled with column mean.")

    # -----------------------
    # Statistics
    # -----------------------
    st.subheader("📈 Statistical Summary")
    st.dataframe(df.describe())

    # -----------------------
    # Column selection
    # -----------------------
    st.subheader("📊 Visualization")

    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

    if len(numeric_columns) > 0:
        selected_col = st.selectbox("Select a numeric column", numeric_columns)
        st.line_chart(df[selected_col])
    else:
        st.warning("No numeric columns found for visualization.")

    # -----------------------
    # Filter data
    # -----------------------
    st.subheader("🔎 Filter Data")

    column_to_filter = st.selectbox("Select column", df.columns)

    unique_values = df[column_to_filter].dropna().unique().tolist()

    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[column_to_filter] == selected_value]
    st.dataframe(filtered_df)

    # -----------------------
    # Download cleaned data
    # -----------------------
    st.subheader("⬇️ Download Cleaned Data")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload a CSV file to start analysis.")
