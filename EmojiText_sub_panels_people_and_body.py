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


# Loading  the emoji data for People & Body category
EMOJI_INFO = load_emoji_database("People & Body")


# BOILER PLATE USAGE STARTS HERE
class TEXT_OT_EMOJI_PEOPLE_AND_BODY(BaseEmojiCategoryOperator):
    bl_idname = "text.emoji_people_and_body"
    bl_label = "People & Body"
    bl_description = "People & Body"
    category_name = 'PEOPLE_AND_BODY'


class TEXT_OT_INSERT_PEOPLE_AND_BODY(BaseEmojiInsertOperator):
    bl_idname = "text.insert_people_and_body"
    bl_label = "Insert People & Body Emoji"


class TEXT_PT_EMOJI_PEOPLE_AND_BODY_PANEL(BaseEmojiPanel):
    bl_label = "People & Body"
    category_key = 'PEOPLE_AND_BODY'
    emoji_data = EMOJI_INFO
    insert_operator = "text.insert_people_and_body"


# All the classes in here have to be imported in the EmojiText_sub_panels.py file and added to its classes tuple
# Precautionary
# Make the class available for import
__all__ = [
    'TEXT_OT_EMOJI_PEOPLE_AND_BODY',
    'TEXT_OT_INSERT_PEOPLE_AND_BODY',
    'TEXT_PT_EMOJI_PEOPLE_AND_BODY_PANEL'
]
