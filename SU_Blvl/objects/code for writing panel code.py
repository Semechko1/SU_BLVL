import xml.etree.ElementTree as ET
import os

directory = "SU/"
file = open("panel.txt", 'w')
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
        obj_list.append([])
        obj_list[num].append(files[SUobject].rpartition('.')[0])  # File/ObjectName
        prop_count=0
        obj_list[num].append([])
        for i in range(len(root)):
            if not root[i].tag == "Extra":
                obj_list[num][1].append([])
                obj_list[num][1][prop_count].append(root[i].tag) # Property
                obj_list[num][1][prop_count].append(root[i].attrib) # For property type
                prop_count+=1
        num += 1
        #print(list)
        #print(list[0][1].get("type"))
        temp_file.close()

#print(obj_list)
for i in range(len(obj_list)):
    for j in range(len(obj_list[i][1])):
        temp_name = ""
        for k in obj_list[i][1][j][0]:
            if (k != "-") and (k != "."):
                temp_name=temp_name+k
            if k == "-":
                temp_name=temp_name+"_"
            if k == ".":
                temp_name=temp_name+""
        obj_list[i][1][j][0]=temp_name
for i in obj_list:
    for j in i[1]:
        j[0]=f'{j[1].get("type")}_{j[0]}'

print(obj_list[0])
for i in range(len(obj_list)):
    file.write(f'if context.object.data.name == "{obj_list[i][0]}":\n')
    for prop in obj_list[i][1]:
        # obj_list[i]*[1]**[1]***[1]****
        # *    - Object
        # **   - its list properties
        # ***  - property
        # **** - propertie's attributes
        if (prop[1].get("type") == "integer"
                or prop[1].get("type") == "float"
                or prop[1].get("type") == "bool"
                or prop[1].get("type") == "vector"
                or prop[1].get("type") == "string"
                or prop[1].get("type") == "uint16"
                or prop[1].get("type") == "uint132"
                or prop[1].get("type") == "id_list"
                or prop[1].get("type") == "id"
                or prop[1].get("type") == "target"):
            file.write(f'    col.prop(context.object, "{prop[0]}")\n')
file.close()
