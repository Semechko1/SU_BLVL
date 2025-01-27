import bpy
from .imp.set_xml import box_create, open_xml
from .imp.NAVI.import_xmlbin import ImportXMLBIN
from .imp.NAVI.import_NAVIxml import ImportNAVI_XML

bl_info = {
    'name': 'Blender Unleashed Lvl',
    'author': 'Semka/Renas',
    'version': (0, 0, 1),
    'blender': (2, 83, 20),
    'location': 'File > Import ',
    'description': 'Import-Create-Export Sonic Unleashed stages!',
    "wiki_url": "https://github.com/Semechko1/SU_BLVL",
    'support': 'COMMUNITY',
    'category': 'Import-Export',
}


class TOPBAR_MT_SU_BLVL_import(bpy.types.Menu):
    '''The export submenu in the export menu'''

    bl_label = "SU Formats"

    def draw(self, context):
        layout = self.layout
        layout.label(text="NAVI imports...")
        layout.operator("import_scene.navixml")
        layout.operator("import_scene.navixmlbin")
        layout.separator()


def menu_func_exportsu(self, context):
    self.layout.menu("TOPBAR_MT_SU_BLVL_import")


classes = [
    TOPBAR_MT_SU_BLVL_import,
    ImportXMLBIN,
    ImportNAVI_XML
]


def register():
    """Add addon."""
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_file_import.append(menu_func_exportsu)


def unregister():
    """Remove addon."""
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_exportsu)
