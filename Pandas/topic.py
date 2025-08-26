import pandas as pd
"""
what is the size of your Dataset
what are the names of the column

Shape and Column 

"""


dic={
    "Name":["Sparsh","Aditya","Aman","Anubhav","Uday"],
    "Age":[21,20,21,25,24],
    "City":["Saharanpur","Delhi","Asia","Yurup","North"],
    "Performance Score":[12,45,10,25,35]
}


df = pd.DataFrame(dic)

print(df)
print(f"Shape :{df.shape}")
print(f"Column is :{df.columns}")