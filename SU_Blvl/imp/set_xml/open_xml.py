import math

import bpy
import mathutils
import xml.etree.ElementTree as ET




def read_some_data(context, filepath, setting):
    tree = ET.parse(filepath)
    root = tree.getroot()
    print(root.tag)
    print(len(root))
    print()
    for i in range(len(root)):
        for j in range(len(root[i])):
            # print(root[i][j].tag)
            if root[i][j].tag == "Position":
                if setting == "OPT_B":
                    xp, yp, zp = (float(root[i][j][1].text),
                                  float(root[i][j][3].text)*-1,
                                  float(root[i][j][2].text))
                else:
                    xp, yp, zp = (float(root[i][j][1].text),
                                  float(root[i][j][2].text),
                                  float(root[i][j][3].text))
                break
            else:
                xp, yp, zp = 0, 0, 0
        for j in range(len(root[i])):
            if root[i][j].tag == "Rotation":
                wr, xr, yr, zr = (float(root[i][j][0].text), float(root[i][j][1].text),
                                  float(root[i][j][2].text), float(root[i][j][3].text))
                break
            else:
                wr, xr, yr, zr = 1, 0, 0, 0

        #Euler = mathutils.Quaternion((xr,yr,zr,wr)).to_euler('XYZ')
        #Euler.rotate(temp_Euler)
        bpy.ops.mesh.primitive_monkey_add(location=(xp,yp,zp))
        the_mesh = bpy.context.object
        the_mesh.rotation_mode = 'QUATERNION'
        if setting == "OPT_B":
            the_mesh.rotation_quaternion = mathutils.Quaternion(
                mathutils.Quaternion((wr, xr, yr, zr)) @
                mathutils.Quaternion((1 / math.sqrt(2), 1 / math.sqrt(2), 0, 0)))
        else:
            the_mesh.rotation_quaternion = mathutils.Quaternion((wr, xr, yr, zr))
        the_mesh.name = root[i].tag


    return {'FINISHED'}


# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ImportSetXml(Operator, ImportHelper):
    """Import Set of objects from SU stage"""
    bl_idname = "import_scene.setxml"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import .set.xml"
    bl_options = {'UNDO'}

    # ImportHelper mix-in class uses this.
    filename_ext = ".xml"

    filter_glob: StringProperty(
        default="*.xml",
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

    opt_cord: EnumProperty(
        name="Import in XZ-Y",
        description="Import set of objects with Blender's default orientation",
        items=(
            ('OPT_A', "No", "Import in original coordinates"),
            ('OPT_B', "Yes", "Import in Blender's coordinates"),
        ),
        default='OPT_B',
    )

    def execute(self, context):
        return read_some_data(context, self.filepath, self.opt_cord)


# Only needed if you want to add into a dynamic menu.
def menu_func_import(self, context):
    self.layout.operator(ImportSetXml.bl_idname, text="Import .set.xml")


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
