import json

f = open("D:/Code/PoGoDaysSince/data/raidData.json")

data = json.load(f)

dateForeachCodeDict = {}

for date in range(len(data)):
    dateString = data[str(date)]['date']

    for code in data[str(date)]['codes']:
        if code not in dateForeachCodeDict:
            dateForeachCodeDict[code] = dateString

print(dateForeachCodeDict)