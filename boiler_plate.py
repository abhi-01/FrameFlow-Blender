import bpy


# Boiler plate base classes for emoji operators and panels
# This was created after the reviewer on Blender extension suggested to reduce code duplication.

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


class BaseEmojiCategoryOperator(bpy.types.Operator):
    """Base class for emoji category operators"""
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_options = {'REGISTER', 'UNDO'}

    # Override in subclasses
    category_name = ""

    def execute(self, context):
        context.scene.emoji_active_category = self.category_name
        return {'FINISHED'}


class BaseEmojiPanel(bpy.types.Panel):
    """Base class for emoji category panels"""
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_parent_id = "TEXT_PT_EMOJI_CATEGORIES"

    # Override in subclasses
    category_key = ""
    emoji_data = {}
    insert_operator = ""

    @classmethod
    def poll(cls, context):
        return context.scene.emoji_active_category == cls.category_key

    def draw(self, context):
        layout = self.layout
        layout.label(text=f"Found {len(self.emoji_data)} emojis")
        grid = layout.grid_flow(columns=4, align=True)

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
