import pandas as pd


df_1  = pd.DataFrame({
    "CustomerID":[1,2],
    "Name":["Sparsh","Aditya"]
})

df_2 = pd.DataFrame({
    "CustomerID":[3,4],
    "Name":["Sohan","Mohan"]
})

# Use a concatenation method

df_concatenate = pd.concat([df_1,df_2],ignore_index=True) # Vertically concatenate axis=0
df_concatenate = pd.concat([df_1,df_2],axis=0,ignore_index=True) # Horizontally concatenate axis=1
print(df_concatenate)

