# FrameFlow (Beta) — Smarter Frames for Blender’s Node Editor

>  **Now in Free Beta!**  
> FrameFlow is a powerful Blender add-on that redefines node organization — add **annotated frames**, **multiline comments**, and **emoji support** to your node setups.  
> The **stable version** will be released soon on Blender Market and Gumroad.

---

## Features

- **Smart Node Frames** — neatly group and label nodes  
- **Multiline Comments** — describe your setups clearly  
- **Emoji & Unicode Support** — make notes expressive  
- **Customizable Styles** — adjust font, size, color, and padding  
- **Quick Workflow** — add frames instantly with shortcuts  
- Perfect for complex node setups, tutorials, and procedural systems

---

##  Installation

1. Download the latest `.zip` file from,    
[Gumroad](https://abhishek3d.gumroad.com/l/frameflow)
2. or simply srag and drop from:  
[Blender Official Extension's website](https://extensions.blender.org/approval-queue/frameflowblender/)  

🧠 *Tip:* You can remove any previous FrameFlow version before installing a new one.

**Gumroad Installtion**
In Blender:
   - Open **Edit → Preferences → Add-ons**
   - Click **Install from disk**
   - Select the downloaded `.zip`
   - Enable **FrameFlow** from the list

##  Usage

1. Open a **Shader Node Editor** (Support for Geometry and Compositor will be updated soon!!)
2. Press N --> 
3. Go to the **FrameFlow** tab
4. To create a frame or comment:
   - Use the **Create Frame ➕** button

5. To create a frame for a node or nodes:
   - Select your node or nodes
   - Use the **Insert Frame ☐** button
6. A frame will be created at the mouse cursor location.
7. Click on the **Open Text Editor** button to open the text editor.
8. The editor will have a **Editor Ⓕ** tab.
9. Use the search bar to search for emojis or unicode characters.
10. Or manually select from the categories below.
11. Click on any emoji or unicode character to copy it to the clipboard.
12. You can change the text format to bold or italic using the buttons **🅱️ Bold Live** and **𝑰 Italic Live**.
13. You can use the editor just like any text editor to add multiline text.
14. Use emojis like:
   - 🌲 for generators
   - ⚙️ for controls
15. And many more to make your notes and frames expressive and fun!
16. To edit the following frame properties, You do these just as you would with any regular frame node in Blender:
   
   - **Name**, **label** and **color**
   select the frame and go to the **Node** tab in the sidebar (N key) and adjust the properties under **Node** --->
   The **label** will be shown at the top of the frame in the node editor.-->
   The **name** is the internal name of the frame and will be shown in the outliner.-->
   The **color** will change the frame color.

   - **Font Size**
   select the frame and go to the **Node** tab in the sidebar (N key) and adjust the properties under **Properties**

   - **Size**
   select the frame and click on the boundary of the frame and drag to resize.

17. Each frame creation results in a data block named **active_frame_name_USER_Data_Block**. This stores your text and formatting.
any frame created via FrameFlow will have data block ending with **_USER_Data_Block**. You can change it if you want.

18. All data blocks are saved automatically, you do not need to save them manually.

19. To delete a frame and its data block, simply delete the frame node. The data block will be deleted automatically.

20. Still got queries?  [Open an issue](https://github.com/abhi-01/FrameFlow-Blender/issues) on GitHub.

21. Discord Server coming Soon!!

22. For more help see these options in the text editor:
    
    <img width="344" height="409" alt="image" src="https://github.com/user-attachments/assets/2053e9de-8c4f-4fc2-b074-552a1eba5f64" />


