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


# Loading emoji data for Flags category
EMOJI_INFO = load_emoji_database("Flags")


# BOILER PLATE USAGE STARTS HERE
class TEXT_OT_EMOJI_FLAGS(BaseEmojiCategoryOperator):
    bl_idname = "text.emoji_flags"
    bl_label = "Flags"
    bl_description = "Flags"
    category_name = 'FLAGS'


class TEXT_OT_INSERT_FLAGS(BaseEmojiInsertOperator):
    bl_idname = "text.insert_flags"
    bl_label = "Insert Flags"


class TEXT_PT_EMOJI_FLAGS_PANEL(BaseEmojiPanel):
    bl_label = "Flags"
    category_key = "FLAGS"
    emoji_data = EMOJI_INFO
    insert_operator = "text.insert_flags"


__all__ = [
    'TEXT_OT_EMOJI_FLAGS',
    'TEXT_OT_INSERT_FLAGS',
    'TEXT_PT_EMOJI_FLAGS_PANEL'
]
