import pandas as pd

# Load dataset
jobs = pd.read_csv("data/raw/postings.csv")

print("========== DATASET OVERVIEW ==========")

# Rows and columns
print("\nShape:")
print(jobs.shape)

# Data types
print("\nData Types:")
print(jobs.dtypes)

# Missing values
print("\nMissing Values:")
print(jobs.isnull().sum())

# Unique values
print("\nUnique Values:")
print(jobs.nunique())

# Duplicate rows
print("\nDuplicate Rows:")
print(jobs.duplicated().sum())