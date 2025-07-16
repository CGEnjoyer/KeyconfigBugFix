import bpy
from ..utils.utl_addon_preferences import get_preferences


def menu_add_draw_USERPREF_MT_save_load(self, context):
    prefs = get_preferences()

    if prefs.menu_save_keyconfig or prefs.menu_save_keyconfig_as or prefs.menu_save_and_restore:
        self.layout.separator()

    if prefs.menu_save_keyconfig:
        self.layout.operator("wm.save_current_keyconfig", text="Save Keyconfig").keymaps_restore = False
    if prefs.menu_save_keyconfig_as:
        self.layout.operator("wm.save_current_keyconfig_as", text="Save Keyconfig As...")
    if prefs.menu_save_and_restore:
        self.layout.operator("wm.save_current_keyconfig", text="Save & Restore Keyconfig").keymaps_restore = True

    if prefs.menu_restore_keyconfig or prefs.menu_remove_addon_keymap_items:
        self.layout.separator()

    if prefs.menu_restore_keyconfig:
        self.layout.operator("wm.restore_keyconfig", text="Restore All Keymaps")
    if prefs.menu_remove_addon_keymap_items:
        self.layout.operator("wm.remove_addon_keymap_items", text="Remove All Addon Keys")
    if prefs.menu_restore_addon_keymap_items:
        self.layout.operator("wm.restore_addon_keymap_items", text="Restore All Addon Keys")


def register():
    bpy.types.USERPREF_MT_save_load.append(menu_add_draw_USERPREF_MT_save_load)
def unregister():
    bpy.types.USERPREF_MT_save_load.remove(menu_add_draw_USERPREF_MT_save_load)