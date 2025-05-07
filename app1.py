import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="📊 DataFrame Viewer", page_icon="📁", layout="centered")

# Title
st.title("📊 DataFrame Viewer")
st.markdown("### 🎯 *Objective: Load and display data interactively*")

# File uploader
uploaded_file = st.file_uploader("📂 Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Load the CSV with pandas
    df = pd.read_csv(uploaded_file)

    # Check column count
    if df.shape[1] < 5:
        st.warning("⚠️ The uploaded file must have at least 5 columns.")
    else:
        # Show checkbox to view raw data
        if st.checkbox("Show raw data"):
            st.dataframe(df)

        # Select column to filter
        column_to_filter = st.selectbox("🔎 Select a column to filter", df.columns)

        # Unique values from that column
        selected_value = st.selectbox(f"Filter by value in '{column_to_filter}'", df[column_to_filter].unique())

        # Filtered DataFrame
        filtered_df = df[df[column_to_filter] == selected_value]

        st.markdown("### 📌 Filtered Data")
        st.dataframe(filtered_df)
else:
    st.info("👈 Please upload a CSV file to get started.")
