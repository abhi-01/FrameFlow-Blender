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


# Loading  the emoji data for Symbols category
EMOJI_INFO = load_emoji_database("Symbols")

# BOILER PLATE USAGE STARTS HERE


class TEXT_OT_EMOJI_SYMBOLS(BaseEmojiCategoryOperator):
    bl_idname = "text.emoji_symbols"
    bl_label = "Symbols"
    bl_description = "Symbols"
    category_name = 'SYMBOLS'


class TEXT_OT_INSERT_SYMBOLS(BaseEmojiInsertOperator):
    bl_idname = "text.insert_symbols"
    bl_label = "Insert Symbols"


class TEXT_PT_EMOJI_SYMBOLS_PANEL(BaseEmojiPanel):
    bl_label = "Symbols"
    category_key = 'SYMBOLS'
    emoji_data = EMOJI_INFO
    insert_operator = "text.insert_symbols"


# All the classes in here have to be imported in the EmojiText_sub_panels.py file and added to its classes tuple
# Precautionary
# Make the class available for import
__all__ = [
    'TEXT_OT_EMOJI_SYMBOLS',
    'TEXT_OT_INSERT_SYMBOLS',
    'TEXT_PT_EMOJI_SYMBOLS_PANEL'
]
