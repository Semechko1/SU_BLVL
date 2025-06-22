import bpy
import xml.etree.ElementTree as ET
from ...objects.get_properties_for_obj import gmop
import os

def write_stg(context, filepath, option):
    for obj in bpy.data.objects:
        if obj.select_get() == True:
            obj.select_set(False)
    if option == "BC":
        bpy.data.objects['BLVL.Stage_Orientation'].select_set(True)
        bpy.ops.object.rotation_clear()

    Set_collection = bpy.context.collection
    for set_piece in list(Set_collection.children):
        root = ET.Element("SetObject")
        for object in list(set_piece.objects):
            if object.parent == bpy.data.objects["BLVL.Stage_Orientation"]:
                xml_se_object = ET.SubElement(root, object.data.name)
                Position = ET.SubElement(xml_se_object, "Position")
                Object_Location = object.matrix_world.decompose()[0]
                ET.SubElement(Position, 'x').text = str(Object_Location.x)
                ET.SubElement(Position, 'y').text = str(Object_Location.y)
                ET.SubElement(Position, 'z').text = str(Object_Location.z)
                Rotation = ET.SubElement(xml_se_object, "Rotation")
                if object.rotation_mode != "QUATERNION":
                    object.rotation_mode = "QUATERNION"
                Object_Rotation = object.matrix_world.decompose()[1]
                ET.SubElement(Rotation, 'w').text = str(Object_Rotation.w)
                ET.SubElement(Rotation, 'x').text = str(Object_Rotation.x)
                ET.SubElement(Rotation, 'y').text = str(Object_Rotation.y)
                ET.SubElement(Rotation, 'z').text = str(Object_Rotation.z)
                ET.SubElement(xml_se_object, "SetObjectID").text = str(object.name).split(".")[1]

                cur_props_list = gmop(object)
                prop_dictionary={"val_of_cur_prop":None, "object":object}
                for cur_prop in cur_props_list:
                    if cur_prop[1][2]!="Extra":
                        exec(f"val_of_cur_prop = object.{cur_prop[0]}", globals(), prop_dictionary)
                        if cur_prop[1][0].get("type")=="bool":
                            prop_txt = str(prop_dictionary["val_of_cur_prop"]).lower()
                        else:
                            prop_txt = str(prop_dictionary["val_of_cur_prop"])
                        ET.SubElement(xml_se_object, cur_prop[1][2]).text = prop_txt
                if len(object.children) != 0:
                    MultiSetParam = ET.SubElement(xml_se_object, "MultiSetParam")
                    for i in range(len(object.children)):
                        Element = ET.SubElement(MultiSetParam, "Element")
                        ET.SubElement(Element, "Index").text = str(i+1)
                        El_Position = ET.SubElement(Element, "Position")
                        Element_Location = list(object.children)[i].matrix_world.decompose()[0]
                        ET.SubElement(El_Position, 'x').text = str(Element_Location.x)
                        ET.SubElement(El_Position, 'y').text = str(Element_Location.y)
                        ET.SubElement(El_Position, 'z').text = str(Element_Location.z)
                        El_Rotation = ET.SubElement(Element, "Rotation")
                        if list(object.children)[i].rotation_mode != "QUATERNION":
                            list(object.children)[i].rotation_mode = "QUATERNION"
                        Element_Rotation = list(object.children)[i].matrix_world.decompose()[1]
                        ET.SubElement(El_Rotation, 'w').text = str(Element_Rotation.w)
                        ET.SubElement(El_Rotation, 'x').text = str(Element_Rotation.x)
                        ET.SubElement(El_Rotation, 'y').text = str(Element_Rotation.y)
                        ET.SubElement(El_Rotation, 'z').text = str(Element_Rotation.z)
        tree = ET.ElementTree(root)
        ET.indent(tree)
        tree.write(os.path.join(os.path.dirname(os.path.abspath(filepath)), str(set_piece.name)+".set.xml"))
        print(os.path.join(os.path.dirname(os.path.abspath(filepath)), str(set_piece.name)+".set.xml"))
    return {'FINISHED'}

# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportStgSet(Operator, ExportHelper):
    """Exports Selected Collection as a group of set files"""
    bl_idname = "export_scene.stg"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export stage set"

    # ExportHelper mix-in class uses this.
    filename_ext = ".xml"

    filter_glob: StringProperty(
        default="*.xml",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    '''
    use_setting: BoolProperty(
        name="Use 0 instead of -1",
        description="Currently AdjFaceIndex -1 values don't work, so this check switches all of -1 to 0",
        default=False,
    )
    '''
    opt_cord: EnumProperty(
        name="Correct orientation",
        description="Choose 'Yes' if you were importing in the Blender's orientation",
        items=(
            ('OC', "No", "Do not re-orient 'BLVL.Stage_Orientation' Empty, keep it as is"),
            ('BC', "Yes", "Reset 'BLVL.Stage_Orientation' Empty to zero values "),
        ),
        default='BC',
    )

    def execute(self, context):
        return write_stg(context, self.filepath, self.opt_cord)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportStgSet.bl_idname, text="Export stage set")