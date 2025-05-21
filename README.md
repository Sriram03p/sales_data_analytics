# 📦 Data Lake Demo Project

## 📝 Project Description

This project demonstrates a basic implementation of a **Data Lake** using local file system storage and Python-based ETL. The use case is centered around **sales data analysis** where raw sales data is ingested, processed, and visualized via a Streamlit dashboard.

---

## 🧱 Data Lake Architecture

```
                 ┌────────────────────┐
                 │   Raw Zone         │
                 │ sales_data.csv     │
                 └────────┬───────────┘
                          │
                          ▼
                 ┌────────────────────┐
                 │ ETL Script         │
                 │ process_data.py    │
                 └────────┬───────────┘
                          ▼
        ┌────────────┐        ┌────────────┐
        │ Processed   │        │ Curated    │
        │ cleaned.csv │        │ final.parquet │
        └────────────┘        └────────────┘
                                  │
                                  ▼
                 ┌────────────────────────┐
                 │ Streamlit Dashboard    │
                 │ (dashboard.py)         │
                 └────────────────────────┘
```



## 🔧 Steps to Run the Project

### 1. Install Dependencies

```bash
pip install pandas pyarrow streamlit
```

### 2. Run ETL Pipeline

```bash
python scripts/process_data.py
```

This loads raw CSV, cleans and transforms the data, and saves it in Parquet format.

### 3. Run Streamlit Dashboard

```bash
streamlit run app/dashboard.py
```

This will open a web browser displaying the dashboard with KPIs and visualizations.

---

## 📊 KPIs Available in Dashboard

* 📈 Total Revenue
* 📦 Total Units Sold
* 📍 Unique Regions
* 🛒 Unique Products
* 📅 Time-based Sales Trend (Bar Chart)
* 📍 Region-wise Revenue Distribution (Pie Chart)

---

## 🎯 Purpose

* Understand how data flows in a Data Lake.
* Simulate Raw → Processed → Curated zones.
* Practice working with Parquet files and dashboards.

---