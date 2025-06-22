import os
import xml.etree.ElementTree as ET
import bpy
import mathutils

from ..small_scripts import add_driver, add_my_modifier, link_modifier, change_orient
from .get_properties_for_obj import gmop
import math  # needed in vector "exec" function

def read_params(sef, obj_root, my_object, current_collection, og_location):
    obj_list = gmop(my_object)
    for my_prop in obj_root:
        for db_prop in obj_list:
            if db_prop[1][2] != "Extra":
                #print(my_prop.tag, db_prop[1][2])
                if my_prop.tag == db_prop[1][2]:
                    if db_prop[1][0].get("type") == "float":
                        exec(f'my_object.{db_prop[0]}=float(my_prop.text)')
                        link_modifier(sef, my_object, my_prop.tag, db_prop[0], False)
                    if (db_prop[1][0].get("type") == "integer" or
                            db_prop[1][0].get("type") == "uint32" or
                            db_prop[1][0].get("type") == "uint16"):
                        exec(f'my_object.{db_prop[0]}=int(my_prop.text)')
                        link_modifier(sef, my_object, my_prop.tag, db_prop[0], False)
                    if db_prop[1][0].get("type") == "bool":
                        # print(my_prop.text)
                        exec(f'my_object.{db_prop[0]}=bool(str.capitalize(my_prop.text))')
                        link_modifier(sef, my_object, my_prop.tag, db_prop[0], False)
                    if db_prop[1][0].get("type") == "string":
                        exec(f'my_object.{db_prop[0]}=str(my_prop.text)')
                    if (db_prop[1][0].get("type") == "id" or
                            db_prop[1][0].get("type") == "target"):
                        for lvl_object in bpy.data.objects:
                            if str(lvl_object.name).split(".")[1] == my_prop[0].text:
                                #print(f'{lvl_object.name} is referenced by {my_object.name}')
                                exec(f'my_object.{db_prop[0]}=lvl_object')
                    if db_prop[1][0].get("type") == "vector":
                        wr, xr, yr, zr = 1.0, 0.0, 0.0, 0.0
                        for axis in my_prop:
                            if axis.tag == "w":
                                wr = float(axis.text)
                            if axis.tag == "x":
                                xr = float(axis.text)
                            if axis.tag == "y":
                                yr = float(axis.text)
                            if axis.tag == "z":
                                zr = float(axis.text)
                        exec(f"my_object.{db_prop[0]}=mathutils.Quaternion((wr, xr, yr, zr)).to_euler('XYZ')")
                    if db_prop[1][0].get("type") == "id_list":
                        prop_coll = bpy.data.collections.new(str(my_object.name).split(".")[1] + "." + my_prop.tag)
                        prop_coll.color_tag = "COLOR_08"
                        exec(f"my_object.{db_prop[0]}=prop_coll")
                        for child_tag in my_prop:
                            for lvl_object in bpy.data.objects:
                                if child_tag.text == str(lvl_object.name).split(".")[1]:
                                    prop_coll.objects.link(lvl_object)
                if my_prop.tag == "MultiSetParam":
                    #print(f"#BLVL {my_prop.keys()} | {my_prop.items()}")
                    for E in range(len(my_prop)):
                        if str(my_prop[E].tag) == "Element":
                            # print(f"#BLVL - obj {my_object.name} has {Element.tag}")
                            if "Element" not in bpy.data.meshes.keys():
                                me = bpy.data.meshes.new("Element")
                            else:
                                me = bpy.data.meshes.get("Element")
                            xp, yp, zp = 0, 0, 0
                            xr, yr, zr, wr = 0, 0, 0, 1
                            Index = ""
                            for i in my_prop[E]:
                                if i.tag == "Index":
                                    Index = i.text
                                if i.tag == "Position":
                                    for pos_id in i:
                                        xp = (float(pos_id.text) if (pos_id.tag == "x") else xp)#
                                        yp = (float(pos_id.text) if (pos_id.tag == "y") else yp)#
                                        zp = (float(pos_id.text) if (pos_id.tag == "z") else zp)#
                            for i in my_prop[E]:
                                if i.tag == "Rotation":
                                    for pos_id in i:
                                        wr = (float(pos_id.text) if (pos_id.tag == "w") else wr)
                                        xr = (float(pos_id.text) if (pos_id.tag == "x") else xr)
                                        yr = (float(pos_id.text) if (pos_id.tag == "y") else yr)
                                        zr = (float(pos_id.text) if (pos_id.tag == "z") else zr)
                            an_Element = bpy.data.objects.new(
                                str(my_object.name).split(".")[1] + ".Element." + str(Index), me)
                            xp -= og_location.x
                            yp -= og_location.y
                            zp -= og_location.z
                            an_Element.location.xyz = (xp, yp, zp)
                            an_Element.rotation_mode = 'QUATERNION'
                            an_Element.rotation_quaternion = mathutils.Quaternion((wr, xr, yr, zr))
                            add_my_modifier(an_Element, my_prop[E].tag)
                            link_modifier(sef=sef, curr_object=an_Element, curr_ob_property=my_object, curr_db_property="not needed", EL_toggle=True)
                            current_collection.objects.link(an_Element)
                            an_Element.parent = my_object
