import bpy


# Constant sub panels of the EmoijiText addon

# from . EmojiText_sub_panels_smiles import *


# These import helps in keeping all classes in one place, easier to manage. They are all stored in 'classes' tuple at the end of this file.

from . EmojiText_sub_panels_smiles_new import TEXT_OT_EMOJI_SMILES, TEXT_PT_EMOJI_SMILES_PANEL, TEXT_OT_INSERT_SMILES
from . EmojiText_sub_panels_symbols import TEXT_OT_EMOJI_SYMBOLS, TEXT_OT_INSERT_SYMBOLS, TEXT_PT_EMOJI_SYMBOLS_PANEL
from . EmojiText_sub_panels_objects import TEXT_OT_EMOJI_OBJECTS, TEXT_OT_INSERT_OBJECT, TEXT_PT_EMOJI_OBJECTS_PANEL
from . EmojiText_sub_panels_people_and_body import TEXT_OT_EMOJI_PEOPLE_AND_BODY, TEXT_OT_INSERT_PEOPLE_AND_BODY, TEXT_PT_EMOJI_PEOPLE_AND_BODY_PANEL
from . EmojiText_sub_panels_animals_and_nature import TEXT_OT_EMOJI_ANIMALS_AND_NATURE, TEXT_OT_INSERT_ANIMALS_AND_NATURE, TEXT_PT_EMOJI_ANIMALS_AND_NATURE
from . EmojiText_sub_panels_activities import TEXT_OT_EMOJI_ACTIVITIES, TEXT_OT_INSERT_ACTIVITIES, TEXT_PT_EMOJI_ACTIVITIES_PANEL
from . EmojiText_sub_panels_food_and_drink import TEXT_OT_EMOJI_FOOD_AND_DRINK, TEXT_OT_INSERT_FOOD_AND_DRINK, TEXT_PT_EMOJI_FOOD_AND_DRINK
from . EmojiText_sub_panels_travel_and_places import TEXT_OT_EMOJI_TRAVEL_AND_PLACES, TEXT_OT_INSERT_TRAVEL_AND_PLACES, TEXT_PT_EMOJI_TRAVEL_AND_PLACES
from . EmojiText_sub_panels_flags import TEXT_OT_EMOJI_FLAGS, TEXT_OT_INSERT_FLAGS, TEXT_PT_EMOJI_FLAGS_PANEL


# from . EmojiText_panel_Blender_Friendly import TEXT_PT_BLENDER_EMOJI_CATEGORIES # keeping it out as of now to avoid clutter

# Text formatting panel
from . Editor_text_format import TEXT_PT_unicode_style, TEXT_OT_live_style


# from . Help_Panel import TEXT_PT_HELP_PANEL   # Replaced with Help_Settings_Panel.py
from . Help_Settings_Panel import LanguageOptionDropDown, TEXT_PT_HELP_SETTINGS_PANEL, LANGUAGE_OT_Update, FAQ_OT_Open, DOCS_OT_Open, RATE_US_OT_Open, SHARE_OT_Open, CONTACT_US_OT_Open, ABOUT_US_OT_Open


# Registering the emoji_active_category property.
# Add property definition at module level

# WHY THE def init() and def cleanup() functions?
# To avoid potential conflicts or errors during the registration and un-registration process of the addon. ??
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


# Categories of emojis starts here

# Frame that contains all emojis categories.
class TEXT_PT_EMOJI_CATEGORIES(bpy.types.Panel):
    bl_space_type = 'TEXT_EDITOR'  # Changed from VIEW_3D
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    # Just "Categories" Not Emoji Categories, as this takes up space in the UI, keep it clean and less cluttered.
    # And default space when opened , it fits right in. NO need tp expand, keeping it minimal.
    bl_label = "Emoji Categories"
    bl_options = {'DEFAULT_CLOSED'}  # Start closed
    # bl_order = 2  # After Frequently Used

    def draw(self, context):
        layout = self.layout

        # First row of emojis
        row = layout.row(align=True)

        # Add categories as buttons in the row
        row.operator("text.emoji_symbols", text="✔️")  # Symbols
        row.operator("text.emoji_objects", text="🔔")  # Objects
        row.operator("text.emoji_smiles", text="😊")  # Smiles

        # Second row
        row = layout.row(align=True)
        # People & Body
        row.operator("text.emoji_people_and_body", text="👩")

        # Animals & Nature
        row.operator("text.emoji_animals_and_nature", text="🐱")

        # Activities
        row.operator("text.emoji_activities", text="🎄")

        # Third row
        row = layout.row(align=True)

       # Food & Drink
        row.operator("text.emoji_food_and_drink", text="🍩")

        # Travel & Places
        row.operator("text.emoji_travel_and_places", text="🛩️")

        # Flags
        row.operator("text.emoji_flags", text="🚩")


# List of all classes to be registered of the panels.
classes = (TEXT_PT_EMOJI_CATEGORIES,
           TEXT_OT_EMOJI_SMILES, TEXT_OT_INSERT_SMILES, TEXT_PT_EMOJI_SMILES_PANEL,
           TEXT_OT_EMOJI_SYMBOLS, TEXT_OT_INSERT_SYMBOLS, TEXT_PT_EMOJI_SYMBOLS_PANEL,
           TEXT_OT_EMOJI_OBJECTS, TEXT_OT_INSERT_OBJECT, TEXT_PT_EMOJI_OBJECTS_PANEL,
           TEXT_OT_EMOJI_PEOPLE_AND_BODY, TEXT_OT_INSERT_PEOPLE_AND_BODY, TEXT_PT_EMOJI_PEOPLE_AND_BODY_PANEL,
           TEXT_OT_EMOJI_ANIMALS_AND_NATURE, TEXT_OT_INSERT_ANIMALS_AND_NATURE, TEXT_PT_EMOJI_ANIMALS_AND_NATURE,
           TEXT_OT_EMOJI_ACTIVITIES, TEXT_OT_INSERT_ACTIVITIES, TEXT_PT_EMOJI_ACTIVITIES_PANEL,
           TEXT_OT_EMOJI_FOOD_AND_DRINK, TEXT_OT_INSERT_FOOD_AND_DRINK, TEXT_PT_EMOJI_FOOD_AND_DRINK,
           TEXT_OT_EMOJI_TRAVEL_AND_PLACES, TEXT_OT_INSERT_TRAVEL_AND_PLACES, TEXT_PT_EMOJI_TRAVEL_AND_PLACES,
           TEXT_OT_EMOJI_FLAGS, TEXT_OT_INSERT_FLAGS, TEXT_PT_EMOJI_FLAGS_PANEL,
           TEXT_PT_unicode_style, TEXT_OT_live_style,
           LanguageOptionDropDown, TEXT_PT_HELP_SETTINGS_PANEL, LANGUAGE_OT_Update, FAQ_OT_Open, DOCS_OT_Open, RATE_US_OT_Open, SHARE_OT_Open, CONTACT_US_OT_Open, ABOUT_US_OT_Open)


# These classes are not included for registration, as of now.
# They can be added back if needed in the future either as a feature or for debugging purposes.

#   TEXT_PT_BLENDER_EMOJI_CATEGORIES # Keeping it out as of now to avoid clutter
#   TEXT_PT_HELP_PANEL
#   TEXT_PT_FREQUENTLY_USED_EMOJIS,
#   TEXT_PT_MORE_PANEL)
#   TEXT_PT_MORE_EMOJI_CATEGORIES,
#   TEXT_OT_EMOJI_ANIMALS, TEXT_OT_EMOJI_FOOD
