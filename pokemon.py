import json

effects = json.load(open('effectiveness.json'))


new_effects = {}
multiplier = {"super effective":2, "normal effective":1, "not very effective":0.5, "no effect":0}
temp = {}

for key1,key2 in effects.items():
    for key3, value in key2.items():
        new_effects[key3] = new_effects.get(key3,{})
        if len(value)!=0:
            for i in value:
                temp[i] = temp.get(i,multiplier[key1])
            new_effects[key3].update(temp)
            temp = { }
print(new_effects)
print(new_effects["Poison"]["Steel"])
with open('effectiveness_new.json',"w") as new_file:
    new = json.dumps(new_effects, indent= 4)
    new_file.write(new)

# for key1,key2 in effects.items():
#     for key3,value in key2.items():
#         if key1 == "super effective":
#             if len(value)!=0:
#                 for i in value:
#                     temp[i] = temp.get(i,2)
#             new_effects[key3] = new_effects.get(key3,temp)
#             temp = { }
#         if key1 == "normal effective":
#             if len(value)!=0:
#                 for i in value:
#                     temp[i] = temp.get(i,1)
#             new_effects[key3].update(temp)
#             temp = { }
#         if key1 == 'not very effective':
#             if len(value)!=0:
#                 for i in value:
#                     temp[i] = temp.get(i,0.5)
#             new_effects[key3].update(temp)
#             temp = { }
#         if key1 == 'no effect':
#             if len(value)!=0:
#                 for i in value:
#                     temp[i] = temp.get(i,0)
#             new_effects[key3].update(temp)
#             temp = { }
# print(new_effects)

# print(new_effects["Fighting"]['Ghost'])

