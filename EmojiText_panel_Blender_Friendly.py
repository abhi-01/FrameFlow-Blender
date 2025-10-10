import bpy

# To be added to main panel. Commenting it out for now to avoid clutter..


class TEXT_PT_BLENDER_EMOJI_CATEGORIES(bpy.types.Panel):

    bl_space_type = 'TEXT_EDITOR'  # Changed from VIEW_3D
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_label = "Blender Friendly"  # Emojis"--> removed to save space
    bl_options = {'DEFAULT_CLOSED'}  # Start closed

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)