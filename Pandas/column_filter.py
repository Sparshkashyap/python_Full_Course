import pandas as pd

dic={
    "Name":["Sparsh","Aditya","Aman","Anubhav","Uday"],
    "Age":[21,20,21,25,24],
    "City":["Saharanpur","Delhi","Asia","Yurup","North"],
    "Performance Score":[12,45,10,25,35],
    "Salary":[50000,40000,30000,80000,75000]
}


df = pd.DataFrame(dic)

# Display the dataset

print(df)

print("Names (single column return a series)")

name = df["Name"]
print(name)

# Selecting multiple columns

subset = df[["Name","Salary"]]
print("\n Subset with name and salary")
print(subset)
