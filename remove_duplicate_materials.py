import bpy
import re

def purge_unused_materials():
    materials_to_remove = []
    for material in bpy.data.materials:
        if not material.users:
            materials_to_remove.append(material)
    for material in materials_to_remove:
        bpy.data.materials.remove(material)

def remap_materials():
    # Iterate over all materials in the scene
    for material in bpy.data.materials:
        # check if the material's name matches the pattern "materialname.0xx"
        match = re.match(r"(.+)\.0\d{2}", material.name)
        if match:
            # Get a reference to the material we want to remap to
            remap_to_material = bpy.data.materials.get(match.group(1))
            # Iterate over all objects in the scene
            for obj in bpy.data.objects:
                # Check if the object uses the material
                if material.name in [m.name for m in obj.material_slots]:
                    # Assign the remap_to_material to the object
                    obj.material_slots[obj.material_slots.find(material.name)].material = remap_to_material
    purge_unused_materials()

class RemoveDuplicateMaterials(bpy.types.Operator):
    """Removes duplicate materials and remaps them to a single one"""
    bl_idname = "material.remove_duplicate_materials"
    bl_label = "Remove Duplicate Materials"

    def execute(self, context):
        remap_materials()
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return self.execute(context)

def register():
    bpy.utils.register_class(RemoveDuplicateMaterials)

def unregister():
    bpy.utils.unregister_class(RemoveDuplicateMaterials)

if __name__ == "__main__":
    register()
