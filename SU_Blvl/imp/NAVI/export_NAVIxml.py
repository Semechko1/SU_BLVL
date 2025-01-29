import bpy
import bmesh
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring


def write_some_data(context, filepath, use_some_setting):
    # bmesh initialization I suppose
    nobj = [obj for obj in bpy.context.selected_objects]
    bm = bmesh.new()
    bm.from_mesh(nobj[0].data)
    bm.faces.ensure_lookup_table()

    filename = filepath

    header = '<?xml version="1.0" encoding="utf-8" standalone="no" ?>'

    # Creating the XML
    root = ET.Element("Parent")

    # DataSize
    data_size = ET.SubElement(root, "DataSize")
    ET.SubElement(data_size, "VertsNum").text = str(len(bm.verts))
    ET.SubElement(data_size, "FacesNum").text = str(len(bm.faces))

    # TagVertex
    tag_vertex = ET.SubElement(root, "TagVertex")

    def locat(flt):
        round_to = 6
        nflt = format(flt, '.6f')
        num = len(str(nflt).split(".")[1])
        #print(num)
        while num != round_to:
            nflt = str(nflt) + "0"
            num += 1
        #print(nflt)
        return str(nflt)

    n = 0
    for vertex in bm.verts:
        vert = ET.SubElement(tag_vertex, "Vertex")
        ET.SubElement(vert, "x").text = str(locat(vertex.co.x))
        ET.SubElement(vert, "y").text = str(locat(vertex.co.y))
        ET.SubElement(vert, "z").text = str(locat(vertex.co.z))
        n += 1

    # TagVertexIndex
    tag_vertex_index = ET.SubElement(root, "TagVertexIndex")
    for i in bm.faces:
        for j in (i.verts):
            vert = ET.SubElement(tag_vertex_index, "VertexIndex")
            vert.text = str(j.index)

    # TagAdjFaceIndex
    tag_adjacent_face_index = ET.SubElement(root, "TagAdjFaceIndex")

    def find_correct_index(face_id, list):
        for i in list:
            if str(i) != str(face_id):
                return i

    for i in bm.faces:
        for j in i.edges:
            face = ET.SubElement(tag_adjacent_face_index, "AdjFaceIndex")
            temp_lis = [f.index for f in j.link_faces]
            if len(temp_lis) == 1:
                face.text = "-1"
            elif len(temp_lis) > 1:
                face.text = str(find_correct_index(i.index, temp_lis))

    # TagColor
    tag_color = ET.SubElement(root, "TagColor")
    for i in bm.faces:
        col = ET.SubElement(tag_color, "Color")
        col.text = str(1)

    # TagIllum
    tag_illum = ET.SubElement(root, "TagIllum")
    for i in bm.faces:
        ilu = ET.SubElement(tag_illum, "Illum")
        ilu.text = str(0)

    # Writing to the .xml
    xmlstr = tostring(root).decode()

    outp = open(filename, "w", encoding="utf-8")
    outp.write(header + xmlstr)
    outp.close()
    return {'FINISHED'}


# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportNAVI_XML(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_scene.navixml"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export .NAVI.XML"

    # ExportHelper mix-in class uses this.
    filename_ext = ".XML"

    filter_glob: StringProperty(
        default="*.XML",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    use_setting: BoolProperty(
        name="Example Boolean",
        description="Example Tooltip",
        default=True,
    )

    type: EnumProperty(
        name="Example Enum",
        description="Choose between two items",
        items=(
            ('OPT_A', "First Option", "Description one"),
            ('OPT_B', "Second Option", "Description two"),
        ),
        default='OPT_A',
    )

    def execute(self, context):
        return write_some_data(context, self.filepath, self.use_setting)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportNAVI_XML.bl_idname, text="Export .NAVI.XML")


# Register and add to the "file selector" menu (required to use F3 search "Text Export Operator" for quick access).
def register():
    bpy.utils.register_class(ExportNAVI_XML)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportNAVI_XML)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

# if __name__ == "__main__":
#    register()
#
# test call
#    bpy.ops.export_test.some_data('INVOKE_DEFAULT')
