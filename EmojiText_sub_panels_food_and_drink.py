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

# Loading  the emoji data for Food & Drink category
EMOJI_INFO = load_emoji_database("Food & Drink")


# BOILER PLATE USAGE STARTS HERE
class TEXT_OT_EMOJI_FOOD_AND_DRINK(BaseEmojiCategoryOperator):
    bl_idname = "text.emoji_food_and_drink"
    bl_label = "Food & Drink"
    bl_description = "Food & Drink"
    category_name = 'FOOD_AND_DRINK'


class TEXT_OT_INSERT_FOOD_AND_DRINK(BaseEmojiInsertOperator):
    bl_idname = "text.insert_food_and_drink"
    bl_label = "Insert Food & Drink"


class TEXT_PT_EMOJI_FOOD_AND_DRINK(BaseEmojiPanel):
    bl_label = "Food & Drink"
    category_key = 'FOOD_AND_DRINK'
    emoji_data = EMOJI_INFO
    insert_operator = "text.insert_food_and_drink"


# All the classes in here have to be imported in the EmojiText_sub_panels.py file and added to its classes tuple
# Precautionary
# Make the class available for import
__all__ = [
    'TEXT_OT_EMOJI_FOOD_AND_DRINK',
    'TEXT_OT_INSERT_FOOD_AND_DRINK',
    'TEXT_PT_EMOJI_FOOD_AND_DRINK'
]
