import pandas as pd

df = pd.read_csv("nailib_data_cleaned.csv", delimiter=',')

print(df.head(10))

print(df)
