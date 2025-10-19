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


# Loading emoji data for Activities category
EMOJI_INFO = load_emoji_database("Activities")


# BOILER PLATE USAGE STARTS HERE
class TEXT_OT_EMOJI_ACTIVITIES(BaseEmojiCategoryOperator):
    bl_idname = "text.emoji_activities"
    bl_label = "Activities"
    bl_description = "Activities"
    category_name = 'ACTIVITIES'


class TEXT_OT_INSERT_ACTIVITIES(BaseEmojiInsertOperator):
    bl_idname = "text.insert_activities"
    bl_label = "Insert Activities"


class TEXT_PT_EMOJI_ACTIVITIES_PANEL(BaseEmojiPanel):
    bl_label = "Activities"
    category_key = 'ACTIVITIES'
    emoji_data = EMOJI_INFO
    insert_operator = "text.insert_activities"


__all__ = [
    'TEXT_OT_EMOJI_ACTIVITIES',
    'TEXT_OT_INSERT_ACTIVITIES',
    'TEXT_PT_EMOJI_ACTIVITIES_PANEL'
]
