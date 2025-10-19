import bpy


# These are the features associated with all emojis
# Emojis : 🥇
# Category: Activities
# Sub group : award-medal
# Name: in all 14 languages.
# Aliases : "....medalla de oro, ميدالية مركز أول,..."
# Tags : "......Tags: 1st, activities, award-medal, birincilik, de, d’or, d’oro, emas, goldmedaille, ....."


# IMPORTING FROM BOILER PLATE
from .boiler_plate import BaseEmojiInsertOperator, BaseEmojiCategoryOperator, BaseEmojiPanel


from .emoji_database_search import load_emoji_database


# Loading  the emoji data for Objects category
EMOJI_INFO = load_emoji_database("Objects")


# BOILER PLATE USAGE STARTS HERE
class TEXT_OT_EMOJI_OBJECTS(BaseEmojiCategoryOperator):
    bl_idname = "text.emoji_objects"
    bl_label = "Objects"
    bl_description = "Objects"
    category_name = 'OBJECTS'


class TEXT_OT_INSERT_OBJECT(BaseEmojiInsertOperator):
    bl_idname = "text.insert_object"
    bl_label = "Insert Object"


class TEXT_PT_EMOJI_OBJECTS_PANEL(BaseEmojiPanel):
    bl_label = "Objects"
    category_key = 'OBJECTS'
    emoji_data = EMOJI_INFO
    insert_operator = "text.insert_object"


# All the classes in here have to be imported in the EmojiText_sub_panels.py file and added to its classes tuple
# Precautionary
# Make the class available for import
__all__ = [
    'TEXT_OT_EMOJI_OBJECTS',
    'TEXT_OT_INSERT_OBJECT',
    'TEXT_PT_EMOJI_OBJECTS_PANEL'
]
