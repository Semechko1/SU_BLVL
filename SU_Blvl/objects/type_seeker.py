import xml.etree.ElementTree as ET
import os

directory = "SU/"
file = open("types.txt", 'w')
obj_list = []
num=int(0)
for path, folders, files in os.walk(directory):
    for SUobject in range(len(files)):
        #print(os.path.join(path, files[object]))
        temp_file = open(os.path.join(path, files[SUobject]))
        tree = ET.parse(temp_file)
        root = tree.getroot()
        #print(root.tag)
        #print()
        for i in range(len(root)):
            obj_list.append([])
            #print(list)
            #print(f'{root[i].tag} - {root[i].attrib}')
            #mystr=f'{root[i].tag} - {root[i].attrib}'
            obj_list[num].append(root[i].tag)
            obj_list[num].append([])
            obj_list[num][1].append(root[i].attrib)
            obj_list[num][1].append(os.path.join(path, files[SUobject]))
            num += 1
        #print(list)
        #print(list[0][1].get("type"))
        temp_file.close()

#print(obj_list)


temp_type_list = []
temp_type_and_location_list = []
for i in range(len(obj_list)):
    #print(obj_list[i])
    if not obj_list[i][0]=="Extra":
        temp_type_list.append(obj_list[i][1][0].get("type"))
for i in range(len(obj_list)):
    #print(obj_list[i])
    if not obj_list[i][0]=="Extra":
        temp_type_and_location_list.append([obj_list[i][1][0].get("type"), obj_list[i][1][1]])
print(temp_type_list[0])
print(temp_type_and_location_list[0])
print()
type_list=[]
for i in range(len(temp_type_list)):
    if temp_type_list[i] not in type_list:
        #print(f"{temp_type_list[i]} isn't in the list")
        type_list.append(temp_type_list[i])
        type_list.append(temp_type_and_location_list[i][1])
        type_list.append('')
    else:
        pass
for x in type_list:file.write(f'{x}\n')
file.close()

