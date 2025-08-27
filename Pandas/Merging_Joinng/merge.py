import pandas as pd 

df_customerName = pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":["Sparsh","Aditya","Rohan"]
})

df_customerOrder = pd.DataFrame({
    "CustomerID":[2,3,4],
    "Price":[350,400,300]
})

df_merge = pd.merge(df_customerName,df_customerOrder,on="CustomerID",how="left")
print(df_merge)