# Importing a nesscessary modules

import numpy as np
import pandas as pd


# Loading the data

df = pd.read_csv(r"C:\Users\Dell\Desktop\python\Indian Emplyee Dataset\EmployeeID-Name-Department-Age-Salary-Location-Experience.csv")


#Check the null values

print(df.isnull().sum())

# Fill the none values -> AGE

df["Age"].fillna(df["Age"].mean(),inplace=True)

# Fill the none values ->   SALARY

df["Salary"].fillna(df["Salary"].mean(),inplace=True)

# fill the none values ->   Exprience

df["Experience"].fillna(df["Experience"].mean(),inplace=True)

# Replace the infinite value to the none value

df.replace([np.inf,-np.inf],np.nan,inplace=True)

df.fillna(df[["Age","Experience","Salary"]].mean(),inplace=True)

# Remove the Duplicate values

df.drop_duplicates(inplace=True)

#Replace the negative salary into the mean

df["Salary"] = np.where(df["Salary"]<0,df["Salary"].mean(),df["Salary"])

# Handle outlier (means ek limit sai jada salary and ek limit sai kam salary ko manage handle karna)

salary_mean = df["Salary"].mean()
salary_std = df["Salary"].mean()

lower_outlier= salary_mean - (3*salary_std)
upper_outlier = salary_mean + (3*salary_std)

# finally remove the rows and column

data = df[(df["Salary"]>=lower_outlier) & (df["Salary"]<=upper_outlier)]

# Cleaned data is occur

data.to_excel("sample.xlsx",index=False)

print("Data cleaning completed!")




