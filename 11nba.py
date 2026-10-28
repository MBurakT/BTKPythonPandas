import pandas as pd

df = pd.read_csv("datasets/nba.csv")
cols = df.columns

result = df.head(10)
result = len(df.index)
result = df["Salary"].mean()
result = df["Salary"].max()
result = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0]
result = df[(df["Age"] > 20) & (df["Age"] < 25)][["Name", "Team", "Age"]].sort_values("Age", ascending = False)
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]

print(result)
# print(cols)