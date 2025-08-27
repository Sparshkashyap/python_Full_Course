import pandas as pd

dic = {
    "Name":["Sparsh","Aditya","Aman","Sohan","Rohan"],
    "Age":[20,21,24,25,25],
    "Salary":[5000,5500,4000,4500,5500]

}

df=pd.DataFrame(dic)
# Some Aggeregation methods
"""
df["Salary"].mean()
df["Salary"].sum()
df["Salary"].min()
df["Salary"].max()

"""
avg_salary = df["Salary"].mean()
Total_sum = df["Salary"].sum()
Max = df["Salary"].max()
Min = df["Salary"].min()

print(f"Average Salary is :{avg_salary}")
print(f"Total Sum is :{Total_sum}")
print(f"Minimum value is :{Min}")
print(f"Maximum value is :{Max}")