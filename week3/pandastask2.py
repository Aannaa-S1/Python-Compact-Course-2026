import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

print("Original DataFrame:")
print(df.head())

series = df["Model"]

df.set_index(series, inplace=True)

print("\nChanged DataFrame:")
print(df.head())