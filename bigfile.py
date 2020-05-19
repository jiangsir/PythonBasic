#C-B0024-002.json
import pandas as pd
import os, json
## C:\Users\user\Downloads

#filename = os.path.join("C:/", "Users", "user", "Downloads", 'C-B0024-002.json')
#filename = os.path.join("D:/", "Download", 'C-B0024-002.json')

filename = os.path.join(os.sep, "mnt","d", "Download", 'C-B0025-002', 'dy_Report_2019.json')

with open(filename, 'r', encoding='UTF-8') as f:
    datas = json.loads(f.read())

locations = datas['cwbdata']['resources'][0]['resource'][0]['data'][0]['surfaceObs'][0]['location']

#for location in locations:
location = locations[0]
stationObsTime = location['stationObsTimes'][0]['stationObsTime']
print(location['station'][0]['stationName'], len(stationObsTime))
for day in stationObsTime:
    print(day['dataDate'][0], day['weatherElements'][0]['precipitation'][0])