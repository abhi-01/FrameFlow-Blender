import bpy

"""This module contains the Help & Settings panels for both Text Editor and Node Editor.
It also includes the language selection dropdown for emojis."""


# Language dropdown to select language for the addon.
# This language option is based on the Python Emoji package:
# https://pypi.org/project/emoji/
# This has to registered (and unregistered) via the __init__.py file.
class LanguageOptionDropDown(bpy.types.PropertyGroup):
    languages: bpy.props.EnumProperty(
        name="Languages",
        description="Select Language",
        items=[
            ('en', "English (Default)", "English"),
            ('es', "Spanish", "Spanish"),
            ('pt', "Portuguese", "Portuguese"),
            ('it', "Italian", "Italian"),
            ('fr', "French", "French"),
            ('de', "German", "German"),
            ('fa', "Farsi/Persian", "Farsi/Persian"),
            ('id', "Indonesian", "Indonesian"),
            ('zh', "Simplified Chinese", "Simplified Chinese"),
            ('ja', "Japanese", "Japanese"),
            ('ko', "Korean", "Korean"),
            ('ru', "Russian", "Russian"),
            ('ar', "Arabic", "Arabic"),
            ('tr', "Turkish", "Turkish"),
        ],
        default='en'
    )


# Global variable to store the selected language
user_selected_language = 'en'


# BASE CLASS - contains all the common UI logic
class BaseHelpSettingsPanel:
    """Base class for Help & Settings panels - inherit from this in different editors"""
    bl_label = "Help"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_common_buttons(self, layout):
        """Common help buttons for both panels"""
        # Help button
        layout.separator()
        row = layout.row(align=True)

        row.operator(
            "wm.url_faq", text="FAQ \u2754").url = "https://github.com/abhi-01/FrameFlow-Blender/wiki/FAQ"

        row.operator(
            "wm.url_docs", text="Docs \U0001F4C4").url = "https://github.com/abhi-01/FrameFlow-Blender/wiki"

        row = layout.row(align=True)

        row.operator("wm.url_rate_us", text="Rate \u2B50",
                     ).url = "https://abhishek3d.gumroad.com/l/frameflow"

        row.operator("wm.url_share", text="Share \u2764",
                     ).url = "https://abhishek3d.gumroad.com/l/frameflow"

        row = layout.row(align=True)
        row.operator("wm.url_contact_us", text="Contact \U0001F4E7",
                     ).url = "mailto:abhishek.physics90@gmail.com"
        row.operator("wm.url_about_us", text="About \u2139",
                     ).url = "https://github.com/abhi-01/FrameFlow-Blender/blob/main/README.md"

        # Report bug/Raise issue
        layout.separator()
        row = layout.row(align=True)
        row.operator("wm.url_report_bug", text="Report Bug \U0001FAB2"
                     ).url = "https://github.com/abhi-01/FrameFlow-Blender/issues"


# Panel for Text Editor
class TEXT_PT_HELP_SETTINGS_PANEL(BaseHelpSettingsPanel, bpy.types.Panel):
    """Help & Settings panel in Text Editor"""
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_label = "Help"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        # Language dropdown (ONLY in Text Editor)
        row = layout.row(align=True)
        row.label(text="Set Emoji Language:")
        row = layout.row()
        lang_options = context.scene.language_options_dropdown
        row.prop(lang_options, "languages", text="")
        row.operator("language.update", text="Update")

        # Draw common buttons
        self.draw_common_buttons(layout)


# Panel for Node Editor (Shader/Geometry/Compositor)
class NODE_PT_HELP_SETTINGS_PANEL(BaseHelpSettingsPanel, bpy.types.Panel):
    """Help & Settings panel in Node Editor"""
    bl_label = "Help"
    bl_idname = "NODE_PT_frame_flow_help_settings_panel"
    bl_icon = 'FILE_FONT'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = "NODE_PT_simple_frame"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        # NO language dropdown here - only common buttons
        self.draw_common_buttons(layout)


