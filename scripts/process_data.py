import pandas as pd
import os

# Paths
RAW_PATH = "./raw_data/sales_data.csv"
PROCESSED_PATH = "./processed_data/cleaned_sales.csv"
CURATED_PATH = "./curated_data/final_sales.parquet"

# Ensure folders exist
os.makedirs("./processed_data", exist_ok=True)
os.makedirs("./curated_data", exist_ok=True)

# Load raw data
df = pd.read_csv(RAW_PATH)

# Clean: drop nulls, standardize columns
df.dropna(inplace=True)
df.columns = df.columns.str.lower().str.replace(" ", "_")
df["revenue_per_unit"] = df["revenue"] / df["units_sold"]

# Save intermediate CSV
df.to_csv(PROCESSED_PATH, index=False)

# Save final Parquet
df.to_parquet(CURATED_PATH, index=False)

print("✅ Data processed successfully.")
