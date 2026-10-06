import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

data = df[["Price", "Horsepower", "MPG.city"]]

corr = data.corr()

print(corr)