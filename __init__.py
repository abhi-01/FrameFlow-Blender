from . import frame_flow_1
from . import EmojiText
from . import EmojiText_sub_panels


# Need to import it separately to register the property group for language dropdown.
from . import Help_Settings_Panel


import bpy
bl_info = {
    "name": "Frame Flow Beta",
    "author": "Abhishek Kumar",
    "version": (1, 0),
    "blender": (4, 3, 0),
    "location": "Node Editor > Sidebar > Node",
    "description": "Advanced Node Frame Add-on for Blender",
    "category": "Node",
}


# Create a tuple of classes from both modules
classes = (
    *frame_flow_1.classes,  # Unpack frame_flow_1 classes
    *EmojiText.classes,       # Unpack EmojiText classes
    *EmojiText_sub_panels.classes  # Unpack EmojiText_sub_panels classes
)


def register():
    # Register the language property in scene
    bpy.types.Scene.emoji_selected_language = bpy.props.StringProperty(
        name="Emoji Language",
        description="Selected language for emoji names",
        default="en"
    )
    EmojiText_sub_panels.init()  # This now registers both properties
    for cls in classes:
        bpy.utils.register_class(cls)

    # For Language dropdowns
    bpy.types.Scene.language_options_dropdown = bpy.props.PointerProperty(
        type=Help_Settings_Panel.LanguageOptionDropDown)


def unregister():
    # Unregister the property
    if hasattr(bpy.types.Scene, "emoji_selected_language"):
        del bpy.types.Scene.emoji_selected_language
    EmojiText_sub_panels.cleanup()  # This cleans up both properties
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.language_options_dropdown


if __name__ == "__main__":
    register()
