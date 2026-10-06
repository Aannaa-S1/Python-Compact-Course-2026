import pandas as pd

dict1 = {
    "ID": [1, 2, 3],
    "Name": ["Anna", "Bob", "Tom"]
}

dict2 = {
    "ID": [1, 2, 3],
    "Age": [20, 25, 30]
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

merged = pd.merge(df1, df2, on="ID")

print("\nMerged:")
print(merged)

df1["Age"] = df2["Age"]

print("\nAfter adding column:")
print(df1)