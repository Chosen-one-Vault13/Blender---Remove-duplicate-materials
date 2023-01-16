import bpy
from .main_script import register, unregiste

bl_info = {
    "name": "Remove Duplicate Materials",
    "author": "Gustavo Alcarde - AI",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tools > Remove Duplicate Materials",
    "description": "Removes duplicate materials and remaps them to a single one",
    "category": "Material",
}

def register():
    bpy.utils.register_class(RemoveDuplicateMaterialsButton)
    bpy.utils.register_class(RemoveDuplicateMaterials)

def unregister():
    bpy.utils.unregister_class(RemoveDuplicateMaterialsButton)
    bpy.utils.unregister_class(RemoveDuplicateMaterials)

if __name__ == "__main__":
    register()
