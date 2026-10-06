import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

missing = df["Price"].isnull()

print("Before:")
print(df[missing][["Model", "Price"]])

average = df["Price"].mean()

df["Price"] = df["Price"].fillna(average)

print("\nAverage price:")
print(average)

print("\nAfter:")
print(df[missing][["Model", "Price"]])