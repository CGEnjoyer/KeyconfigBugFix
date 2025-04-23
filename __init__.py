bl_info = {
    "name": "Keyconfig Bug Fix",
    "author": "Vladimir Ilin (CGEnjoyer)",
    "version": (1, 0, 0),
    "description": "Fixes a bug where keys were duplicated when saving keyconfig",
    "location": "Preferences > Save & Load",
    "blender": (4, 2, 0),
    "category": "System",
    "warning": "Make a backup of all user settings before using",
}


import bpy
from bpy.app.handlers import persistent
from .utils.utl_keymap_editing import remove_addon_keymap_items
from .ops import (opr_debug_check_addon_keys,
                  opr_remove_addon_keymap_items,
                  opr_restore_keyconfig,
                  opr_save_current_keyconfig)
from .ui import add_to_menu


classes = []

#operators
classes.extend([opr_remove_addon_keymap_items,
                opr_restore_keyconfig,
                opr_save_current_keyconfig,
                opr_debug_check_addon_keys,])
#ui
classes.extend([add_to_menu])


class KeyconfigBugFixAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    auto_remove_keys: bpy.props.BoolProperty(name="Auto Delete Addons Keys")

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Delete all addon keys when blender launch")
        row = layout.row()
        row.prop(self, "auto_remove_keys")
        row = layout.row()
        row.operator("wm.debug_check_addon_keys")


@persistent
def kc_fix_load_handler(dummy):
    try:
        if bpy.context.preferences.addons[__package__].preferences['auto_remove_keys']:
            remove_addon_keymap_items()
    except:
        pass


def register():
    for c in classes:
        c.register()
    bpy.utils.register_class(KeyconfigBugFixAddonPreferences)
    bpy.app.handlers.load_post.append(kc_fix_load_handler)

def unregister():
    for c in reversed(classes):
        c.unregister()
    bpy.utils.unregister_class(KeyconfigBugFixAddonPreferences)
    bpy.app.handlers.load_post.remove(kc_fix_load_handler)