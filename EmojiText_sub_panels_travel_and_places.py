import json


# These are the features associated with all emojis
# Emojis : 🥇
# Category: Activities
# Sub group : award-medal
# Name: in all 14 languages.
# Aliases : "....medalla de oro, ميدالية مركز أول,..."
# Tags : "......Tags: 1st, activities, award-medal, birincilik, de, d’or, d’oro, emas, goldmedaille, ....."
# Function to load emoji database, just a safety check.

# IMPORTING FROM BOILER PLATE
from .boiler_plate import BaseEmojiInsertOperator, BaseEmojiCategoryOperator, BaseEmojiPanel


from .emoji_database_search import load_emoji_database


# Loading  the emoji data for Travel & Places category
EMOJI_INFO = load_emoji_database("Travel & Places")


class TEXT_OT_EMOJI_TRAVEL_AND_PLACES(BaseEmojiCategoryOperator):
    bl_idname = "text.emoji_travel_and_places"
    bl_label = "Travel & Places"
    bl_description = "Travel & Places"
    category_name = 'TRAVEL_AND_PLACES'


class TEXT_OT_INSERT_TRAVEL_AND_PLACES(BaseEmojiInsertOperator):
    bl_idname = "text.insert_travel_and_places"
    bl_label = "Insert Travel & Places"


class TEXT_PT_EMOJI_TRAVEL_AND_PLACES(BaseEmojiPanel):
    bl_label = "Travel & Places"
    category_key = 'TRAVEL_AND_PLACES'
    emoji_data = EMOJI_INFO
    insert_operator = "text.insert_travel_and_places"


# All the classes in here have to be imported in the EmojiText_sub_panels.py file and added to its classes tuple
# Precautionary
# Make the class available for import
__all__ = [
    'TEXT_OT_EMOJI_TRAVEL_AND_PLACES',
    'TEXT_OT_INSERT_TRAVEL_AND_PLACES',
    'TEXT_PT_EMOJI_TRAVEL_AND_PLACES'
]
