"""Exercise 1"""
print("Name: Wissam Jemal")
print("Age:26")
print("JavaScript")

"""Exercise 2"""

price = 20
quantity = 12

"""Exercise 3"""
#Accept Numbers from user
num1 = int(input("Input first number: "))
num2 = int(input("Input second Number: "))

#Sum of numbers
print("Sum: ",num1 + num2)
#Difference of numbers
print("Difference: ",num1 - num2)
#Product of numbers
print("Sum: ",num1 * num2)

""" Exercise 4"""

#Accept score from user
score = int(input("Input score"))

if score >= 50:
    print("Pass")
else:
    print("Fail")


""" Exercise 5"""
#Accept student marks from user
mark = int(input("input student mark"))

if mark >= 80:
    print("A")
elif mark >= 70:
    print("B")
elif mark >= 60:
    print("C")
else:
    print("F")



"""Exercise 6 print even numbers from 1 - 20 """
for i in range(1,21):
    if i% 2 == 0:
        print(i)




"""Exercise 7 """
num = 10
sum_of_nums = 0

while(num > 0):
    sum_of_nums+= num
    num -=1

print(sum_of_nums)



"""Exercise 8"""
def rectangle_area(length ,width):
    return length * width
print(rectangle_area(2,4))

"""Exercise 9"""
square = lambda x: x**2
# Test it on numbers from 1 to 10
for i in range(1,11):
    print(square(i))

"""Exercise 10"""
list_com = [x**2 for x in range(1,21)]

print(list_com)

"""SECTION B: NUMPY"""

"""Exercise 11"""
#import numpy 
import numpy as np

numbers = np.arange(1,21)
print(numbers.shape)
print(numbers.dtype)
print(numbers.size)

"""Exercise 12: Array Operations"""
a = np.array([10,20,30,40])
b = np.array([5,10,15,20])

# Addition
print("Addition:" ,a + b)

# Subtraction
print("Subtraction:" ,a - b)
# Multiplication
print("Multiplication:" ,a * b)
# Division
print("Division:" ,a / b)


"""Exercise 13: Statistics Using NumPy (0.5 marks)"""
# For an array of exam scores:

exam_scores = np.array([100,67,53,80,90,78])
# Find the mean.
print("Mean: of score ",exam_scores.mean())

# Find the maximum value.
print("Maximum: score ",exam_scores.max())
# Find the minimum value.

print("Minimum score: ",exam_scores.min())
# Find the standard deviation.
print("Standard deviation: ",exam_scores.std())

"""Section C: Pandas DataFrames"""
"""Exercise 14: Create a DataFrame """

import pandas as pd

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

"""Exercise 17:Summary Statistics (0.6 marks)
Using .describe() :
Display:
Mean
Standard deviation
Minimum
Maximum values"""
print(df.describe().loc[["mean","std","min","max"]])

"""Section D: Data Cleaning
Exercise 18: Missing Values Detection (0.6 marks)"""

df = pd.DataFrame({
    "name": ["Abel","Sara",None,"John",None],
    "age":[22,21,np.nan,20,np.nan],
    })
print(df)

#Number of missing values in each column.
print(df.isna().sum())
#Total missing values in the dataset.
print(df.isna().sum().sum())


"""Replace missing numerical values using:
Mean
Median"""
df["age"] = df["age"].fillna(df["age"].mean())
print(df)
df["age"] = df["age"].fillna(df["age"].median())
print(df)

"""Exercise 20: Duplicate Records"""

df = pd.DataFrame({
     "name": ["Abebe","Sara","John","Sara","Abebe","Abel"],
    "score":[80,90,75,90,80,88]
})

# Identify duplicates.

print(df.duplicated())
# Remove duplicate records.
df_clean = df.drop_duplicates()
print(df_clean)

"""Exercise 21: Standardizing Text Data"""

city = pd.DataFrame({"city":["addis ababa", "ADDIS ABABA", "Addis Ababa", "adDis abaBa"]})

city["city"] = city["city"].str.title()
print(city)

"""Exercise 22: Correcting Data Entry Errors"""

df = pd.DataFrame({"age":[21, 25, 230, 30, 19, -5, 27]})
df["age"]= df["age"].apply(lambda x:np.nan if x < 0 or x > 120 else x)


"""exercise 23"""

df = pd.DataFrame({
    "name": ["Abel","Sara",None,"John",None,"Abel"],
    "age":[22,21,np.nan,20,np.nan,22],

    })
df_clean = df.drop_duplicates()
df_clean = df.dropna()
print(df_clean)
