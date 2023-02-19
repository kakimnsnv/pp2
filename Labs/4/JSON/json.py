import json
from json import loads, load
f = open ('a.json', "r")
  
data = json.loads(f.read())

print(data)
f.close()
