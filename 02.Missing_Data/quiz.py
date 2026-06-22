""" Wissam Jemal"""
import pandas as pd
import numpy as np

university = pd.DataFrame({
    "student_id":[201,202,203,204,205,206,207,208,209,210],
    "name": ["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
    "department":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
    "gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
    "scholarship": [5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
})

#1.Count missing values 

print("Missing values per row",university.isnull().sum())
print("Total missing values",university.isnull().sum().sum())

#2.missing values percentage
print("Missing value percentage per row",university.isnull().sum() / len(university) * 100)


#3.replace missing names with "unknown"

university["name"] = university["name"].fillna("Unknown")
print(university)

#4 replace missing deparment using mode 

university["department"] = university["department"].fillna(university["department"].mode()[0])
print(university)
#5.Replace missing GPA with median

university["gpa"] = university["gpa"].fillna(university["gpa"].median())
print(university)
#6.Replace missing scholarship with 0
university["scholarship"] = university["scholarship"].fillna(0)
print(university)