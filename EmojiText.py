import bpy

# Contains the search functionality for emojis,
# including the search bar and
# search results in a 4 column grid.


# To change keywords for searching, In the function "def search_emojis(query):"
# see the code following the comment --> # CHANGE KEYWORDS OPTIONS FOR SEARCHING:

from .emoji_database_search import load_emoji_database

# # Loading  the emoji data for Symbols category
# Load the database once
EMOJI_DATABASE = load_emoji_database()


# This function takes into account the selected language for searching
# and goes through all the metadata provided in the emoji database "EMOJI_DATABASE"
# The categories of metadata can be added or removed.
def search_emojis(query):
    """Search emojis based on query matching any metadata field"""
    if not query:
        return {}

    query_lower = query.lower()
    results = {}

    # Get selected language from scene properties - FIX THE CONTEXT ACCESS
    selected_language = bpy.context.scene.language_options_dropdown.languages

    for emoji, data in EMOJI_DATABASE.items():
        # Check all searchable fields with correct field names
        searchable_text = []

        # Add name from selected language AND English fallback for search
        if isinstance(data.get("names"), dict):
            # Try selected language first
            emoji_name_selected = data.get(
                "names", {}).get(selected_language, "")
            if emoji_name_selected:
                searchable_text.append(emoji_name_selected.lower())

            # ALWAYS add English name too for broader search results
            emoji_name_en = data.get("names", {}).get("en", "")
            if emoji_name_en and emoji_name_en != emoji_name_selected:
                searchable_text.append(emoji_name_en.lower())

        # CHANGE KEYWORDS OPTIONS FOR SEARCHING:
        # Add whatever fields are necessary, commenting out all of them as of now.
        # Add other fields (check if they exist in your database)
        searchable_text.extend([
            data.get("category", "").lower(),
            data.get("subgroup", "").lower()
        ])

        # # Add aliases
        # aliases = data.get("aliases", [])
        # if isinstance(aliases, list):
        #     searchable_text.extend([alias.lower() for alias in aliases])

        # # Add tags
        # tags = data.get("tags", [])
        # if isinstance(tags, list):
        #     searchable_text.extend([tag.lower() for tag in tags])

        # Check if query matches any field
        if any(query_lower in text for text in searchable_text if text):
            results[emoji] = data

    return results


# Main Panel class
class TEXT_PT_EMOJI_TEXT(bpy.types.Panel):
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_label = "Emoji Text"

    def draw(self, context):
        layout = self.layout

        # # Temporarily disable search to stop the errors
        # layout.label(text="Search temporarily disabled")

        # Search input field
        row = layout.row()
        row.prop(context.scene, "emoji_search_query", text="", icon='VIEWZOOM')
        row.operator("frameflow.manual_search", text="", icon='ZOOM_IN')

        # TO BE ADDED LATER
        # # Frequently used emojis - Placeholder for now
        # # Most used emojis
        # row = layout.row()
        # row.label(text="Most Used:")

        # Search results
        search_query = context.scene.emoji_search_query
        if search_query:
            search_results = search_emojis(search_query)

            if search_results:
                box = layout.box()
                box.label(text=f"Found {len(search_results)} emojis:")

                # Display results in grid
                # More columns for compact display
                grid = box.grid_flow(columns=4, align=True)

                for emoji, data in search_results.items():
                    props = grid.operator("frameflow.insert_emoji", text=emoji)
                    props.emoji = emoji
                    if isinstance(data, dict):
                        # Use the SAME selected language as the search function
                        selected_language = bpy.context.scene.language_options_dropdown.languages
                        # emoji_name = data.get("names", {}).get(
                        #     "en", "Unknown Emoji")
                        # Get emoji name in selected language with English fallback
                        emoji_name = data.get("names", {}).get(selected_language,
                                                               data.get("names", {}).get("en", "Unknown Emoji"))
                        # Not sure if it is needed. right now.
                        emoji_category = data.get(
                            "category", "Unknown Category")
                        # Not sure if it is needed. right now.
                        emoji_subgroup = data.get("subgroup", "")

                        tooltip_text = f"{emoji_name}"
                        # # This was taking space so commented it out, keeping it minimal.
                        # if emoji_subgroup:
                        #     tooltip_text += f" ({emoji_subgroup})"
                        props.tooltip = tooltip_text
                    else:
                        props.tooltip = str(data)

            else:
                box = layout.box()
                box.label(text=f"No results for '{search_query}'", icon='INFO')
        # No need for it, as it was simple adding an extra label that was not necessary.
        # else:
        #     # Show instruction when no search query
        #     box = layout.box()
        #     box.label(text="Type to search emojis...", icon='VIEWZOOM')


# Search operator (keeping the original popup search)
# ADD UPDATE FUNCTION FOR REAL-TIME SEARCH
def update_emoji_search(self, context):
    """Force panel redraw when search query changes"""
    # This forces the panel to redraw and show updated results
    for region in context.area.regions:
        if region.type == 'UI':
            region.tag_redraw()


class TEXT_OT_emoji_search(bpy.types.Operator):
    bl_idname = "frameflow.emoji_search"
    bl_label = "Emoji Finder"
    bl_property = "emoji_enum"

    emoji_enum: bpy.props.EnumProperty(
        items=lambda self, context: [(emoji, data.get("name", emoji)[:20], data.get("name", ""))
                                     for emoji, data in EMOJI_DATABASE.items()],
        name='Select Emoji'
    )

    def execute(self, context):
        if context.space_data.type == 'TEXT_EDITOR' and context.space_data.text:
            context.space_data.text.write(self.emoji_enum)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.invoke_search_popup(self)
        return {'FINISHED'}


# Emoji insertion operator for search results
class TEXT_OT_insert_emoji(bpy.types.Operator):
    bl_idname = "frameflow.insert_emoji"
    bl_label = "Insert Emoji"

    emoji: bpy.props.StringProperty(default="")
    tooltip: bpy.props.StringProperty(default="")

    @classmethod
    def description(cls, context, properties):
        return properties.tooltip if properties.tooltip else f"Insert {properties.emoji}"

    def execute(self, context):
        if context.space_data.type == 'TEXT_EDITOR' and context.space_data.text:
            context.space_data.text.write(self.emoji)
        return {'FINISHED'}


# Search button class
class TEXT_OT_manual_search(bpy.types.Operator):
    bl_idname = "frameflow.manual_search"
    bl_label = "Search"
    bl_description = "Search emojis"

    def execute(self, context):
        # Force panel redraw only when button is clicked
        for region in context.area.regions:
            if region.type == 'UI':
                region.tag_redraw()
        return {'FINISHED'}


# Define classes for registration
classes = (
    TEXT_OT_emoji_search,
    TEXT_OT_insert_emoji,
    TEXT_OT_manual_search,
    TEXT_PT_EMOJI_TEXT,
)


# Registration functions
def register():
    # Register search query property
    bpy.types.Scene.emoji_search_query = bpy.props.StringProperty(
        name="Search Emojis",
        description="Search emojis by name, category, tags, or aliases",
        default="",
    )

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    # Remove search query property
    if hasattr(bpy.types.Scene, "emoji_search_query"):
        del bpy.types.Scene.emoji_search_query

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
