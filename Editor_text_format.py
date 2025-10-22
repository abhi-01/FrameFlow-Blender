import bpy


# Unicode Character Mapping
# This functions maps the english alphabet and numbers to their bold and italic Unicode equivalents.
def generate_style_maps():
    # Bold A–Z, a–z, 0–9
    bold = {
        **{chr(i): chr(0x1D400 + (i - 0x41)) for i in range(0x41, 0x5B)},  # A–Z
        **{chr(i): chr(0x1D41A + (i - 0x61)) for i in range(0x61, 0x7B)},  # a–z
        **{chr(i): chr(0x1D7CE + (i - 0x30)) for i in range(0x30, 0x3A)},  # 0–9
    }

    # Italic A–Z (contiguous)
    italic_upper = {chr(i): chr(0x1D434 + (i - 0x41))
                    for i in range(0x41, 0x5B)}

    # The reason for the gap is that Unicode does not have a separate italic character for 'h'.
    # It gets confused with the Planck constant symbol (ℎ, U+210E) and yields incorrect rendering for the
    # alphabet 'h' in italic style..
    # Italic a–z (gap at h)
    italic_lower = {}
    italic_lower.update({chr(i): chr(0x1D44E + (i - 0x61))
                        for i in range(0x61, 0x68)})  # a–g
    italic_lower["h"] = "\u210E"  # ℎ
    italic_lower.update({chr(i): chr(0x1D456 + (i - 0x69))
                        for i in range(0x69, 0x7B)})  # i–z

    italic = {**italic_upper, **italic_lower}
    return bold, italic


# Generate the maps once
BOLD_MAP, ITALIC_MAP = generate_style_maps()


def stylize_text(text, style='bold'):
    mapping = BOLD_MAP if style == 'bold' else ITALIC_MAP
    return ''.join(mapping.get(ch, ch) for ch in text)


# State handling
def get_live_mode(context):
    wm = context.window_manager
    if "unicode_text_style_mode" not in wm:
        wm["unicode_text_style_mode"] = "none"
    return wm["unicode_text_style_mode"]


def set_live_mode(context, mode):
    context.window_manager["unicode_text_style_mode"] = mode


# # # IMPORTANT: DO NOT DELETE THIS CODE BLOCK
# # # Operator – Manual Apply, user selects text and click button.
# # # Leaving it for now, in case needed in future.

# # class TEXT_OT_style_unicode(bpy.types.Operator):
# #     bl_idname = "text.style_unicode"
# #     bl_label = "Stylize Text (Unicode)"
# #     bl_options = {'REGISTER', 'UNDO'}

# #     style: bpy.props.EnumProperty(
# #         name="Style",
# #         items=[
# #             ('bold', "Bold", "Apply bold Unicode characters"),
# #             ('italic', "Italic", "Apply italic Unicode characters"),
# #         ],
# #         default='bold',
# #     )

# #     def execute(self, context):
# #         text = context.space_data.text
# #         if not text:
# #             self.report({'WARNING'}, "No text open.")
# #             return {'CANCELLED'}

# #         line = text.current_line
# #         c1, c2 = sorted((text.current_character, text.select_end_character))
# #         body = line.body

# #         if c1 == c2:
# #             self.report({'WARNING'}, "Select text first.")
# #             return {'CANCELLED'}

# #         try:
# #             selected = body[c1:c2]
# #             styled = stylize_text(selected, self.style)
# #             new_body = body[:c1] + styled + body[c2:]
# #             line.body = new_body
# #             text.current_character = c1 + len(styled)
# #             text.select_end_character = text.current_character
# #             return {'FINISHED'}
# #         except Exception as e:
# #             self.report({'ERROR'}, str(e))
# #             return {'CANCELLED'}


