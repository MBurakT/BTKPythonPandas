import pandas as pd



data = pd.read_csv("datasets/nba.csv")
data = data.dropna()
cols = data.columns

# data["Name"] = data["Name"].str.upper()
# data["Name"] = data["Name"].str.lower()
data["index"] = data["Name"].str.find('a')

result = data.Name.str.contains("Jordan")
result = data[data.Name.str.contains("Jordan")]
result = data.Team.str.replace(' ', '-')
result = data.Team.str.replace(' ', '-').str.replace('*', '')

data[["FirstName", "LastName"]] = data["Name"].loc[data["Name"].str.split(' ').str.len() == 2].str.split(' ', expand = True)


print(data.head(10))
print(cols)