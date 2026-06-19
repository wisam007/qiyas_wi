import pandas as pd
import numpy as np

data = {"Name":["Abel","Sara","john","Hana"],
        "Age":[22,21,23,20],
        "GPA":[3.8,3.5,3.2,3.9],
        "Departments" : ["CS","IT","SE","DS"]}
df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print("1st 3 rows")
print(df.head(3))


print("Last 2 rown")
print(df.tail(2))


print("Name Column")
print(df["Name"])

print("Name and GPA")
print(df[["Name","GPA"]])


print("Using Loc")
print(df.iloc[2])

print("Sara's GPA")
print(df.loc[1,"GPA"])

print("Hana's age using iloc")
print(df.iloc[3,2])

print("Students older than 21")
print(df[df["Age"] > 21])

print("Students GPA > 3.5")
print(df[df["GPA"] > 3.5])


print("Students older than 20 and Students GPA > 3.5")
print(df[
    (df["Age"] > 20) & 
    (df["GPA"] > 3.5)]
    )

print(df[
    (df["Departments"] == "CS") 
    | 
    (df["Departments"] == "IT")
    
    ])
df["Percentage"] = df["GPA"] * 25
print(df)

print("Pass/Fail Column")
df["Pass"] = df["GPA"].apply(lambda x: "Pass" if x >=2.0 else "Fail")
print(df)

print("Find average age")
print(df["Age"].mean())

print("Max GPA")
print(df["GPA"].max())

print("Min GPA")
print(df["GPA"].min())

print(df["Age"].sum())

print(df["Name"].count())
print(df.sort_values("GPA",ascending=False))

def classify(gpa):
    if gpa >= 3.7:
        return "Distinction"
    elif gpa >= 3.0:
        return "Very Good"
    elif gpa >= 2.0:
        return "Good"
    return "Probation"
df["Clasification"] = df["GPA"].apply(classify)

print(df)
    




"""========================================================="""

data = {"Name":["Abel","Sara","John"],
        "Age":[22,np.nan,23]}

df = pd.DataFrame(data)

print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.fillna(0))

# df["Age"] = df["Age"].fillna(df["Age"].mean())
# print(df)

print(df.dropna())

for row in df.itertuples():
    print(row.Name)


# departments = ["CS","IT","SE","DS"]
# dep_df = pd.DataFrame(departments)
# print(dep_df)