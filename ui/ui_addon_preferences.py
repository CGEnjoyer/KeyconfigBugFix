import bpy
from bpy.app.handlers import persistent
from ..utils.utl_keymap_editing import remove_addon_keymap_items
from ..utils.utl_addon_preferences import get_addon_name

class KeyconfigBugFixAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = get_addon_name()

    auto_remove_keys: bpy.props.BoolProperty(name="Auto Delete Addons Keys", default=False)
    menu_save_keyconfig: bpy.props.BoolProperty(name="Show Save Keyconfig", default=True)
    menu_save_keyconfig_as: bpy.props.BoolProperty(name="Show Save Keyconfig As...", default=True)
    menu_save_and_restore: bpy.props.BoolProperty(name="Show Save & Restore Keyconfig", default=True)
    menu_restore_keyconfig: bpy.props.BoolProperty(name="Show Restore All Keymaps", default=True)
    menu_remove_addon_keymap_items: bpy.props.BoolProperty(name="Show Remove All Addon Keys", default=True)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Delete all addon keys when blender launch")
        row = layout.row()
        row.prop(self, "auto_remove_keys")
        row = layout.row()
        row.operator("wm.debug_check_addon_keys")
        layout.separator()
        row = layout.row()
        row.label(text="Displaying menu items")
        row = layout.row()
        col = row.column()
        col.prop(self, "menu_save_keyconfig")
        col.prop(self, "menu_save_keyconfig_as")
        col.prop(self, "menu_save_and_restore")
        col = row.column()
        col.prop(self, "menu_restore_keyconfig")
        col.prop(self, "menu_remove_addon_keymap_items")


@persistent
def kc_fix_load_handler(dummy):
    try:
        if bpy.context.preferences.addons[get_addon_name()].preferences['auto_remove_keys']:
            remove_addon_keymap_items()
    except:
        pass


classes = (KeyconfigBugFixAddonPreferences,)


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.app.handlers.load_post.append(kc_fix_load_handler)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    bpy.app.handlers.load_post.remove(kc_fix_load_handler)