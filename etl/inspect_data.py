import pandas as pd

# Load the job postings dataset
jobs = pd.read_csv("data/raw/postings.csv")

# Show number of rows and columns
print("Shape of dataset:")
print(jobs.shape)

# Show column names
print("\nColumns:")
print(jobs.columns.tolist())

# Show first 5 rows
print("\nFirst 5 rows:")
print(jobs.head())