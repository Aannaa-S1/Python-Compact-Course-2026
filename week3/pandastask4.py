import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

print("Column names:")
print(df.columns)

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nTotal missing values:")
print(df.isnull().sum().sum())