import pandas as pd

dic={
    "Name":["Sparsh","Aditya","Aman","Anubhav","Uday"],
    "Age":[21,20,21,25,24],
    "City":["Saharanpur","Delhi","Asia","Yurup","North"],
    "Performance Score":[12,45,10,25,35],
    "Salary":[50000,40000,30000,80000,75000]
}



df = pd.DataFrame(dic)

# Filtered a rows based on  single condition

High_Salary  = df[df["Salary"]<=50000]
# print(High_Salary)

# Filtered a rows based on multiple condition using logical operator -> And
filtered = df[(df["Age"]>20) & (df["Salary"]<80000)]
# print(filtered)

# Filtered a rows based on multiple condition using logical operator -> And

AnyOne = df[(df["Salary"]>50000) | (df["Age"]<22)]

print(AnyOne)

