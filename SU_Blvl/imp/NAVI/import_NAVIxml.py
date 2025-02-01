import bpy
from .spawn_NAVIxml import AddBox


# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy_extras.object_utils import AddObjectHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ImportNAVI_XML(Operator, ImportHelper, AddObjectHelper):
    """Import .NAVI.XML as a 3D object. Uses only Vertex Data and VertexIndex, other valiues aren't checked"""
    bl_idname = "import_scene.navixml"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import NAVI.XML"

    # ImportHelper mix-in class uses this.
    filename_ext = ".NAVI.XML"

    filter_glob: StringProperty(
        default="*.NAVI.XML",
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

#    type: EnumProperty(
#        name="Example Enum",
#        description="Choose between two items",
#        items=(
#            ('OPT_A', "First Option", "Description one"),
#            ('OPT_B', "Second Option", "Description two"),
#        ),
#        default='OPT_A',
#    )

    def execute(self, context):
        return AddBox.my_func(self, context, self.filepath)


# Only needed if you want to add into a dynamic menu.
def menu_func_import(self, context):
    self.layout.operator(ImportNAVI_XML.bl_idname, text="Import .NAVI.xml")


# Register and add to the "file selector" menu (required to use F3 search "Text Import Operator" for quick access).
def register():
    bpy.utils.register_class(ImportNAVI_XML)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.utils.unregister_class(ImportNAVI_XML)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.import_test.some_data('INVOKE_DEFAULT')
