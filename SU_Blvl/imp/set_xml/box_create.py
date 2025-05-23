import bpy
import bmesh
from bpy_extras.object_utils import AddObjectHelper

from bpy.props import (
    FloatProperty, StringProperty
)


def add_box(width, height, depth, x, y, z):
    """
    This function takes inputs and returns vertex and face arrays.
    no actual mesh data creation is done here.
    """

    verts = [
        (+1.0, +1.0, -1.0),
        (+1.0, -1.0, -1.0),
        (-1.0, -1.0, -1.0),
        (-1.0, +1.0, -1.0),
        (+1.0, +1.0, +1.0),
        (+1.0, -1.0, +1.0),
        (-1.0, -1.0, +1.0),
        (-1.0, +1.0, +1.0),
    ]

    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (4, 0, 3, 7),
    ]

    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0]+x * width, v[1]+y * depth, v[2]+z * height

    return verts, faces


class AddBox(bpy.types.Operator, AddObjectHelper):
    """Add a simple box mesh"""
    bl_idname = "mesh.primitive_box_add"
    bl_label = "Add Box"
    bl_description = 'Adds a box that currently replaces an empty'
    bl_options = {'REGISTER', 'UNDO'}

    x: FloatProperty(
        name="X Coordinate",
        description="x position",
        min=-1000.0, max=1000.0,
        default=0,
    )
    y: FloatProperty(
        name="Y Coordinate",
        description="y position",
        min=-1000.0, max=1000.0,
        default=0,
    )
    z: FloatProperty(
        name="Z Coordinate",
        description="x position",
        min=-1000.0, max=1000.0,
        default=0,
    )
    name: StringProperty(
        name="Object Name",
        description="Object Name",
        default="Box",
    )

    width: FloatProperty(
        name="Width",
        description="Box Width",
        min=0.01, max=100.0,
        default=0.2,
    )
    height: FloatProperty(
        name="Height",
        description="Box Height",
        min=0.01, max=100.0,
        default=0.2,
    )
    depth: FloatProperty(
        name="Depth",
        description="Box Depth",
        min=0.01, max=100.0,
        default=0.2,
    )

#, name, move_x, move_y, move_z
    def execute(self, context):

        verts_loc, faces = add_box(
            self.width,
            self.height,
            self.depth,
            self.x,
            self.y,
            self.z
        )

        mesh = bpy.data.meshes.new(self.name)

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

# def menu_func(self, context):
#    self.layout.operator(AddBox.bl_idname, icon='MESH_CUBE')


# Register and add to the "add mesh" menu (required to use F3 search "Add Box" for quick access).
def register():
   bpy.utils.register_class(AddBox)
#    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
   bpy.utils.unregister_class(AddBox)
#    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
