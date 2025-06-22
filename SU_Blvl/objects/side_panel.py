import bpy
import os
import xml.etree.ElementTree as ET


def reading_db(my_object):
    obj_list = []
    num = 0
    db_directory = os.path.join(os.path.dirname(__file__), 'SU/')
    # print(os.path.abspath(db_directory), db_directory, os.path.realpath(__file__))
    # print(os.path.join(os.path.dirname(__file__), "SU/"))
    # print()
    for path, folders, files in os.walk(db_directory):
        for file in range(len(files)):
            # print(path, files[file], my_object.data.name+".xml")
            try:
                if my_object.data.name + ".xml" == files[file]:
                    tree = ET.parse(os.path.join(path, files[file]))
                    # print(path, files[file])
                    root = tree.getroot()
                    for i in range(len(root)):
                        obj_list.append([])
                        obj_list[num].append(root[i].tag)
                        obj_list[num].append([])
                        obj_list[num][1].append(root[i].attrib)
                        obj_list[num][1].append(os.path.join(path, files[file]))
                        num += 1
            except AttributeError:
                break
    for i in range(len(obj_list)):
        temp_name = ""
        original_name = ""
        for j in obj_list[i][0]:
            if j == "-":
                temp_name = temp_name + ""
            if j == ".":
                # print(j, obj_list[i][0])
                temp_name = temp_name + ""
            if j == "_":
                temp_name = temp_name + ""
            if j != "-" and j != "_" and j != ".":
                temp_name = temp_name + j
            original_name = original_name + j
        obj_list[i][0] = temp_name
        obj_list[i][1].append(original_name)
    for i in obj_list:
        i[0] = f'{i[1][0].get("type")}_{i[0]}'
    return obj_list

class VIEW3D_PT_BLVL_IE(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BLVL I/E'
    bl_label = 'Import/Export'

    def draw(self, context):
        layout = self.layout
        layout.label(text="NAVI options")
        layout.operator("import_scene.navixml")
        layout.operator("import_scene.navixmlbin")
        layout.separator()
        layout.operator("export_scene.navixml")
        layout.label(text="Stage Set options")
        layout.operator("import_scene.stg")
        layout.operator("export_scene.stg")


class VIEW3D_PT_BLVL_TOOLS(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BLVL'
    bl_label = 'Tool Shortcuts'

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.label(text="Reassign Object Modifiers")
        col.operator("blvl.updatemodifiers")
        col.label(text="Include selected objects into Stage Set")
        col.operator("blvl.assignobj")

        col.separator()
        col.label(text="Stage Orientation")
        try:
            col.prop(bpy.data.objects['BLVL.Stage_Orientation'], "rotation_euler")
        except KeyError:
            #print("No 'BLVL.Stage_Orientation' Empty in the file!")
            pass



class VIEW3D_PT_BLVL_objprop(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BLVL'
    bl_label = 'Object Properties'

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        obj_props = reading_db(context.object)
        for obj_prop in obj_props:
            if (obj_prop[1][0].get("type") == "float"
                    or obj_prop[1][0].get("type") == "integer"
                    or obj_prop[1][0].get("type") == "bool"
                    or obj_prop[1][0].get("type") == "uint16"
                    or obj_prop[1][0].get("type") == "uint32"
                    or obj_prop[1][0].get("type") == "vector"
                    or obj_prop[1][0].get("type") == "string"
                    or obj_prop[1][0].get("type") == "id"
                    or obj_prop[1][0].get("type") == "target"
                    or obj_prop[1][0].get("type") == "id_list"):
                col.prop(context.object, obj_prop[0])

def get_my_type(an_index):
    if an_index<20 and an_index>=0:
        if an_index==0:
            return "0:No event"
        elif an_index==1:
            return "1:Open"
        elif an_index==2:
            return "2:Close"
        elif an_index==3:
            return "3:Kill"
        elif an_index==4:
            return "4:Generate"
        elif an_index==5:
            return "5:Get_off"
        elif an_index==6:
            return "6:On"
        elif an_index==7:
            return "7:Off"
        elif an_index==8:
            return "8:Attack"
        elif an_index==9:
            return "9:Attack_ready"
        elif an_index==10:
            return "10:Can't_Attack"
        elif an_index==11:
            return "11:Return"
        elif an_index==12:
            return "12:Destroy"
        elif an_index==13:
            return "13:Start_Moving"
        elif an_index==14:
            return "14:Reset"
        elif an_index==15:
            return "15:Rise"
        elif an_index==16:
            return "16:Descent"
        elif an_index==17:
            return "17:Start"
        elif an_index==18:
            return "18:Invert"
        elif an_index==19:
            return "19:Clear"
    else:
        return f"Unknown {an_index}"

class VIEW3D_PT_BLVL_objidlistprop(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BLVL'
    bl_label = 'Collection lists'

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        obj_props = reading_db(context.object)
        mydict = {"Event0type": "", "Event1type": "", "Event2type": "",
                  "Event3type": ""}  # used as a link between this code and exec() parts
        mydict["current_object"] = context.object
        # try:
        #     mydict["cur_index"] = str(context.object.name).split(".")[1]
        # except IndexError:
        #     mydict["cur_index"] = str(context.object.name)
        # except AttributeError:
        #     mydict['cur_index'] = "whatever"
        mydict["current_list"] = []
        mydict["layout"] = layout
        for obj_prop in obj_props:
            if obj_prop[0]=="integer_Event0":
                exec(f'Event0type = current_object.{obj_prop[0]}', globals(), mydict)
                mydict["Event0type"]=get_my_type(mydict["Event0type"])
            if obj_prop[0]=="integer_Event1":
                exec(f'Event1type = current_object.{obj_prop[0]}', globals(), mydict)
                mydict["Event1type"]=get_my_type(mydict["Event1type"])
            if obj_prop[0]=="integer_Event2":
                exec(f'Event2type = current_object.{obj_prop[0]}', globals(), mydict)
                mydict["Event2type"]=get_my_type(mydict["Event2type"])
            if obj_prop[0]=="integer_Event3":
                exec(f'Event3type = current_object.{obj_prop[0]}', globals(), mydict)
                mydict["Event3type"]=get_my_type(mydict["Event3type"])
            if obj_prop[1][0].get("type") == "id_list":
                if obj_prop[0]=="id_list_TargetList0":
                    exec(f"layout.label(text=str(current_object.{obj_prop[0]}.name)+'  has action  '+Event0type)", globals(), mydict)
                elif obj_prop[0]=="id_list_TargetList1":
                    exec(f"layout.label(text=str(current_object.{obj_prop[0]}.name)+'  has action  '+Event1type)", globals(), mydict)
                elif obj_prop[0]=="id_list_TargetList2":
                    exec(f"layout.label(text=str(current_object.{obj_prop[0]}.name)+'  has action  '+Event2type)", globals(), mydict)
                elif obj_prop[0]=="id_list_TargetList3":
                    exec(f"layout.label(text=str(current_object.{obj_prop[0]}.name)+'  has action  '+Event3type)", globals(), mydict)
                else:
                    exec(f"layout.label(text=current_object.{obj_prop[0]}.name)", globals(), mydict)
                exec(f"current_list = list(current_object.{obj_prop[0]}.objects)", globals(), mydict) # getting list of objects
                current_list = mydict["current_list"]  # getting list out of exec() function
                for i in current_list:
                    i = "    " + i.name
                    layout.label(text=i)
                layout.separator()
