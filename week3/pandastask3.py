import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

print("Original:")
print(df[["Model", "Price"]].head(10))

def change_price(x):
    if x > 30:
        return 30
    else:
        return x

df["Price"] = df["Price"].apply(change_price)

print("\nChanged:")
print(df[["Model", "Price"]].head(10))