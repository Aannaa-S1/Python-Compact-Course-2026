import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

print("Original columns:")
print(df.columns)

def exchange_columns(df, col1, col2):
    columns = list(df.columns)
    i = columns.index(col1)
    j = columns.index(col2)
    columns[i], columns[j] = columns[j], columns[i]
    return df[columns]

df = exchange_columns(df, "Manufacturer", "Model")

print("\nAfter exchange:")
print(df.columns)

df = df[sorted(df.columns)]

print("\nSorted columns:")
print(df.columns)