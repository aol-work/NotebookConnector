bl_info = {
    "name": "BNotebooks",
    "author": "Brady Johnston",
    "version": (0, 0, 1),
    "blender": (3, 5, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Makes Blender available as a jupyter kernal.",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
    }


import bpy
# from . import auto_load

# auto_load.init()

from . import pref

def register():
    bpy.utils.register_class(pref.BNotebooksPreferences)
    bpy.utils.register_class(pref.BN_Kernel_Append)
    bpy.utils.register_class(pref.BN_Kernel_Remove)


def unregister():
    bpy.utils.unregister_class(pref.BNotebooksPreferences)
    bpy.utils.unregister_class(pref.BN_Kernel_Append)
    bpy.utils.unregister_class(pref.BN_Kernel_Remove)
