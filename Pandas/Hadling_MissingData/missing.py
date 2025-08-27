
import pandas as pd

dic={
    "Name":["Sparsh",None,"Aman","Anubhav","Uday"],
    "Age":[21,20,None,25,24],
    "City":["Saharanpur","Delhi","Asia","Yurup","North"],
    "Performance Score":[12,45,10,None,35],
    "Salary":[50000,40000,30000,None,75000]
}

df = pd.DataFrame(dic)

print(df)

# print(df.isnull())
print(df.isnull().sum())