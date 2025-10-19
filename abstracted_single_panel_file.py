"""Unified emoji sub-panels - replaces all individual sub-panel files"""

import bpy
from .boiler_plate import BaseEmojiInsertOperator, BaseEmojiCategoryOperator, BaseEmojiPanel
from .emoji_database_search import load_emoji_database
from .emoji_category_single_file_list import EMOJI_CATEGORIES

# Store generated classes
LIST_OF_CLASSES = []

# Dynamically create classes for each category
for config in EMOJI_CATEGORIES:
    category_name = config["name"]
    category_key = config["key"]
    insert_op_id = config["insert_op_id"]
    category_op_id = config["category_op_id"]
    label = config["label"]

    # Load emoji data for this category
    emoji_data = load_emoji_database(category_name)

    # 1. Create Category Operator (button that switches to this category)
    CategoryOperator = type(
        f"TEXT_OT_EMOJI_{category_key}",
        (BaseEmojiCategoryOperator,),
        {
            "bl_idname": category_op_id,
            "bl_label": label,
            "bl_description": f"Show {label} emojis",
            "category_name": category_key
        }
    )
    LIST_OF_CLASSES.append(CategoryOperator)

    # 2. Create Insert Operator (inserts emoji into text editor)
    InsertOperator = type(
        f"TEXT_OT_INSERT_{category_key}",
        (BaseEmojiInsertOperator,),
        {
            "bl_idname": insert_op_id,
            "bl_label": f"Insert {label}"
        }
    )
    LIST_OF_CLASSES.append(InsertOperator)

    # 3. Create Panel (displays emojis in UI)
    Panel = type(
        f"TEXT_PT_EMOJI_{category_key}_PANEL",
        (BaseEmojiPanel,),
        {
            "bl_label": label,
            "category_key": category_key,
            "emoji_data": emoji_data,
            "insert_operator": insert_op_id
        }
    )
    LIST_OF_CLASSES.append(Panel)

# Make all classes available for import


def get_classes():
    """Return all dynamically generated classes for registration"""
    return LIST_OF_CLASSES
