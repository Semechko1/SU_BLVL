import bpy
import os
import xml.etree.ElementTree as ET

def gmop(my_object):
    prop_list = []
    num = 0
    db_directory = os.path.join(os.path.dirname(__file__), 'SU/')
    for path, folders, files in os.walk(db_directory):
        for file in range(len(files)):
            # print(path, files[file], my_object.data.name+".xml")
            if my_object.data.name + ".xml" == files[file]:
                tree = ET.parse(os.path.join(path, files[file]))
                # print(path, files[file])
                root = tree.getroot()
                for i in range(len(root)):
                    prop_list.append([])
                    prop_list[num].append(root[i].tag)
                    prop_list[num].append([])
                    prop_list[num][1].append(root[i].attrib)
                    prop_list[num][1].append(os.path.join(path, files[file]))
                    num += 1
    for i in range(len(prop_list)):
        #clearing unneeded characters
        temp_name = ""
        original_name = ""
        for j in prop_list[i][0]:
            if j == "-":
                temp_name = temp_name + ""
            if j == ".":
                # print(j, prop_list[i][0])
                temp_name = temp_name + ""
            if j == "_":
                temp_name = temp_name + ""
            if j != "-" and j != "_" and j != ".":
                temp_name = temp_name + j
            original_name = original_name + j
        prop_list[i][0] = temp_name
        prop_list[i][1].append(original_name)

    for i in prop_list:
        #adding type for property in its name to not have any problems later
        i[0] = f'{i[1][0].get("type")}_{i[0]}'
    return prop_list