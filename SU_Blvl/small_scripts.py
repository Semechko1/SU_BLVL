import bpy
from .objects.get_properties_for_obj import gmop

def load_my_library(directory):
    with bpy.data.libraries.load(directory) as (data_from, data_to):
        data_to.node_groups = data_from.node_groups

def add_driver(
        source, target, source_prop, target_prop,
        multi_source_prop_index = -1, negative = False, func =''
    ):
    ''' Add driver to source prop (at index), driven by target dataPath '''

    if multi_source_prop_index != -1:
        d = source.driver_add(target_prop, multi_source_prop_index).driver
    else:
        d = source.driver_add(target_prop).driver

    v = d.variables.new()
    v.name                 = "variable"
    v.targets[0].id        = target
    v.targets[0].data_path = source_prop

    d.expression = func + "(" + v.name + ")" if func else v.name
    d.expression = d.expression if not negative else "-1 * " + d.expression

import os
def get_path_to_addon():
    return os.path.dirname(__file__)

def add_my_modifier(my_object, name_of_mod):
    try:
        modifier = my_object.modifiers.new("BLVL Visual Node", "NODES")
        modifier.node_group = bpy.data.node_groups[name_of_mod]
    except KeyError:
        pass

def link_modifier(sef, curr_object, curr_ob_property, curr_db_property, EL_toggle: bool):
    # getting modifier inputs
    Modif_socket_list = []
    Group_Inp_list = []

    modifier = curr_object.modifiers["BLVL Visual Node"]
    try:
        current_node_group = modifier.node_group
        my_lis = list(modifier.keys())
        for modif_socket in range(0, len(my_lis), 3):
            # from start till the end of the list with a step of 3 (**Socket_2**, Socket_2_use_attribute, Socket_2_attribute_name)
            Modif_socket_list.append(my_lis[modif_socket])
        for input_socket in range(1, len(list(current_node_group.nodes["Group Input"].outputs.keys())) - 1):
            # 1st one is Geometry, last one is blank socket
            Group_Inp_list.append(list(current_node_group.nodes["Group Input"].outputs.keys())[input_socket])

        for i in range(len(Modif_socket_list)):
            for j in range(len(Group_Inp_list)):
                if i == j:
                    if EL_toggle == False:
                        if Group_Inp_list[j] == curr_ob_property:
                            add_driver(curr_object, curr_object, curr_db_property,
                                       f'modifiers["BLVL Visual Node"]["{Modif_socket_list[i]}"]')
                    elif EL_toggle == True:
                        #print(Modif_socket_list[i], Group_Inp_list[j])
                        if str(Group_Inp_list[j]) == "Object":
                            #print(curr_ob_property)
                            exec(f'curr_object.modifiers["BLVL Visual Node"]["{Modif_socket_list[i]}"] = curr_ob_property')
    except AttributeError:
        #print(f"#BLVL {curr_object.name} doesn't have a modifier -- {modifier.node_group} | {type(modifier.node_group)}")
        #sef.report({'ERROR'}, f"Couldn't find modifier for {curr_object.name}")
        pass

class UpdateObjectModifiers(bpy.types.Operator):
    """Import Set of objects from SU stage"""
    bl_idname = "blvl.updatemodifiers"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Update Object Modifiers"
    bl_options = {'UNDO'}

    def execute (self, context):
        load_my_library(os.path.join(get_path_to_addon(), "set_assets/AssetsLib1.blend"))
        for object in bpy.data.objects:
            if object.type == 'MESH':
                if "BLVL Visual Node" not in object.modifiers.keys():
                    add_my_modifier(object, object.data.name)
                    obj_list = gmop(object)
                    for db_prop in obj_list:
                        if db_prop[1][2]!="Extra":
                            if db_prop[1][0].get("type") == "float":
                                link_modifier(self, object, db_prop[1][2], db_prop[0], False)
                            if (db_prop[1][0].get("type") == "integer" or
                                    db_prop[1][0].get("type") == "uint32" or
                                    db_prop[1][0].get("type") == "uint16"):
                                link_modifier(self, object, db_prop[1][2], db_prop[0], False)
                            if db_prop[1][0].get("type") == "bool":
                                link_modifier(self, object, db_prop[1][2], db_prop[0], False)
        return {'FINISHED'}

def assign_obj_2_stage(sef):
    try:
        for sel_object in bpy.context.selected_objects:
            if sel_object.parent == None:
                sel_object.parent = bpy.data.objects["BLVL.Stage_Orientation"]
                # sel_object.matrix_world = sel_object.matrix_local
            elif sel_object.parent == bpy.data.objects["BLVL.Stage_Orientation"]:
                sef.report({"INFO"}, f"{sel_object.name}  is already a part of stage's set!")
            else:
                sef.report({"WARNING"}, f'{sel_object.name}  has a parent object: {sel_object.parent.name}')
        return {'FINISHED'}
    except KeyError:
        sef.report({"ERROR"}, "File doesn't have 'BLVL.Stage_Orientation' Empty to assign to")
        return {'CANCELLED'}

class AssignObj2Stage(bpy.types.Operator):
    """Assign all selected objects to Empty 'BLVL.Stage_Orientation' """
    bl_idname = "blvl.assignobj"
    bl_label = "Assign Selected Objects"
    bl_options = {'UNDO'}

    def execute (self, context):
        return assign_obj_2_stage(self)

import mathutils, math
def change_orient(an_object, setting):
    if setting == "BC":
        an_object.rotation_quaternion @= mathutils.Quaternion((1 / math.sqrt(2), 1 / math.sqrt(2), 0, 0))
        an_object.location.x, an_object.location.y, an_object.location.z = \
            (an_object.location.x, an_object.location.z * -1, an_object.location.y)
    else:
        pass