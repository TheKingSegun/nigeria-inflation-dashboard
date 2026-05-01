"""
Nigeria CPI Data Pipeline
Cleans and transforms raw NBS inflation data for analysis and Power BI ingestion.
"""
import pandas as pd
import numpy as np
import os

RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"

def clean_cpi_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardise NBS CPI dataset."""
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
        df = df.sort_values("date").reset_index(drop=True)
    numeric_cols = [c for c in df.columns if c != "date"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["date"])
    if "headline_cpi" in df.columns:
        df["mom_inflation"] = df["headline_cpi"].pct_change() * 100
        df["yoy_inflation"] = df["headline_cpi"].pct_change(12) * 100
    return df

def add_food_core_spread(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate spread between food and core inflation."""
    if "food_cpi" in df.columns and "core_cpi" in df.columns:
        df["food_yoy"] = df["food_cpi"].pct_change(12) * 100
        df["core_yoy"] = df["core_cpi"].pct_change(12) * 100
        df["food_core_spread"] = df["food_yoy"] - df["core_yoy"]
    return df

def generate_sample_data() -> pd.DataFrame:
    """Generate realistic NBS-style CPI sample data."""
    dates = pd.date_range(start="2019-01-01", end="2024-12-01", freq="MS")
    np.random.seed(42)
    df = pd.DataFrame({
        "date": dates,
        "headline_cpi": np.cumsum(np.random.uniform(0.8, 2.5, len(dates))) + 280,
        "food_cpi": np.cumsum(np.random.uniform(1.0, 3.0, len(dates))) + 310,
        "core_cpi": np.cumsum(np.random.uniform(0.6, 2.0, len(dates))) + 260,
        "urban_cpi": np.cumsum(np.random.uniform(0.9, 2.8, len(dates))) + 290,
        "rural_cpi": np.cumsum(np.random.uniform(0.7, 2.2, len(dates))) + 270,
    })
    df = add_food_core_spread(df)
    df["mom_inflation"] = df["headline_cpi"].pct_change() * 100
    df["yoy_inflation"] = df["headline_cpi"].pct_change(12) * 100
    return df

if __name__ == "__main__":
    df = generate_sample_data()
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/nigeria_cpi_processed.csv", index=False)
    print(f"Pipeline complete. {len(df)} records saved.")
    print(df.tail())
