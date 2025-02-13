import bpy
# from .imp.set_xml import box_create, open_xml
from .imp.NAVI.import_xmlbin import ImportXMLBIN
from .imp.NAVI.import_NAVIxml import ImportNAVI_XML
from .imp.NAVI.export_NAVIxml import ExportNAVI_XML
import sys

bl_info = {
    'name': 'Blender Unleashed Lvl',
    'author': 'Semka/Renas',
    'version': (0, 1, 1),
    'blender': (3, 6, 0),
    'location': 'File > Import ',
    'description': 'Import-Create-Export Sonic Unleashed stages!',
    "wiki_url": "https://github.com/Semechko1/SU_BLVL",
    'support': 'COMMUNITY',
    'category': 'Import-Export',
}


class TOPBAR_MT_SU_BLVL_import(bpy.types.Menu):
    '''The import submenu in the import menu'''

    bl_label = "SU Formats"
    bl_idname = "import_menu"

    def draw(self, context):
        layout = self.layout
        layout.label(text="NAVI imports...")
        layout.separator()
        layout.operator("import_scene.navixml")
        layout.operator("import_scene.navixmlbin")
        #layout.separator()
    


def menu_func_importsu(self, context):
    self.layout.menu(TOPBAR_MT_SU_BLVL_import.bl_idname)


class TOPBAR_MT_SU_BLVL_export(bpy.types.Menu):
    '''The export submenu in the export menu'''

    bl_label = "SU Formats"
    bl_idname = "export_menu"

    def draw(self, context):
        layout = self.layout
        layout.label(text="NAVI exports...")
        layout.separator()
        layout.operator("export_scene.navixml")
        # layout.operator("export_scene.navixmlbin")
        #layout.separator()


def menu_func_exportsu(self, context):
    self.layout.menu(TOPBAR_MT_SU_BLVL_export.bl_idname)


classes = [
    TOPBAR_MT_SU_BLVL_export,
    ExportNAVI_XML,

    TOPBAR_MT_SU_BLVL_import,
    ImportXMLBIN,
    ImportNAVI_XML
]


def register():
    """Add addon."""
    '''
    addons = bpy.context.preferences.addons.keys()
    if 'bl_ext.sonic_io.hedgehog_engine_io_dev' in addons:
        raise Exception("Disable [Hedgehog Engine I/O]\nSU_BLVL is NOT registered!")
    elif 'bl_ext.sonic_io.hedgehog_engine_io' in addons:
        raise Exception("Disable [Hedgehog Engine I/O]\nSU_BLVL is NOT registered!")
    '''
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_exportsu)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_importsu)





def unregister():
    """Remove addon."""

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_importsu)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_exportsu)

    for cls in classes:
        bpy.utils.unregister_class(cls)
