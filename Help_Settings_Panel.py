import bpy


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
            # Add more languages as needed
        ],
        default='en'
    )


# Global variable to store the selected language
user_selected_language = 'en'


# Panel class that contains the help and settings options.
class TEXT_PT_HELP_SETTINGS_PANEL(bpy.types.Panel):

    bl_space_type = 'TEXT_EDITOR'  # Changed from VIEW_3D
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_label = "Help"
    bl_options = {'DEFAULT_CLOSED'}  # Start closed

    def draw(self, context):

        layout = self.layout

        row = layout.row(align=True)

        # Language dropdown
        row.label(text="Set Emoji Language:")
        row = layout.row()
        lang_options = context.scene.language_options_dropdown
        row.prop(lang_options, "languages", text="")
        row.operator("language.update", text="Update")

        # Settings Button
        # To be added. May contain default color, text of frames, default size of text editor, default name of text block, etc.

        # Help button
        # separator for better looking
        layout.separator()
        # The "align=True" keeps the button intact and pretty, instead of a gap between them.
        row = layout.row(align=True)

        # row.operator("wm.url_open", text="FAQ",
        #              ).url = "https://github.com/abhi-01/FrameFlow"
        row.operator(
            "wm.url_faq", text="FAQ \u2754").url = "https://github.com/abhi-01/FrameFlow-Blender/blob/main/README.md"

        # row.operator("wm.url_open", text="Docs",
        #              ).url = "https://github.com/abhi-01/FrameFlow"

        row.operator(
            "wm.url_docs", text="Docs \U0001F4C4").url = "https://github.com/abhi-01/FrameFlow-Blender/wiki"
        # # The "align=True" keeps the button intact and pretty, instead of a gap between them.
        row = layout.row(align=True)
        # row.label(text="Contact / Rate Us:")

        row.operator("wm.url_rate_us", text="Rate \u2B50",
                     ).url = "https://abhishek3d.gumroad.com/l/frameflow"
        row.operator("wm.url_share", text="Share \u2764",
                     ).url = "https://abhishek3d.gumroad.com/l/frameflow"

        # The "align=True" keeps the button intact and pretty, instead of a gap between them.
        row = layout.row(align=True)
        row.operator("wm.url_contact_us", text="Contact \U0001F4E7",  # not "Contact Us", as it got hidden dur to long name
                     ).url = "mailto:abhishek.physics90@gmail.com"
        row.operator("wm.url_about_us", text="About \u2139",  # Not "About Us", as it implies a big team.
                     ).url = "https://github.com/abhi-01/FrameFlow"


# Update language option button
def update_language(self, context):
    selected_language = context.scene.language_options_dropdown.languages
    # global user_selected_language
    # user_selected_language = selected_language
    # Store in scene properties instead of global variable
    context.scene.emoji_selected_language = selected_language
    print(f"Selected Language: {selected_language}")
    print(f"Global User Selected Language: {user_selected_language}")


class LANGUAGE_OT_Update(bpy.types.Operator):
    bl_idname = "language.update"
    bl_label = "Update Language"
    bl_description = "Update the language of the emojis in the addon"

    def execute(self, context):
        update_language(self, context)
        # Force emoji panel to redraw with new language
        for area in context.screen.areas:
            if area.type == 'TEXT_EDITOR':
                for region in area.regions:
                    if region.type == 'UI':
                        region.tag_redraw()
        return {'FINISHED'}


# print(
#     f"Outside Global User Selected Language at load: {user_selected_language}")


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
    bl_label = "Rate on Gumroad page"
    bl_description = "Rate Us on Gumroad"

    url: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.wm.url_open(url=self.url)
        return {'FINISHED'}


# Operator class of Share button
class SHARE_OT_Open(bpy.types.Operator):
    bl_idname = "wm.url_share"
    bl_label = "Share page on gumroad"
    bl_description = "Share on Gumroad"

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
