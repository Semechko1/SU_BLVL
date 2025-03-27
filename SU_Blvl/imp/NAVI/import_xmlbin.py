import bpy
from .spawn_xmlbin import AddBox


# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy_extras.object_utils import AddObjectHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ImportXMLBIN(Operator, ImportHelper, AddObjectHelper):
    """Imports .NAVI.xmlbin as a 3D object"""
    bl_idname = "import_scene.navixmlbin"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import xmlbin"
    bl_options = {'UNDO'}

    # ImportHelper mix-in class uses this.
    filename_ext = ".xmlbin"

    filter_glob: StringProperty(
        default="*.xmlbin",
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
        description="Import xmlbin mesh with Blender's default orientation",
        items=(
            ('OPT_A', "No", "Import in original coordinates"),
            ('OPT_B', "Yes", "Import in Blender's coordinates"),
        ),
        default='OPT_B',
    )

    def execute(self, context):
        return AddBox.my_func(self, context, self.filepath, self.opt_cord)


# Only needed if you want to add into a dynamic menu.
def menu_func_import(self, context):
    self.layout.operator(ImportXMLBIN.bl_idname, text="Import .NAVI.xmlbin")


# Register and add to the "file selector" menu (required to use F3 search "Text Import Operator" for quick access).
def register():
    bpy.utils.register_class(ImportXMLBIN)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.utils.unregister_class(ImportXMLBIN)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.import_test.some_data('INVOKE_DEFAULT')
