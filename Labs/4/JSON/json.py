import json
from json import load

# f = open(r'/Users/kakimbekn/Library/CloudStorage/OneDrive-АОКазахстанско-БританскийТехническийУниверситет/My Personal Data/docslocal/GitHub/pp2/Labs/4/JSON/a.json')
# data = json.load(f)

with open("/Users/kakimbekn/Library/CloudStorage/OneDrive-АОКазахстанско-БританскийТехническийУниверситет/My Personal Data/docslocal/GitHub/pp2/Labs/4/JSON/a.json", "r") as file:
    data = json.load(file)


print('''=======================================================================================
DN                                                 Description           Speed    MTU" 
-------------------------------------------------- --------------------  ------  ------''')

imdata = data["imdata"]
for i in imdata:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print("{0:51} {1:20} {2:8} {3:6}".format(dn,descr,speed,mtu))

f.close()
