import pandas as pd

dic={
    "Name":["Sparsh","Aditya","Aman","Anubhav","Uday"],
    "Age":[21,20,21,25,24],
    "City":["Saharanpur","Delhi","Asia","Yurup","North"],
    "Performance Score":[12,45,10,25,35]
}


data = pd.DataFrame(dic)

# print(data[["Age","Performance Score"]].count()
# )
print(data[["Age","Performance Score"]].mean())

print(data)

print("Descriptive statics")

print(data.describe())