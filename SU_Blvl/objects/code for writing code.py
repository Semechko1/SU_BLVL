import xml.etree.ElementTree as ET
import os

directory = "SU/"
file = open("code.txt", 'w')
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

print(obj_list[0])
for i in range(len(obj_list)):
    temp_name = ""
    original_name = ""
    for j in obj_list[i][0]:
        if j == "-":
            temp_name=temp_name+""
        if j == ".":
            #print(j, obj_list[i][0])
            temp_name=temp_name+""
        if j == "_":
            temp_name=temp_name+""
        if j!="-" and j!="_" and j!=".":
            temp_name = temp_name + j
        original_name=original_name+j
    obj_list[i][0] = temp_name
    obj_list[i][1].append(original_name)
for i in obj_list:
    i[0]=f'{i[1][0].get("type")}_{i[0]}'

f_obj_list=dict(obj_list)
#print(f_obj_list)

obj_list=[]
i=0
for key, value in f_obj_list.items():
    obj_list.append([])
    obj_list[i].append(key)
    obj_list[i].append(value)
    i+=1
i=0
print(obj_list[378])
for i in obj_list:
    if i[1][0].get('type')== "float":
        file.write(
            f'bpy.types.Object.{i[0]} = bpy.props.FloatProperty(name="{i[1][2]}", default={float(i[1][0].get("default"))}, ' +
            f'description="{i[1][0].get("description")}") # {i[1][1]}\n')
for i in obj_list:
    if i[1][0].get('type')== "integer":
        file.write(
            f'bpy.types.Object.{i[0]} = bpy.props.IntProperty(name="{i[1][2]}", default={int(i[1][0].get("default"))}, ' +
            f'description="{i[1][0].get("description")}") # {i[1][1]}\n')
for i in obj_list:
    if i[1][0].get('type')== "uint16":
        file.write(
            f'bpy.types.Object.{i[0]} = bpy.props.IntProperty(name="{i[1][2]}", default={int(i[1][0].get("default"))}, ' +
            f'description="{i[1][0].get("description")}", min=0, max=65535) # {i[1][1]}\n')
for i in obj_list:
    if i[1][0].get('type')== "uint32":
        file.write(
            f'bpy.types.Object.{i[0]} = bpy.props.IntProperty(name="{i[1][2]}", default={int(i[1][0].get("default"))}, ' +
            f'description="{i[1][0].get("description")}", min=0) # {i[1][1]}\n')
for i in obj_list:
    if i[1][0].get('type')== "bool":
        file.write(
            f'bpy.types.Object.{i[0]} = bpy.props.BoolProperty(name="{i[1][2]}", default={str.capitalize(i[1][0].get("default"))}, ' +
            f'description="{i[1][0].get("description")}") # {i[1][1]}\n')
for i in obj_list:
    if i[1][0].get('type')== "vector":
        file.write(
            f'bpy.types.Object.{i[0]} = bpy.props.FloatVectorProperty(name="{i[1][2]}", default=(0.0, 0.0, 0.0), ' +
            f'description="{i[1][0].get("description")}") # {i[1][1]}\n')
for i in obj_list:
    if i[1][0].get('type')== "string":
        file.write(
            f'bpy.types.Object.{i[0]} = bpy.props.StringProperty(name="{i[1][2]}", default="{i[1][0].get("default")}", ' +
            f'description="{i[1][0].get("description")}") # {i[1][1]}\n')
for i in obj_list:
    if i[1][0].get('type')== "id_list":
        file.write(
            f'bpy.types.Object.{i[0]} = bpy.props.PointerProperty(type=bpy.types.Collection, name="{i[1][2]}",' +
            f'description="{i[1][0].get("description")}") # {i[1][1]}\n')
for i in obj_list:
    if i[1][0].get('type')== "id":
        file.write(
            f'bpy.types.Object.{i[0]} = bpy.props.PointerProperty(type=bpy.types.Object, name="{i[1][2]}",' +
            f'description="{i[1][0].get("description")}") # {i[1][1]}\n')
for i in obj_list:
    if i[1][0].get('type')== "target":
        file.write(
            f'bpy.types.Object.{i[0]} = bpy.props.PointerProperty(type=bpy.types.Object, name="{i[1][2]}",' +
            f'description="{i[1][0].get("description")}") # {i[1][1]}\n')
file.close()

