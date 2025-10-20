import bpy


# It creates a boiler plate format of 'base classes' for emoji 'operators' and 'panels'.
# This was created after the reviewer on Blender extension suggested to reduce code duplication.
# All the classes are pretty self explanatory.

# Most important class, inserts the emoji into the text editor
class BaseEmojiInsertOperator(bpy.types.Operator):
    """Base class for emoji insert operators"""

    emoji: bpy.props.StringProperty(
        name="Emoji",
        description="The emoji character to insert",
        default="📱"
    )

    tooltip: bpy.props.StringProperty(
        name="Tooltip",
        description="Hover description for the emoji",
        default=""
    )

    @classmethod
    def description(cls, context, properties):
        return properties.tooltip if properties.tooltip else "Insert emoji into text editor"

    def execute(self, context):
        if context.space_data.type == 'TEXT_EDITOR' and context.space_data.text:
            context.space_data.text.write(self.emoji)
        return {'FINISHED'}


# Pretty simple and straight forward. No Brainer.
class BaseEmojiCategoryOperator(bpy.types.Operator):
    """Base class for all the emoji category operators"""
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_options = {'REGISTER', 'UNDO'}

    # Override in subclasses
    category_name = ""

    def execute(self, context):
        context.scene.emoji_active_category = self.category_name
        return {'FINISHED'}


# Pretty straightforward panel class for each emoji category
# Goes through the language settings and shows the emoji names accordingly.
class BaseEmojiPanel(bpy.types.Panel):
    """Base class for all the emoji category panels"""
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_parent_id = "TEXT_PT_EMOJI_CATEGORIES"

    # Overriding in subclasses
    category_key = ""
    emoji_data = {}
    insert_operator = ""

    @classmethod
    def poll(cls, context):
        # Each sub panel has its own unique key.
        return context.scene.emoji_active_category == cls.category_key

    def draw(self, context):
        # Layout emojis in a grid layout of four columns
        layout = self.layout
        layout.label(text=f"Found {len(self.emoji_data)} emojis")
        grid = layout.grid_flow(columns=4, align=True)

        # English is set as default language. Here the data is collected through the dropdown options
        # from the settings option of Language.
        selected_language = bpy.context.scene.language_options_dropdown.languages
        for emoji, data in self.emoji_data.items():
            props = grid.operator(self.insert_operator, text=emoji)
            props.emoji = emoji
            if isinstance(data, dict):
                emoji_name = data.get("names", {}).get(selected_language,
                                                       data.get("names", {}).get("en", "Unknown Emoji"))
                tooltip_text = f"{emoji_name}"
                props.tooltip = tooltip_text
            else:
                props.tooltip = str(data)
