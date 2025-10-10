import bpy
import os
import json


# These are the features associated with all emojis
# Emojis : 🥇
# Category: Activities
# Sub group : award-medal
# Name: in all 14 languages.
# Aliases : "....medalla de oro, ميدالية مركز أول,..."
# Tags : "......Tags: 1st, activities, award-medal, birincilik, de, d’or, d’oro, emas, goldmedaille, ....."


# Performs a check to see if the file exists, and then load it.
def load_emoji_database():
    """Load emoji data from external file"""
    emoji_data = {}

    # Get addon directory path
    addon_dir = os.path.dirname(os.path.realpath(__file__))
    database_path = os.path.join(addon_dir, "emoji_database.txt")

    print(f"Looking for emoji database at: {database_path}")

    try:
        with open(database_path, 'r', encoding='utf-8') as file:
            # Load JSON data
            all_emojis = json.load(file)

            # Filter only "Symbols" category
            for emoji, data in all_emojis.items():
                if data.get("category") == "Symbols":
                    emoji_data[emoji] = data

    except FileNotFoundError:
        print(f"Warning: emoji_database.txt not found at {database_path}")

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        emoji_data = {}
    except Exception as e:
        print(f"Error loading emoji database: {e}")
        emoji_data = {}

    print(f"Loaded {len(emoji_data)} emojis from Symbols category")
    return emoji_data


# Load emoji data with rich metadata
EMOJI_INFO = load_emoji_database()


class TEXT_OT_EMOJI_SYMBOLS(bpy.types.Operator):
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_label = "Symbols"
    bl_idname = "text.emoji_symbols"
    bl_description = "Symbols"

    def execute(self, context):
        # Set active category in scene properties
        context.scene.emoji_active_category = 'SYMBOLS'
        return {'FINISHED'}


class TEXT_OT_INSERT_SYMBOLS(bpy.types.Operator):
    bl_idname = "text.insert_symbol"
    bl_label = "Insert Symbol"

    emoji: bpy.props.StringProperty(
        name="Emoji",
        description="The emoji character to insert",
        default="⭐"
    )

    tooltip: bpy.props.StringProperty(
        name="Tooltip",
        description="Hover description for the emoji",
        default=""
    )

    @classmethod
    def description(cls, context, properties):
        return properties.tooltip if properties.tooltip else "Insert emoji into text editor"

    def execute(self, context):
        if context.space_data.type == 'TEXT_EDITOR' and context.space_data.text:
            context.space_data.text.write(self.emoji)
        return {'FINISHED'}


# Panel to contain emojis, a grid with four columns.
class TEXT_PT_EMOJI_SYMBOLS_PANEL(bpy.types.Panel):
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_label = "Symbols"
    bl_parent_id = "TEXT_PT_EMOJI_CATEGORIES"

    @classmethod
    def poll(cls, context):
        return context.scene.emoji_active_category == 'SYMBOLS'

    def draw(self, context):
        layout = self.layout
        # Debug info
        layout.label(text=f"Found {len(EMOJI_INFO)} emojis")
        grid = layout.grid_flow(columns=4, align=True)

        # Get selected language from scene properties
        selected_language = bpy.context.scene.language_options_dropdown.languages
        for emoji, data in EMOJI_INFO.items():
            props = grid.operator("text.insert_food_and_drink", text=emoji)
            props.emoji = emoji
            if isinstance(data, dict):

                # Get emoji name in selected language, fallback to English if not available
                emoji_name = data.get("names", {}).get(selected_language,
                                                       # Fallback to English if selected language not available
                                                       data.get("names", {}).get("en", "Unknown Emoji"))

                # Not sure if it is needed. right now.
                emoji_category = data.get("category", "Unknown Category")
                # Not sure if it is needed. right now.
                emoji_subgroup = data.get("subgroup", "")

                tooltip_text = f"{emoji_name}"
                # # This was taking space so commented it out, keeping it minimal.
                # if emoji_subgroup:
                #     tooltip_text += f" ({emoji_subgroup})"
                props.tooltip = tooltip_text
            else:
                props.tooltip = str(data)


# All the classes in here have to be imported in the EmojiText_sub_panels.py file and added to its classes tuple
# Precautionary
# Make the class available for import
__all__ = [
    'TEXT_OT_EMOJI_SYMBOLS',
    'TEXT_OT_INSERT_SYMBOLS',
    'TEXT_PT_EMOJI_SYMBOLS_PANEL'
]
