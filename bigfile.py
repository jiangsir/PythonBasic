#C-B0024-002.json
import pandas as pd
import os, json
## C:\Users\user\Downloads

filename = os.path.join("C:/", "Users", "user", "Downloads", 'C-B0024-002.json')
with open(filename, 'r', encoding='UTF-8') as f:
    datas = json.loads(f.read())
print(len(datas))
