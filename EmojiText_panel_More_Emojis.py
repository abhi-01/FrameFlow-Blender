import bpy


# # IMPORTANT: DO NOT DELETE THIS FILE.
# This class is not added to the main panel.
# This is kept to add specific symbols that might be useful for Blender but are not covered by Emojis.


class TEXT_PT_MORE_EMOJI_CATEGORIES(bpy.types.Panel):

    bl_space_type = 'TEXT_EDITOR'  # Changed from VIEW_3D
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_label = "More Emojis"  # Emojis"--> removed to save space
    bl_options = {'DEFAULT_CLOSED'}  # Start closed

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)

        # # Add categories as buttons in the row
        # row.operator("text.emoji_symbols", text="✔️")  # Symbols
        # row.operator("text.emoji_objects", text="🔔")  # Objects
        # row.operator("text.emoji_animals", text="🐾")  # Animals
        # row.operator("text.emoji_food", text="🍔")     # Food
        # row.operator("text.emoji_smiles", text="😊")  # Smiles
        # # row.operator("text.emoji_animals", text="🎲")   # Activities
