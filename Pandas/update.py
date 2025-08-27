
import pandas as pd

dic={
    "Name":["Sparsh","Aditya","Aman","Anubhav","Uday"],
    "Age":[21,20,21,25,24],
    "City":["Saharanpur","Delhi","Asia","Yurup","North"],
    "Performance Score":[12,45,10,25,35],
    "Salary":[50000,40000,30000,80000,75000]
}

df=pd.DataFrame(dic)
# Update the multiple values in the column

df["Salary"] = df["Salary"]*0.05
print(df)