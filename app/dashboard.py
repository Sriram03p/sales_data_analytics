import streamlit as st
import pandas as pd

# Load curated data
df = pd.read_parquet("../curated_data/final_sales.parquet")

st.set_page_config(page_title="Sales Data Lake Dashboard", layout="wide")
st.title("📊 Sales Data Lake Dashboard")

# Filters
col1, col2 = st.columns(2)
region = col1.selectbox("Filter by Region", options=["All"] + sorted(df["region"].unique()))
product = col2.selectbox("Filter by Product", options=["All"] + sorted(df["product"].unique()))

# Apply filters
filtered_df = df.copy()
if region != "All":
    filtered_df = filtered_df[filtered_df["region"] == region]
if product != "All":
    filtered_df = filtered_df[filtered_df["product"] == product]

# KPIs
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("💰 Total Revenue", f"${filtered_df['revenue'].sum():,.2f}")
kpi2.metric("📦 Total Units Sold", int(filtered_df['units_sold'].sum()))
kpi3.metric("📊 Avg Revenue/Unit", f"${filtered_df['revenue_per_unit'].mean():.2f}")
top_product = filtered_df.groupby("product")["revenue"].sum().idxmax() if not filtered_df.empty else "N/A"
kpi4.metric("🏆 Top Product", top_product)

# Table
st.subheader("📋 Filtered Sales Data")
st.dataframe(filtered_df)

# Plot
st.subheader("📈 Revenue by Product")
revenue_chart = filtered_df.groupby("product")["revenue"].sum().sort_values(ascending=False)
st.bar_chart(revenue_chart)
