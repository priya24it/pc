import requests
import json
import pandas as pd
import time
from xl2dict import XlToDict



data = pd.read_excel("Sample.xlsx")
df = pd.DataFrame(data)
print(df.columns.tolist())
df.to_excel("sample_amended.xlsx",index=False)
print(df)
df = df.drop(index=1)
print(df.columns.tolist())