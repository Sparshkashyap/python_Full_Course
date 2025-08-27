import pandas as pd

dic={

    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]

}

print("Before Interprolation")
df = pd.DataFrame(dic)

print(df)

print("Linear Interpolation")

df["Value"] = df["Value"].interpolate(method="linear")
print(df)