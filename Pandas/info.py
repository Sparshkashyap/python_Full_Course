import pandas as pd


data = pd.read_json(r"C:\Users\Dell\Desktop\python\Pandas\Dataset\sample_Data.json",encoding="utf-8")

print(data.info())

