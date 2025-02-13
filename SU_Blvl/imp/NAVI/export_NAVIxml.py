import bpy
import bmesh
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring


def write_some_data(context, filepath, use_some_setting):
    # bmesh initialization I suppose
    nobj = [obj for obj in bpy.context.selected_objects]

    ob = nobj[0]

    if ob.type != 'MESH':
        raise TypeError("Active object is not a Mesh")

    # Get editmode changes
    ob.update_from_editmode()

    me = ob.data

    if len(me.polygons) < 1:
        raise ValueError("Mesh has no faces")
    bm = bmesh.new()
    bm.from_mesh(nobj[0].data)
    bm.faces.ensure_lookup_table()

    filename = filepath

    #header = '<?xml version="1.0" encoding="utf-8" standalone="no" ?>'

    # Creating the XML
    root = ET.Element("Parent")

    # DataSize
    data_size = ET.SubElement(root, "DataSize")
    VertsNum = ET.SubElement(data_size, "VertsNum")
    VertsNum.text = str(len(bm.verts))
    FacesNum = ET.SubElement(data_size, "FacesNum")
    FacesNum.text = str(len(bm.faces))

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
        edge_list = list(i.edges)
        edge_list.reverse()
        edge1 = edge_list[0].calc_length()
        edge2 = edge_list[1].calc_length()
        edge3 = edge_list[2].calc_length()
        temp_lis = [edge1, edge2, edge3]
        for j in range(len(edge_list)):
            face_list = [f.index for f in edge_list[j].link_faces]
            if len(face_list) == 1:
                edge_list[-1], edge_list[j], temp_lis[-1], temp_lis[j] = edge_list[j], edge_list[-1], temp_lis[j], temp_lis[-1]
                break
        for j in range(len(edge_list)-1):
            for k in range(0, len(edge_list)-j-2):
                if temp_lis[k] < temp_lis[k+1]:
                    temp_lis[k], temp_lis[k+1], edge_list[k], edge_list[k+1] = temp_lis[k+1], temp_lis[k], edge_list[k+1], edge_list[k]

        print(f'{edge_list[0].index} - {temp_lis[0]}; {edge_list[1].index} - {temp_lis[1]}; {edge_list[2].index} - {temp_lis[2]}')
        for j in edge_list:
            face = ET.SubElement(tag_adjacent_face_index, "AdjFaceIndex")
            temp_lis = [f.index for f in j.link_faces]
            if len(temp_lis) == 1:
                if use_some_setting == True:
                    face.text = "0"
                if use_some_setting == False:
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
    tree = ET.ElementTree(root)
    ET.indent(tree)
    tree.write(filename, encoding='utf-8',xml_declaration=True)
    #xmlstr = tostring(root).decode()


    #outp = open(filename, "w", encoding="utf-8")
    #outp.write(header + xmlstr)
    #outp.close()
    return {'FINISHED'}


# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportNAVI_XML(Operator, ExportHelper):
    """Exports FIRST selected object (MESH) as a .NAVI.XML"""
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
    '''
    use_setting: BoolProperty(
        name="Use 0 instead of -1",
        description="Currently AdjFaceIndex -1 values don't work, so this check switches all of -1 to 0",
        default=False,
    )
    '''
    '''
    type: EnumProperty(
        name="Example Enum",
        description="Choose between two items",
        items=(
            ('OPT_A', "First Option", "Description one"),
            ('OPT_B', "Second Option", "Description two"),
        ),
        default='OPT_A',
    )
    '''

    def execute(self, context):
        return write_some_data(context, self.filepath, False)


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
