import bpy


# # A panel that creates a frame node in the shader editor with a pop up for text editor.

# # As of now I have removed the location, size, font size and color properties.
# # Out of these 4 font size and color are already provided by Blender.

# # So, I will keep the "open editor" option as of now.

# Features to add:
# # 1. Add color buttons for specific nodes?

# # 2. Add backups?


# This data block list will keep track of all the text blocks created by FrameFlow,
# for future use of keeping back up feature.
data_block_list = []


# Main Panel class
class SimpleFramePanel(bpy.types.Panel):
    # Just FrameFlow and not FrameFlow Panel, to keep it minimalistic.
    bl_label = "FrameFlow Ⓕ"
    bl_idname = "NODE_PT_simple_frame"
    bl_icon = 'FILE_FONT'

    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Node"
    bl_options = {'DEFAULT_CLOSED'}

    # It seems Blender expects the draw method to have two parameters: self and context.
    # The context parameter provides access to the current state of Blender, including the active object,
    def draw(self, context):
        layout = self.layout

        row = layout.row()

        # Simply creates a frame node in the shader editor where the mouse cursor is.
        row.operator("node.add_frame_node", text="Create Frame  ➕")

       # This inserts a frame node around the selected node. it contains a additional frame by default, such that
       # the user can add notes to it without having to create a new frame node and then linking it to a text block.
        row = layout.row()
        row.operator("node.join_frame_node", text="Insert Frame ☐")

        # This button opens the text editor in a new window
        # and links the text block inside the frame node to the text editor.
        row = layout.row()
        row.operator("wm.open_text_editor",
                     text="Open Text Editor \U0001F5D2")

        # Help, About, Contact, Rate Us section
        # As of now just help is there, to keep it minimalistic.
        layout.separator()
        row = layout.row()
        row.operator("wm.url_open", text="Help❔",
                     ).url = "https://www.blender.org/support/"


# Operator to add a frame node where the mouse cursor is.
class AddFrameNodeOperator(bpy.types.Operator):
    bl_idname = "node.add_frame_node"
    bl_label = "Add Frame Node"
    bl_description = "Create a frame near the mouse cursor"  # <-- Tooltip text

    def execute(self, context):
        area = context.area
        region = context.region
        space = context.space_data

        # Check to ensure that the user is in the node editor and has a material.
        if not area or area.type != 'NODE_EDITOR':
            self.report({'WARNING'}, "Switch to a node editor")
            return {'CANCELLED'}

        obj = context.object
        if not obj or not obj.active_material:
            self.report({'WARNING'}, "Select object with material")
            return {'CANCELLED'}

        # Reference to the selected material's node tree
        ntree = obj.active_material.node_tree

        # Compute view center in node space
        v2d = region.view2d
        # region_to_view gives node-space from region coords
        vx = (region.width) * 0.5
        vy = (region.height) * 0.5
        center_x, center_y = v2d.region_to_view(vx, vy)

        # Create frame
        frame = ntree.nodes.new('NodeFrame')
        frame.width = 150
        frame.height = 150
        frame.location = (center_x - frame.width * 0.5,
                          center_y - frame.height * 0.5)

        # Style & text block
        frame.name = "FrameFlow Block"
        frame.label = "Hello from FrameFlow!"
        frame.use_custom_color = True
        frame.color = (0.144, 0.432, 1)
        tb = bpy.data.texts.new(name=f"{frame.name}_text")
        frame.text = tb
        # Keep track of created text blocks, for future use of keeping back up feature.
        data_block_list.append(tb)
        ntree.nodes.active = frame

        return {'FINISHED'}


