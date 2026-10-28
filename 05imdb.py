import pandas as pd

df = pd.read_csv("datasets/imdb.csv")
cols = df.columns

result = df.head()
result = df.head(10)
result = df.tail()
result = df.tail(10)
result = df["Movie_Title"]
result = df["Movie_Title"].head()
result = df[["Movie_Title", "Rating"]].head()
result = df[["Movie_Title", "Rating"]].head(7)
result = df[5:10][["Movie_Title", "Rating"]]
result = df[df["Rating"] >= 8.0][["Movie_Title", "Rating"]]
result = df.query("Rating >= 8.0")[["Movie_Title", "Rating"]].head(50)
result = df.query("YR_Released >= 2014 & YR_Released <= 2015")
result = df.query("Num_Reviews > 100000 | (Rating > 8 & Rating < 9)")
result = df.query("Num_Reviews > 100000 | (Rating > 8 & Rating < 9)").head()
result = df.query("Num_Reviews > 100000 | (Rating > 8 & Rating < 9)")["Movie_Title"].head()
result = df.query("Num_Reviews > 100000 | (Rating > 8 & Rating < 9)")[["Movie_Title", "Rating"]].head()

print(result)
# print(cols.tolist())