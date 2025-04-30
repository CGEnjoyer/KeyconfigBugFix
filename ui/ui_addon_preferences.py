import bpy
from bpy.app.handlers import persistent
from ..utils.utl_keymap_editing import remove_addon_keymap_items
from ..utils.utl_addon_preferences import get_addon_name

class KeyconfigBugFixAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = get_addon_name()

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