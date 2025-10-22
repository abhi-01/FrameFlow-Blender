import bpy


# It creates a boiler plate format of 'base classes' for emoji 'operators' and 'panels'.
# This was created after the reviewer on Blender extension suggested to reduce code duplication.
# All the classes are pretty self explanatory.

# Most important class, inserts the emoji into the text editor
# MAKING CHANGES CAN BE RISKY.
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
        # IMPORTANT FIX: Verify we're in a valid text editor context
        # WHY --> There was an issue with emojis insertion. See, the following codes/comments.
        if not context.space_data or context.space_data.type != 'TEXT_EDITOR':
            self.report({'WARNING'}, "Must be in Text Editor")
            return {'CANCELLED'}

        txt = context.space_data.text
        if not txt:
            self.report({'WARNING'}, "No text file open")
            return {'CANCELLED'}

        # IMPORTANT FIX: Now after fixing the issue with 'bold' and 'italic' from appearing to a new line
        # instead of the cursor position, I am reusing the same logic here for emoji insertion.
        # Instead of using txt.write() which inserts text and pushes to new line,
        # reconstruct the line with emoji at the cursor position
        line = txt.current_line
        cursor_pos = txt.current_character

        # Build new line: before cursor + emoji + after cursor
        new_body = line.body[:cursor_pos] + self.emoji + line.body[cursor_pos:]
        line.body = new_body

        # Move cursor after the inserted emoji
        txt.current_character = cursor_pos + len(self.emoji)
        txt.select_end_character = txt.current_character

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
