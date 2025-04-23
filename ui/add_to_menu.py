import bpy


def menu_func(self, context):
    self.layout.separator()
    self.layout.operator("wm.save_current_keyconfig", text="Save Keyconfig").keymaps_restore = False
    self.layout.operator("wm.save_current_keyconfig_as", text="Save Keyconfig As...")
    self.layout.operator("wm.save_current_keyconfig", text="Save & Restore Keyconfig").keymaps_restore = True
    self.layout.separator()
    self.layout.operator("wm.restore_keyconfig", text="Restore All Keymaps")
    self.layout.operator("wm.remove_addon_keymap_items", text="Remove All Addon Keys")


def register():
    bpy.types.USERPREF_MT_save_load.append(menu_func)
def unregister():
    bpy.types.USERPREF_MT_save_load.remove(menu_func)