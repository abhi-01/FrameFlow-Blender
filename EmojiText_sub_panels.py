import bpy
from .abstracted_single_panel_file import get_classes


"""Main emoji sub-panels file - now just imports from unified file"""


# Main emoji categories panel (keeps the category buttons)
class TEXT_PT_EMOJI_CATEGORIES(bpy.types.Panel):
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_label = "Emojis"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        # Debug line - shows current active category
        layout.label(text=f"Active: {context.scene.emoji_active_category}")

        # Category buttons (3 rows)
        row = layout.row(align=True)
        row.operator("text.emoji_smiles", text="😊")
        row.operator("text.emoji_people_and_body", text="👤")
        row.operator("text.emoji_animals_and_nature", text="🐱")

        row = layout.row(align=True)
        row.operator("text.emoji_food_and_drink", text="🍩")
        row.operator("text.emoji_activities", text="⚽")
        row.operator("text.emoji_travel_and_places", text="✈️")

        row = layout.row(align=True)
        row.operator("text.emoji_objects", text="🔔")
        row.operator("text.emoji_symbols", text="✔️")
        row.operator("text.emoji_flags", text="🚩")


# Registering the emoji_active_category property.
# Add property definition at module level

# WHY THE def init() and def cleanup() functions?
# To avoid potential conflicts or errors during the registration and un-registration process of the addon. ??!
def init():
    bpy.types.Scene.emoji_active_category = bpy.props.StringProperty(
        name="Active Emoji Category",
        default=""
    )
    # # Add the search property here
    bpy.types.Scene.emoji_search_query = bpy.props.StringProperty(
        name="Search Emojis",
        description="Search emojis by name, category, tags, or aliases",
        default="",
        # update=lambda self, context: None
    )


def cleanup():
    if hasattr(bpy.types.Scene, "emoji_active_category"):
        del bpy.types.Scene.emoji_active_category

    # Clean up search property too
    if hasattr(bpy.types.Scene, "emoji_search_query"):
        del bpy.types.Scene.emoji_search_query


# Get all dynamically generated classes from the abstracted file
classes = [TEXT_PT_EMOJI_CATEGORIES] + get_classes()


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
