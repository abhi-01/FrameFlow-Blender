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


# Loading emoji data for Animals & Nature category
EMOJI_INFO = load_emoji_database("Animals & Nature")


# BOILER PLATE USAGE STARTS HERE
class TEXT_OT_EMOJI_ANIMALS_AND_NATURE(BaseEmojiCategoryOperator):
    bl_idname = "text.emoji_animals_and_nature"
    bl_label = "Animals & Nature"
    bl_description = "Animals & Nature"
    category_name = "ANIMALS_AND_NATURE"


class TEXT_OT_INSERT_ANIMALS_AND_NATURE(BaseEmojiInsertOperator):
    bl_idname = "text.insert_animals_and_nature"
    bl_label = "Insert Animals & Nature"


class TEXT_PT_EMOJI_ANIMALS_AND_NATURE(BaseEmojiPanel):
    bl_label = "Animals & Nature"
    category_key = "ANIMALS_AND_NATURE"
    emoji_data = EMOJI_INFO
    insert_operator = "text.insert_animals_and_nature"


# All the classes in here have to be imported in the EmojiText_sub_panels.py file and added to its classes tuple
# Precautionary
# Make the class available for import
__all__ = [
    'TEXT_OT_EMOJI_ANIMALS_AND_NATURE',
    'TEXT_OT_INSERT_ANIMALS_AND_NATURE',
    'TEXT_PT_EMOJI_ANIMALS_AND_NATURE'
]
