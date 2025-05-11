import xml.etree.ElementTree as ET
import os

directory = "SU/"
file = open("report.txt", 'w')
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
            #obj_list[num].append([])
            obj_list[num].append(root[i].attrib)
            #obj_list[num][1].append(os.path.join(path, files[SUobject]))
            num += 1
        #print(list)
        #print(list[0][1].get("type"))
        temp_file.close()

#print(obj_list[0])
nat = []
num=0
for i in obj_list:
    nat.append([])
    nat[num].append(i[0])
    nat[num].append(i[1].get("type"))
    num+=1
print(nat[0])
nat_unique=[]
for i in nat:
    if not i in nat_unique:
        nat_unique.append(i)
print(nat_unique)
names = []
for i in nat_unique:
    if not i[0] in names:
        names.append(i[0])
#print(names)


for i in names:
    type_l = []
    temp_num=0
    for j in nat_unique:
        if i==j[0]:
            temp_num+=1
            type_l.append(j[1])
    if temp_num!=1:
        file.write(f'{i} - {temp_num} times; {type_l} \n')
file.close()
nnat_unique=[]
for i in nat_unique:
    if i[0]!="Extra":
        nnat_unique.append([f"{i[1]}_{i[0]}", i[1]])
print(nnat_unique)