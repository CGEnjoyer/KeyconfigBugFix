bl_info = {
    "name": "Keyconfig Bug Fix",
    "author": "Vladimir Ilin (CGEnjoyer)",
    "version": (2, 0, 0),
    "description": "Fixes a bug where keys were duplicated when saving keyconfig",
    "location": "Preferences > Save & Load",
    "blender": (2, 80, 0),
    "category": "System",
}


from .ops import (opr_remove_addon_keymap_items,
                  opr_restore_keyconfig,
                  opr_save_current_keyconfig,
                  opr_apply_and_save_preset)
from .ui import (ui_addon_preferences,
                 ui_menu_add)


classes = []

#addn preferences
classes.extend([ui_addon_preferences])
#operators
classes.extend([opr_remove_addon_keymap_items,
                opr_restore_keyconfig,
                opr_save_current_keyconfig,
                opr_apply_and_save_preset])
#ui
classes.extend([ui_menu_add])


def register():
    for c in classes:
        c.register()


def unregister():
    for c in reversed(classes):
        c.unregister()