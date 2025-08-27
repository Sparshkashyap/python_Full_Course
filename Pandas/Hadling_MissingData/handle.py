
import pandas as pd

dic={
    "Name":["Sparsh",None,"Aman","Anubhav","Uday"],
    "Age":[21,20,None,25,24],
    "City":["Saharanpur","Delhi","Asia","Yurup","North"],
    "Performance Score":[12,45,10,None,35],
    "Salary":[12,None,15,None,None]
}

df = pd.DataFrame(dic)

# print(df)

# df.dropna(how="all",axis=1,inplace=True) # If all the values is NAN then it remove that column
df.dropna(axis=0,inplace=True,how="any")
# df.dropna(inplace=True)
print(df)
