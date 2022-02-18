import json


fileObject = open ("data.json",  "r", encoding="UTF-8")
jsonContent = fileObject.read()
ListofItem = json.loads(jsonContent)



#print (ListOfItem)

mincost=11_000

maxcost=30_000

FoundCost=[]

for item in ListofItem:

    if int(item ['cost']) >=mincost and int(item ['cost']) <=maxcost:

        FoundCost.append(item)

FoundU=[]

print (FoundCost)

# minu=20000

# maxU=120000
# Foundu=[]
# for item in FoundCost:

#     if int(item ['U']) >=minu and int(item ['U'])<=maxU:

#         Foundu.append(item)

# print (Foundu)