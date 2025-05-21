import streamlit as st
import pandas as pd

# Load processed data
df = pd.read_parquet("../curated_data/final_sales.parquet")

st.title("📊 Sales Analytics Dashboard")

# Filters
region = st.selectbox("Select Region", options=["All"] + list(df["region"].unique()))
product = st.selectbox("Select Product", options=["All"] + list(df["product"].unique()))

# Apply filters
filtered_df = df.copy()
if region != "All":
    filtered_df = filtered_df[filtered_df["region"] == region]
if product != "All":
    filtered_df = filtered_df[filtered_df["product"] == product]

# KPIs
st.metric("Total Revenue", f"${filtered_df['revenue'].sum():,.2f}")
st.metric("Total Units Sold", int(filtered_df['units_sold'].sum()))
st.metric("Average Revenue per Unit", f"${filtered_df['revenue_per_unit'].mean():.2f}")

# Table
st.subheader("Filtered Sales Data")
st.dataframe(filtered_df)
