import bpy
import xml.etree.ElementTree as ET
from .box_create import AddBox as bc


class do_dat_creat():
    """Class do_dat_creat"""

    bl_idname = "blvl.ddc"
    bl_label = "do_dat_creat"
    bl_description = 'a middle ground between file and data creation'
    bl_options = {'REGISTER', 'UNDO'}

    def rs(huh):
        root = huh.getroot()
        for i in root.iter():
            if (i.find("Position") != -1):
                bc.AddBox.x = i[1].text
                bc.AddBox.y = i[2].text
                bc.AddBox.z = i[3].text
                bc.AddBox.name = i.tag

