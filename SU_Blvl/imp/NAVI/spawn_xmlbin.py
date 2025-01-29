import bpy
import bmesh
import ntpath
from .read_xmlbin import read_xmlbin
from bpy_extras.object_utils import AddObjectHelper

from bpy.props import (
    FloatProperty,
)

def calc_faces(array):
    temp_arr=[]
    i = 0
    while(len(array)>i):
        temp_arr.append(array[i:i+3])
        i+=3
    return temp_arr


def add_box(self, width, height, depth, path):
    """
    This function takes inputs and returns vertex and face arrays.
    no actual mesh data creation is done here.
    """

    verts = read_xmlbin.read_file(self, path)[3]

    faces = calc_faces(read_xmlbin.read_file(self, path)[4])
    print(faces)

    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height

    return verts, faces


class AddBox(bpy.types.Operator, AddObjectHelper):
    """Add the xmlbin navmesh"""
    bl_idname = "mesh.xmlbin"
    bl_label = "Add xmlblin"
    bl_options = {'REGISTER', 'UNDO'}

    width: FloatProperty(
        name="Width",
        description="Box Width",
        min=0.01, max=100.0,
        default=1.0,
    )
    height: FloatProperty(
        name="Height",
        description="Box Height",
        min=0.01, max=100.0,
        default=1.0,
    )
    depth: FloatProperty(
        name="Depth",
        description="Box Depth",
        min=0.01, max=100.0,
        default=1.0,
    )

    def my_func(self, context, file):

        verts_loc, faces = add_box(
            self,
            1, 1, 1,
            file
        )

        mesh = bpy.data.meshes.new(ntpath.basename(file))

        bm = bmesh.new()

        for v_co in verts_loc:
            bm.verts.new(v_co)

        bm.verts.ensure_lookup_table()
        for f_idx in faces:
            bm.faces.new([bm.verts[i] for i in f_idx])

        bm.to_mesh(mesh)
        mesh.update()

        # add the mesh as an object into the scene with this utility module
        from bpy_extras import object_utils
        object_utils.object_data_add(context, mesh, operator=self)

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(AddBox.bl_idname, icon='MESH_GRID')


# Register and add to the "add mesh" menu (required to use F3 search "Add Box" for quick access).
#def register():
#    bpy.utils.register_class(AddBox)
#    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


#def unregister():
#    bpy.utils.unregister_class(AddBox)
#    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)


if __name__ == "__main__":
    pass
    # register()

    # test call
    #bpy.ops.mesh.primitive_box_add()