# Operator to insert frame in existing frame
class InsertFrameOperator(bpy.types.Operator):
    bl_idname = "node.join_frame_node"
    bl_label = "Insert Frame"
    bl_description = "Insert a frame around the selected node"

    def execute(self, context):

        area = context.area

        # Checks to ensure that the user is in the node editor and has a material.
        if not area or area.type != 'NODE_EDITOR':
            self.report({'WARNING'}, "Switch to a node editor")
            return {'CANCELLED'}

        obj = context.object
        if not obj or not obj.active_material:
            self.report({'WARNING'}, "Select object with material")
            return {'CANCELLED'}

        material = bpy.context.object.active_material
        node_tree = material.node_tree

        # Check if user has selected a node (or nodes) , if yes then use that node's location and
        # size to place the frame node around it.

        # active_node = node_tree.nodes.active
        check_node_bool = False
        for node in node_tree.nodes:
            if node.select:
                active_node = node
                check_node_bool = True
                break

        # if active_node:
        if check_node_bool:
            print("active node is ", active_node)

            location_x = active_node.location[0] - (active_node.width + 10)

            location_y = active_node.location[1]
            frame_node = node_tree.nodes.new(type='NodeFrame')
            frame_node.location = (location_x, location_y)
            frame_node.width = active_node.width + 5
            frame_node.height = active_node.height
            # Set default properties for the frame node
            frame_node.use_custom_color = True  # Enable custom color check box
            # Set a custom color (blue here)
            frame_node.color = (0.2, 0.2, 0.8)
            bpy.ops.node.join()

        else:
            self.report({'WARNING'}, "Please select a node")

        return {'FINISHED'}


# Operator to open text editor in new window
class OpenTextEditorOperator(bpy.types.Operator):
    bl_idname = "wm.open_text_editor"
    bl_label = "Open Text Editor"
    bl_description = "Open text editor in new window with data block linked to frame node"

    def execute(self, context):

        # Store the original area type before creating new window
        original_area = context.area.type

        # Check to ensure that the user is in the node editor, has selected an object and has a material.
        if original_area != 'NODE_EDITOR':
            self.report({'WARNING'}, "Please switch to the Shader Editor")
            return {'CANCELLED'}

        # Then check if there's an active object
        if not context.object:
            self.report({'WARNING'}, "Please select an object")
            return {'CANCELLED'}

        if not context.object.active_material:
            self.report({'WARNING'}, "Please select a material")
            return {'CANCELLED'}

        # Resizing the window's size and changing area type to text editor.

        # It seems it is needed to modify render window's settings first in order to open the text editor.
        render_region = bpy.context.scene.render
        render_region.resolution_x = 720
        render_region.resolution_y = 510
        render_region.resolution_percentage = 100

        # Modify preferences, ensures that the new window opens as a normal window and not as a
        # full screen or any other type.
        # Ensuring the render display type is set to 'WINDOW'
        prefs_windows = bpy.context.preferences
        prefs_windows.view.render_display_type = "WINDOW"

        # This opens a new image render window
        bpy.ops.render.view_show("INVOKE_DEFAULT")

        # Changing the area type to text editor
        # Need to add a fallback in case the new window is not the last one
        # but for now it works fine
        area_selected = bpy.context.window_manager.windows[-1].screen.areas[0]
        area_selected.type = "TEXT_EDITOR"

        # Setting the text block as the active text in the editor, starts here.
        material = bpy.context.object.active_material
        node_tree = material.node_tree
        active_frame = node_tree.nodes.active
        print("active frame is ", active_frame)

        # Check for active frame first
        if not active_frame:
            self.report({'WARNING'}, "No active frame selected")
            return {'CANCELLED'}

        if active_frame.type != 'FRAME':
            self.report({'WARNING'}, "Selected node is not a frame")
            return {'CANCELLED'}

        # Now handling existing text blocks, if text block exists, link it, else create new one
        if active_frame.text:
            area_selected.spaces.active.text = active_frame.text
        else:
            # Create a text block and link it with the frame node
            text_block = bpy.data.texts.new(
                name=f"{active_frame.name}_USER_Data_Block")
            active_frame.text = text_block
            data_block_list.append(text_block)
            area_selected.spaces.active.text = text_block

        return {'FINISHED'}


classes = [SimpleFramePanel, AddFrameNodeOperator,
           InsertFrameOperator, OpenTextEditorOperator]
