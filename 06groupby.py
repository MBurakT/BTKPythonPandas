import pandas as pd
import numpy as np

personeller = {
    "Çalışan" : ["Ahmet Yılmaz", "Can Ertürk", "Hasan Korkmaz", "Cenk Saymaz", "Ali Turan", "Rıza Ertürk", "Mustafa Can"], 
    "Departman" : ["İnsan Kaynakları", "Bilgi işlem", "Muhasebe", "İnsan Kaynakları", "Bilgi işlem", "Muhasebe", "Bilgi işlem"], 
    "Yaş" : [30, 25, 45, 50, 23, 34, 42], 
    "Semt" : ["Kadıköy", "Tuzla", "Maltepe", "Tuzla", "Kadıköy", "Tuzla", "Maltepe"], 
    "Maaş" : [5000, 3000, 4000, 3500, 2750, 6500, 4500]
}

df = pd.DataFrame(personeller)

result = df
result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman", "Semt"]).groups

# for name, group in df.groupby("Semt"):
#     print(name)
#     print(group)

# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").get_group("Muhasebe")
result = df.groupby("Departman").sum()
result = df[["Departman", "Yaş", "Maaş"]].groupby("Departman").mean()
result = df[["Departman", "Yaş", "Maaş"]].groupby("Departman")["Maaş"].mean()
result = df[["Semt", "Yaş"]].groupby("Semt")["Yaş"].mean()
result = df[["Semt", "Maaş"]].groupby("Semt")["Maaş"].mean()
result = df.groupby("Semt")["Çalışan"].count()
result = df[["Departman", "Yaş"]].groupby("Departman").max()
result = df[["Departman", "Maaş"]].groupby("Departman").min()
result = df[["Departman", "Maaş"]].groupby("Departman").min().loc["Muhasebe"]
result = df[["Departman", "Yaş", "Maaş"]].groupby("Departman").agg(np.mean)
result = df[["Departman", "Yaş", "Maaş"]].groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.min, np.max])
result = df[["Departman", "Yaş", "Maaş"]].groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.min, np.max]).loc["Muhasebe"]

print(result)