# Operator – Live Typing Mode
class TEXT_OT_live_style(bpy.types.Operator):
    bl_idname = "text.live_style"
    bl_label = "Live Unicode Typing"
    bl_options = {'REGISTER'}
    bl_description = "Apply Bold or Italic styles to text"

    style: bpy.props.EnumProperty(
        name="Style",
        items=[('bold', "Bold", ""), ('italic', "Italic", "")],
    )

    _timer = None
    _last_len = 0
    _last_line_index = -1  # NEW: Track which line we're on
    _last_cursor_pos = 0    # NEW: Track cursor position

    def modal(self, context, event):
        if event.type == 'TIMER':
            if get_live_mode(context) != self.style:
                self.cancel(context)
                return {'CANCELLED'}

            txt = context.space_data.text
            if not txt:
                return {'PASS_THROUGH'}

            line = txt.current_line
            body = line.body

            # Get current line index
            try:
                current_line_index = txt.lines[:].index(line)
            except:
                current_line_index = -1

            current_cursor_pos = txt.current_character

            # IMPORTANT FIX: This was creating issues whenever the user switched lines, it would keep printing same text with each click..
            # Reset tracking when user changes lines or moves cursor backward
            if (current_line_index != self._last_line_index or
                    current_cursor_pos < self._last_cursor_pos):
                self._last_len = len(body)
                self._last_line_index = current_line_index
                self._last_cursor_pos = current_cursor_pos
                return {'PASS_THROUGH'}

            # Detect new text added since last check (only at cursor position)
            if len(body) > self._last_len and current_cursor_pos > self._last_cursor_pos:
                # Calculate how many new characters were added
                new_chars_count = current_cursor_pos - self._last_cursor_pos

                if new_chars_count > 0:
                    # Get only the newly typed characters
                    start_pos = self._last_cursor_pos
                    end_pos = current_cursor_pos
                    new_text = body[start_pos:end_pos]

                    styled = stylize_text(new_text, self.style)

                    # Replace only the new text by reconstructing the line
                    try:
                        # Build new line: before + styled + after
                        new_body = body[:start_pos] + styled + body[end_pos:]
                        line.body = new_body

                        # Position cursor after the styled text
                        txt.current_character = start_pos + len(styled)
                        txt.select_end_character = txt.current_character

                        # Update tracking
                        self._last_len = len(new_body)
                        self._last_cursor_pos = txt.current_character
                    except Exception:
                        pass
            else:
                # Just update tracking without modification
                self._last_len = len(body)
                self._last_cursor_pos = current_cursor_pos

        return {'PASS_THROUGH'}

    def cancel(self, context):
        if self._timer:
            context.window_manager.event_timer_remove(self._timer)
            self._timer = None

    def execute(self, context):
        wm = context.window_manager
        current_mode = get_live_mode(context)

        # FIX: cleanly stop previous live mode before switching
        if current_mode != "none" and current_mode != self.style:
            set_live_mode(context, "none")
            for window in wm.windows:
                for area in window.screen.areas:
                    if area.type == 'TEXT_EDITOR':
                        area.tag_redraw()

        # Normal toggle logic
        if current_mode == self.style:
            set_live_mode(context, "none")
            self.report({'INFO'}, f"{self.style.title()} mode OFF")
            return {'CANCELLED'}

        set_live_mode(context, self.style)
        txt = context.space_data.text
        if txt:
            self._last_len = len(txt.current_line.body)
            try:
                self._last_line_index = txt.lines[:].index(txt.current_line)
            except:
                self._last_line_index = -1
            self._last_cursor_pos = txt.current_character

        self._timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)
        self.report({'INFO'}, f"{self.style.title()} mode ON")
        return {'RUNNING_MODAL'}


# Buttons Panel
class TEXT_PT_unicode_style(bpy.types.Panel):
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Editor Ⓕ"
    bl_label = "Text Styles"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager
        mode = get_live_mode(context)
        layout.label(text="Click to select:")
        col = layout.column(align=True)
        b = col.operator("text.live_style", text="🅱️ Bold Live",
                         depress=(mode == 'bold'))
        b.style = 'bold'
        i = col.operator("text.live_style", text="𝑰 Italic Live",
                         depress=(mode == 'italic'))
        i.style = 'italic'


classes = (TEXT_OT_live_style, TEXT_PT_unicode_style)
