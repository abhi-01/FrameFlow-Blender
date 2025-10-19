import os
import json


def load_emoji_database(category=None):
    """Load emoji data from external file, optionally filtered by category"""
    emoji_data = {}

    # Get addon directory path
    addon_dir = os.path.dirname(os.path.realpath(__file__))
    database_path = os.path.join(addon_dir, "emoji_database.txt")

    print(f"Looking for emoji database at: {database_path}")

    try:
        with open(database_path, 'r', encoding='utf-8') as file:
            # Load JSON data
            all_emojis = json.load(file)

            # Filter by category if specified
            if category:
                for emoji, data in all_emojis.items():
                    if data.get("category") == category:
                        emoji_data[emoji] = data
            else:
                emoji_data = all_emojis

    except FileNotFoundError:
        print(f"Warning: emoji_database.txt not found at {database_path}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        emoji_data = {}
    except Exception as e:
        print(f"Error loading emoji database: {e}")
        emoji_data = {}

    category_name = category if category else "all categories"
    print(f"Loaded {len(emoji_data)} emojis from {category_name}")
    return emoji_data
