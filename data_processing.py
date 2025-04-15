import pandas as pd
import numpy as np
import re

def clean_price(value):
    """Convert price columns from strings (₹, commas) to numeric."""
    return float(re.sub(r"[₹,]", "", value)) if isinstance(value, str) else np.nan

def clean_discount(value):
    """Convert discount percentage from string to numeric."""
    return float(value.replace("%", "")) if isinstance(value, str) else np.nan

def clean_data(df):
    """Clean and preprocess Amazon dataset."""
    # Convert prices to numeric
    df["discounted_price"] = df["discounted_price"].apply(clean_price)
    df["actual_price"] = df["actual_price"].apply(clean_price)
    
    # Convert discount percentage
    df["discount_percentage"] = df["discount_percentage"].apply(clean_discount)
    
    # Convert ratings to numeric
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    
    # Convert rating count to numeric (remove commas)
    df["rating_count"] = df["rating_count"].str.replace(",", "").astype(float)
    
    # Drop duplicate entries if any
    df.drop_duplicates(inplace=True)
    
    return df
