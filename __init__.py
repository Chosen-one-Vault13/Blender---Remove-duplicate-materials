bl_info = {
    "name": "Remove Duplicate Materials",
    "author": "Gustavo Alcarde - AI",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tools > Remove Duplicate Materials",
    "description": "Removes duplicate materials and remaps them to a single one",
    "category": "Material",
}

import bpy
from .remove_duplicate_materials import RemoveDuplicateMaterials

classes = (
    RemoveDuplicateMaterials,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
