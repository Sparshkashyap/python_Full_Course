
import pandas as pd


dic={

    "Name":["Sparsh","Aditya","Aman"],
    "City":["Saharanpur","Yamunanagar","Delhi"],
    "Age":[21,20,20]
}


df = pd.DataFrame(dic)

# df.to_csv("output.csv",index=False)
# df.to_excel("output.xlsx",index=False)
# df.to_json("output.json",index=False)



print(df.info())