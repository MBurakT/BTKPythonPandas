import pandas as pd

data = [["Ahmet", 50], ["Ali", 60], ["Su", 70], ["Veli", 80]]
dict = {
    "Name": ["Ahmet", "Ali", "Su", "Veli"], 
    "Grade": [50, 60, 70, 80]}
dict_list = [
    {"Name": "Ahmet", "Grade": 50},
    {"Name": "Ali", "Grade": 60},
    {"Name": "Su", "Grade": 70},
    {"Name": "Veli", "Grade": 80}]

# df = pd.DataFrame()
# df = pd.DataFrame([1, 2, 3, 4])
# df = pd.DataFrame(data, index = [1, 2, 3, 4], columns = ["Name", "Grade"])
# df = pd.DataFrame(dict, index = ["212", "232", "236", "456"])
df = pd.DataFrame(dict_list, index = ["212", "232", "236", "456"])

print(df)

# s1 = pd.Series([3, 2, 1, 0])
# s2 = pd.Series([0, 3, 7, 2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)

# print(df)