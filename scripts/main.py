import pandas as pd
from data_processing import clean_data
from eda import explore_data
from visualizations import create_visualizations

# Load dataset
df = pd.read_csv("data/amazon.csv")

# Clean data
df_cleaned = clean_data(df)

# Save cleaned data
df_cleaned.to_csv("output/cleaned_data.csv", index=False)

# Perform EDA
explore_data(df_cleaned)

# Generate visualizations
create_visualizations(df_cleaned)
