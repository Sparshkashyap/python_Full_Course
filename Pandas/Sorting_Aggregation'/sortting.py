import pandas as pd

dic = {
    "Name":["Sparsh","Aditya","Aman","Sohan","Rohan"],
    "Age":[20,21,24,25,25],
    "Salary":[5000,5500,4000,4500,5500]

}

df=pd.DataFrame(dic)

# print(df)

# Sorting methods

df.sort_values(by=["Salary","Name"],ascending=[True,True],inplace=True)
df.sort_values(by="Salary",ascending=True,inplace=True)
print(df)
