import pandas as pd

import numpy as np

data = {"Name":["Abel","Sara","john","Hana"],
        "Age":[22,21,23,20],
        "score":[90,68,98,85]}
df = pd.DataFrame(data)

#Display the first three rows.
print(df[0:3])
# Display only the Name column.
print(df["Name"])
# Display students whose score is greater than 70.
print("students whose score is greater than 70.")
print(df[df["score"] > 70])



"""Exercise 16: Adding New Columns"""
df["status"] = np.where(df["score"]>= 50 ,"Pass","Fail")
print(df)

df = pd.DataFrame({
    "name": ["Abel","Sara",None,"John",None,"Abel"],
    "age":[22,21,np.nan,20,np.nan,22],

    })
df_clean = df.drop_duplicates()
df_clean = df.dropna()
print(df_clean)
