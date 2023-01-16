bl_info = {
    "name": "Remove Duplicate Materials",
    "author": "Gustavo Alcarde-AI",
    "version": (1, 0, 0),
    "blender": (2, 83, 0),
    "location": "View3D > Toolbar > Remove Duplicate Materials",
    "description": "Removes duplicate materials and remaps them to a single one",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Material"
}

def register():
    bpy.utils.register_class(RemoveDuplicateMaterials)

def unregister():
    bpy.utils.unregister_class(RemoveDuplicateMaterials)