# Simply update the global variable and scene property
def update_language(self, context):
    selected_language = context.scene.language_options_dropdown.languages
    context.scene.emoji_selected_language = selected_language
    # # Debugging print statements
    # print(f"Selected Language: {selected_language}")
    # print(f"Global User Selected Language: {user_selected_language}")


# Operator to update language selection
class LANGUAGE_OT_Update(bpy.types.Operator):
    bl_idname = "language.update"
    bl_label = "Update Language"
    bl_description = "Update the language of the emojis in the addon"

    def execute(self, context):
        update_language(self, context)
        # Force emoji panel to redraw with new language
        for area in context.screen.areas:
            if area.type in ('TEXT_EDITOR', 'NODE_EDITOR'):
                for region in area.regions:
                    if region.type == 'UI':
                        region.tag_redraw()
        return {'FINISHED'}


# Operator class of FAQ button
class FAQ_OT_Open(bpy.types.Operator):
    bl_idname = "wm.url_faq"
    bl_label = "Open URL FAQ"
    bl_description = "Open Frequently Asked Questions"

    url: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.wm.url_open(url=self.url)
        return {'FINISHED'}


# Operator class of Docs button
class DOCS_OT_Open(bpy.types.Operator):
    bl_idname = "wm.url_docs"
    bl_label = "Open Docs"
    bl_description = "Open Documentation"

    url: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.wm.url_open(url=self.url)
        return {'FINISHED'}


# Operator class of Rate Us button
class RATE_US_OT_Open(bpy.types.Operator):
    bl_idname = "wm.url_rate_us"
    # Changed from gumroad to Blender's extension page, as per the reviewer suggestion.
    bl_label = "Rate on Gumroad page"
    bl_description = "Rate Us on Gumroad"
    # bl_label = "Rate on Blender's extension page"
    # bl_description = "Rate on Blender's extension page"

    url: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.wm.url_open(url=self.url)
        return {'FINISHED'}


# Operator class of Share button
class SHARE_OT_Open(bpy.types.Operator):
    bl_idname = "wm.url_share"
    # Changed from gumroad to Blender's extension page, as per the reviewer suggestion.
    bl_label = "Share page on gumroad"
    bl_description = "Share on Gumroad"
    # bl_label = "Share the addon "
    # bl_description = "Share the addon"

    url: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.wm.url_open(url=self.url)
        return {'FINISHED'}


# Operator class of Contact Us button
class CONTACT_US_OT_Open(bpy.types.Operator):
    bl_idname = "wm.url_contact_us"
    bl_label = "open email to connect "
    bl_description = "Contact Us via Email"

    url: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.wm.url_open(url=self.url)
        return {'FINISHED'}


# Operator class of About Us button
class ABOUT_US_OT_Open(bpy.types.Operator):
    bl_idname = "wm.url_about_us"
    bl_label = "Open About Us page"
    bl_description = "About Us"

    url: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.wm.url_open(url=self.url)
        return {'FINISHED'}


# Operator class of Report Bug button
class REPORT_BUG_OT_Open(bpy.types.Operator):
    bl_idname = "wm.url_report_bug"
    bl_label = "Open Report Bug page"
    bl_description = "Report a Bug"

    url: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.wm.url_open(url=self.url)
        return {'FINISHED'}


classes = (
    LanguageOptionDropDown,
    TEXT_PT_HELP_SETTINGS_PANEL,
    NODE_PT_HELP_SETTINGS_PANEL,  # Add the Node Editor panel
    LANGUAGE_OT_Update,
    FAQ_OT_Open,
    DOCS_OT_Open,
    RATE_US_OT_Open,
    SHARE_OT_Open,
    CONTACT_US_OT_Open,
    ABOUT_US_OT_Open,
    REPORT_BUG_OT_Open
)
