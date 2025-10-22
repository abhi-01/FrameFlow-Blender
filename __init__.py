from . import frame_flow_1
from . import EmojiText
from . import EmojiText_sub_panels
from . import Editor_text_format

# Need to import it separately to register the property group for language dropdown.
from . import Help_Settings_Panel


import bpy
bl_info = {
    "name": "Frame Flow Beta",
    "author": "Abhishek Kumar",
    "version": (1, 4, 0),
    "blender": (4, 3, 0),
    "location": "Node Editor > Sidebar > Node",
    "description": "Advanced Node Frame Add-on for Blender",
    "category": "Node",
}


# Create a tuple of classes from both modules
classes = (
    *frame_flow_1.classes,  # Unpack frame_flow_1 classes
    *EmojiText.classes,       # Unpack EmojiText classes
    *EmojiText_sub_panels.classes,  # Unpack EmojiText_sub_panels classes
    *Editor_text_format.classes,  # Unpack Editor_text_format classes
    *Help_Settings_Panel.classes  # Other classes from Help_Settings_Panel
)


def register():
    # Register all classes first.
    for cls in classes:
        bpy.utils.register_class(cls)

    # This registers both properties, emoji_active_category and emoji_search_query
    EmojiText_sub_panels.init()

    # Register the emoji_selected_language property
    bpy.types.Scene.emoji_selected_language = bpy.props.StringProperty(
        name="Emoji Language",
        description="Selected language for emoji names",
        default="en"
    )

    # For Language dropdowns
    bpy.types.Scene.language_options_dropdown = bpy.props.PointerProperty(
        type=Help_Settings_Panel.LanguageOptionDropDown)


def unregister():

    # Delete properties FIRST
    if hasattr(bpy.types.Scene, "emoji_selected_language"):
        del bpy.types.Scene.emoji_selected_language

    if hasattr(bpy.types.Scene, "language_options_dropdown"):
        del bpy.types.Scene.language_options_dropdown

        # Cleanup emoji sub-panels properties
    EmojiText_sub_panels.cleanup()

    # THEN unregister classes
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
