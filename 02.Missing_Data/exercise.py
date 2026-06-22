import pandas as pd
import numpy as np

students = pd.DataFrame({
    "student_id":[101,102,103,104,105,106,107,108,109,110],
    "name": ["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
    "department":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
    "gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
    "scholarship": [5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
})

print(students)
print(50*"=")
print(students.isnull())
print(50*"=")
print(students.isnull().sum().sum())
print(50*"=")
print(students.isnull().sum() / len(students) * 100)
print(50*"=")
print(students.columns[students.isnull().any()])
print(50*"=")
print(students[students.isnull().any(axis=1)])
print(50*"=")
print(students[students["gpa"].isnull()])
print(50*"=")
print(students[students["scholarship"].isnull()])
print(50*"=")
students["name"] = students["name"].fillna("Unknown")
print(students)
print(50*"=")
students["gpa"] = students["gpa"].fillna(students["gpa"].mean())

print(students)
print(50*"=")
students["gpa"] = students["gpa"].fillna(students["gpa"].median())
print(students)
print(50*"=")
students["department"] = students["department"].fillna(students["department"].mode())
print(students)
print(50*"=")

students["scholarship"] = students["scholarship"].fillna(0)
print(students)
print(50*"=")


students = pd.DataFrame({
    "student_id":[101,102,103,104,105,106,107,108,109,110],
    "name": ["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
    "department":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
    "gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
    "scholarship": [5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
})
print(students)
print(students.dropna())
print(students.dropna(axis=1))

print(50*"=")

students["missing_scholarship"] = students["scholarship"].isnull()
print(students)

print(students.isnull().sum())
print(students.isnull().sum().idxmax())
print(students.isnull().sum().idxmin())

print(100 - (students.isnull().sum().sum() / students.size)*100 )

for col in students.columns:
    print(col)
for col in students.columns:
    print(col,students[col].dtype)
for index,row in students.iterrows():
    print(row["name"],row["gpa"])
print("=====grade greater than 3.5====")
for index,row in students.iterrows():
    if(row["gpa"]> 3.5):
        print(row["name"],row["gpa"])
print("=====Scholarship recipients====")
for index ,row in students.iterrows():
    if row["scholarship"] > 0:
        print(row["name"])
catagories = []
for index ,row in students.iterrows():
    if row["gpa"] > 3.7:
        catagories.append("excelent")
    elif row["gpa"] > 3.0:
        catagories.append("good")
    else:
        catagories.append("at risk")

students['catagories'] = catagories
print("="*50)
print(students)
print("="*50)
for row in students.itertuples():
    print(row.student_id,row.name)
print("===Exercise 29=====")

counts = {}