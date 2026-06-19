import pandas as pd
import numpy as np

df = pd.DataFrame({
    "student_id":[101,102,103,102,104,101],
    "name": ["Abel","Sara","John","Sara","Helen","Abel"],
    "score":[80,90,75,90,88,80]})

print("Duplicate Count: ",df.duplicated().sum())

df_clean = df.drop_duplicates()
print(df_clean)
df_last = df.drop_duplicates(keep="last")
print(df_last)

df = pd.DataFrame({
    "id":[1,2,3,4],
    "email":[
        "a@gmail.com",
        "b@gmail.com",
        "a@gmail.com",
        "c@gmail.com",
    ]
})
duplicated = df[df.duplicated(subset=["email"])]
print(duplicated)
clean_df = df.drop_duplicates(subset="email")
print(clean_df)

df = pd.DataFrame({
    "city":[
        "addis ababa",
        "ADDIS ABABA",
        "Addis Ababa",
        "adDis abAba"
    ]
})

df["upper"] = df["city"].str.upper()
df["lower"] = df["city"].str.lower()
df["title"] = df["city"].str.title()
print(df)