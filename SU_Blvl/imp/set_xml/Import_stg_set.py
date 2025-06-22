import os.path

from bpy_extras.io_utils import ImportHelper
from SU_Blvl.objects.reading_properties import read_params
from ...small_scripts import get_path_to_addon, add_my_modifier, load_my_library

import math
import mathutils
import xml.etree.ElementTree as ET
import bpy


def read_set_piece(sef, filepath, inner_orientation, my_collection):
    tree = ET.parse(filepath)
    root = tree.getroot()
    #print(root.tag)
    #print(len(root))
    #print()
    objlist=[]
    for i in range(len(root)):
        xp, yp, zp = 0, 0, 0
        wr, xr, yr, zr = 1, 0, 0, 0
        for j in range(len(root[i])):
            # print(root[i][j].tag)
            if root[i][j].tag == "Position":
                for pos_id in root[i][j]:
                    xp = (float(pos_id.text) if (pos_id.tag == "x") else xp)
                    yp = (float(pos_id.text) if (pos_id.tag == "y") else yp)
                    zp = (float(pos_id.text) if (pos_id.tag == "z") else zp)
        for j in range(len(root[i])):
            if root[i][j].tag == "Rotation":
                for pos_id in root[i][j]:
                    wr = (float(pos_id.text) if (pos_id.tag == "w") else wr)
                    xr = (float(pos_id.text) if (pos_id.tag == "x") else xr)
                    yr = (float(pos_id.text) if (pos_id.tag == "y") else yr)
                    zr = (float(pos_id.text) if (pos_id.tag == "z") else zr)

        #Euler = mathutils.Quaternion((xr,yr,zr,wr)).to_euler('XYZ')
        #Euler.rotate(temp_Euler)

        #creating an object from set
        temp_id=""
        for j in root[i]:
            if j.tag == "SetObjectID":
                temp_id = j.text
        if not root[i].tag in bpy.data.meshes.keys():
            me = bpy.data.meshes.new(root[i].tag)
        else:
            me = bpy.data.meshes.get(root[i].tag)
        an_object = bpy.data.objects.new(root[i].tag+"."+temp_id, me)

        #setting location, rotation, modifier of an object
        an_object.rotation_mode = 'QUATERNION'
        an_object.rotation_quaternion = mathutils.Quaternion((wr, xr, yr, zr))
        an_object.location.xyz=(xp, yp, zp)
        add_my_modifier(an_object, root[i].tag)
        og_location = an_object.location.xyz
        an_object.parent = inner_orientation

        #adding object to their collection
        my_collection.objects.link(an_object)

        #adding object and it's data for the further usage
        objlist.append([])
        objlist[i].append(an_object)
        objlist[i].append(root[i])
        objlist[i].append(my_collection)
        objlist[i].append(og_location)
    for i in objlist:
        read_params(sef, i[1], i[0], i[2], i[3])
    return {'FINISHED'}


def import_stg(sef, folderpath, setting):
    Orientation = bpy.data.objects.new("BLVL.Stage_Orientation", None)
    Orientation.use_fake_user = True
    stage_stg=ET.parse(f'{folderpath}')
    root=stage_stg.getroot()
    for i in root:
        if i.tag == "SetData":
            for MyObj in i:
                coll = bpy.data.collections.new('temp')
                for prop in MyObj:
                    if prop.tag=="Name":
                        coll.name=f'{prop.text}'
                    if prop.tag=="Color":
                        if prop.text=="White":
                            coll.color_tag="NONE"
                        elif prop.text=="Red":
                            coll.color_tag="COLOR_01"
                        elif prop.text=="Yellow":
                            coll.color_tag="COLOR_03"
                        elif prop.text=="Green":
                            coll.color_tag="COLOR_04"
                        elif prop.text=="Blue":
                            coll.color_tag="COLOR_05"
                        else:
                            coll.color_tag="COLOR_02"
                    if prop.tag=="FileName":
                        read_set_piece(sef, f'{os.path.dirname(folderpath)}/{prop.text}', Orientation, coll)
                bpy.context.collection.children.link(coll)
                coll=""
    if setting == "BC":
        Orientation.rotation_euler.x = math.radians(90)
        Orientation.rotation_euler.y = math.radians(0)
        Orientation.rotation_euler.z = math.radians(0)
    if setting == "OC":
        Orientation.rotation_euler.x = math.radians(0)
        Orientation.rotation_euler.y = math.radians(0)
        Orientation.rotation_euler.z = math.radians(0)
    return {'FINISHED'}


# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.


class ImportSetXml(bpy.types.Operator, ImportHelper):
    """Import Set of objects from SU stage"""
    bl_idname = "import_scene.stg"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import stage set"
    bl_options = {'UNDO'}

    # ImportHelper mix-in class uses this.
    filename_ext = ".stg.xml"

    filter_glob: bpy.props.StringProperty(
        default="*.stg.xml",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
#    use_setting: BoolProperty(
#        name="Example Boolean",
#        description="Example Tooltip",
#        default=True,
#    )

    opt_cord: bpy.props.EnumProperty(
        name="Import in X-ZY",
        description="Import set of objects with Blender's default orientation",
        items=(
            ('OC', "No", "Import in original coordinates"),
            ('BC', "Yes", "Import in Blender's coordinates"),
        ),
        default='BC',
    )

    def execute(self, context):
        load_my_library(os.path.join(get_path_to_addon(), "set_assets/AssetsLib1.blend"))
        return import_stg(self, self.filepath, self.opt_cord)


# Only needed if you want to add into a dynamic menu.
def menu_func_import(self, context):
    self.layout.operator(ImportSetXml.bl_idname, text="Import stage set")


# Register and add to the "file selector" menu (required to use F3 search "Text Import Operator" for quick access).
def register():
    bpy.utils.register_class(ImportSetXml)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(ImportSetXml)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


#if __name__ == "__main__":
#    register()
#
    # test call
#    bpy.ops.import_test.some_data('INVOKE_DEFAULT')
