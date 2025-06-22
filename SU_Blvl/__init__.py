import bpy
from .imp.set_xml.Import_stg_set import ImportSetXml
from .imp.NAVI.import_xmlbin import ImportXMLBIN
from .imp.NAVI.import_NAVIxml import ImportNAVI_XML
from .imp.NAVI.export_NAVIxml import ExportNAVI_XML
from .imp.set_xml.Export_stg_set import ExportStgSet
from .objects.side_panel import VIEW3D_PT_BLVL_IE, VIEW3D_PT_BLVL_TOOLS, VIEW3D_PT_BLVL_objprop, VIEW3D_PT_BLVL_objidlistprop
from .objects.object_properties import MyObjectPG, obj_properties
from .small_scripts import UpdateObjectModifiers, AssignObj2Stage

bl_info = {
    'name': 'BLVL',
    'author': 'Semka/Renas',
    'version': (0, 2, 0),
    'blender': (3, 6, 0),
    'location': 'File > Import ',
    'description': 'Import-Create-Export Hedgehog Engine 1 stages!',
    "wiki_url": "https://github.com/Semechko1/SU_BLVL",
    'support': 'COMMUNITY',
    'category': 'Import-Export',
}


class TOPBAR_MT_SU_BLVL_import(bpy.types.Menu):
    """The import submenu in the import menu"""

    bl_label = "SU Formats"
    bl_idname = "import_menu"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Set XML imports...")
        layout.operator("import_scene.stg")
        layout.separator()
        layout.label(text="NAVI imports...")
        # layout.separator()
        layout.operator("import_scene.navixml")
        layout.operator("import_scene.navixmlbin")
        # layout.separator()


def menu_func_importsu(self, context):
    self.layout.menu(TOPBAR_MT_SU_BLVL_import.bl_idname)


class TOPBAR_MT_SU_BLVL_export(bpy.types.Menu):
    """The export submenu in the export menu"""

    bl_label = "SU Formats"
    bl_idname = "export_menu"

    def draw(self, context):
        layout = self.layo
        layout.label(text="Stage Exports")
        layout.separator()
        layout.operator("export_scene.stg")
        layout.label(text="NAVI exports")
        layout.separator()
        layout.operator("export_scene.navixml")
        # layout.operator("export_scene.navixmlbin")


def menu_func_exportsu(self, context):
    self.layout.menu(TOPBAR_MT_SU_BLVL_export.bl_idname)


classes = [
    TOPBAR_MT_SU_BLVL_export,
    ExportNAVI_XML,
    ExportStgSet,

    TOPBAR_MT_SU_BLVL_import,
    ImportXMLBIN,
    ImportNAVI_XML,
    ImportSetXml,

    VIEW3D_PT_BLVL_IE,

    VIEW3D_PT_BLVL_TOOLS,
    VIEW3D_PT_BLVL_objprop,
    VIEW3D_PT_BLVL_objidlistprop,
    MyObjectPG,
    UpdateObjectModifiers,
    AssignObj2Stage
]


def register():
    """Add addon."""
    #    '''
    #    addons = bpy.context.preferences.addons.keys()
    #    if 'bl_ext.sonic_io.hedgehog_engine_io_dev' in addons:
    #        raise Exception("Disable [Hedgehog Engine I/O]\nSU_BLVL is NOT registered!")
    #    elif 'bl_ext.sonic_io.hedgehog_engine_io' in addons:
    #        raise Exception("Disable [Hedgehog Engine I/O]\nSU_BLVL is NOT registered!")
    #    '''

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
