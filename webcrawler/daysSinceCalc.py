import json

f = open("D:/Code/PoGoDaysSince/data/raidData.json")

data = json.load(f)
raidsDict = {}

# for date in data:
#     print(date)

print(data)