
import pandas as pd

dic={
    "Name":["Sparsh","Aditya","Aman","Anubhav","Uday"],
    "Age":[21,20,21,25,24],
    "City":["Saharanpur","Delhi","Asia","Yurup","North"],
    "Performance Score":[12,45,10,25,35],
    "Salary":[50000,40000,30000,80000,75000]
}

df = pd.DataFrame(dic)

# Adding a one column in the Dataset

df["Bonus"] = df["Salary"]*0.1

# print(df)

# Adding a column in a specific position in the Dataset. -> using insert() method

df.insert(0,"Emplyee ID",[10,20,30,40,50])
print(df)

# Update a value in the rows
df.loc[0,"Salary"] = 55000
print(df)