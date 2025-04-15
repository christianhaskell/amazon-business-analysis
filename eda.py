import pandas as pd

def explore_data(df):
    """Perform exploratory data analysis."""
    print("\nDataset Overview:")
    print(df.info())
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print("\nStatistical Summary:")
    print(df.describe())
    
    print("\nTop 5 Most Popular Products:")
    print(df.nlargest(5, 'rating_count')[['product_name', 'rating', 'rating_count']])
