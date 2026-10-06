import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

print("Original:")
print(df[["Model", "Price"]])

low = df["Price"].quantile(0.05)
high = df["Price"].quantile(0.95)

df = df[
    ((df["Price"] >= low) & (df["Price"] <= high))
    | df["Price"].isnull()
]

print("\nAfter deleting lower and upper 5%:")
print(df[["Model", "Price"]])