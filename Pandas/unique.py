import pandas as pd
import json
from itertools import zip_longest

with open("/Pandas/Dataset/simple_2.json","r",encoding="utf-8") as f:
    data = json.load(f)

# dict ke values ko equal length bana kar DataFrame
keys = list(data.keys())
rows = list(zip_longest(*data.values()))   # chhoti lists ko None fill karega
df = pd.DataFrame(rows,columns=keys)

print(df.tail(10))
