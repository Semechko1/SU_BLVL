from imp.set_xml import box_create, open_xml

bl_info = {
    'name': 'Blender Unleashed Lvl',
    'author': 'Semka/Renas',
    'version': (0, 0, 1),
    'blender': (2, 83, 20),
    'location': 'File > Import ',
    'description': 'Import-Create-Export Sonic Unleashed stages!',
    #"wiki_url": "https://github.com/matyalatte/Blender-DDS-Addon",
    'support': 'COMMUNITY',
    'category': 'Import-Export',
}

modules = [
    open_xml,
    box_create
]


def register():
    """Add addon."""
    for module in modules:
        module.register()


def unregister():
    """Remove addon."""
    for module in modules:
        module.unregister()
