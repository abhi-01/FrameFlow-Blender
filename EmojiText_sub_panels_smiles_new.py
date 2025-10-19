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


# Loading  the emoji data for Smileys & Emotion category
EMOJI_INFO = load_emoji_database("Smileys & Emotion")


# BOILER PLATE USAGE STARTS HERE
class TEXT_OT_EMOJI_SMILES(BaseEmojiCategoryOperator):
    bl_idname = "text.emoji_smiles"
    bl_label = "Smiles"
    bl_description = "Smiley"
    category_name = 'SMILES'


class TEXT_OT_INSERT_SMILES(BaseEmojiInsertOperator):
    bl_idname = "text.insert_smiles"
    bl_label = "Insert Smiles"


class TEXT_PT_EMOJI_SMILES_PANEL(BaseEmojiPanel):
    bl_label = "Smiles"
    category_key = 'SMILES'
    emoji_data = EMOJI_INFO
    insert_operator = "text.insert_smiles"


# All the classes in here have to be imported in the EmojiText_sub_panels.py file and added to its classes tuple
# Precautionary
# Make the class available for import
__all__ = ['TEXT_OT_EMOJI_SMILES',
           'TEXT_OT_INSERT_SMILES', 'TEXT_PT_EMOJI_SMILES_PANEL']
