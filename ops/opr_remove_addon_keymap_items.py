import bpy
from ..utils.utl_keymap_editing import remove_addon_keymap_items


class WM_OT_RemoveAddonKeymapItems(bpy.types.Operator):
    bl_idname = "wm.remove_addon_keymap_items"
    bl_label = "Remove All Addon Keys"
    bl_description = "Remove All Addon Keymap Items (until restart)"

    blender_version = int((str(bpy.app.version[0])[:1]) + (str(bpy.app.version[1])[:1]))

    def execute(self, context):
        remove_addon_keymap_items()
        return {'FINISHED'}

    def invoke(self, context, event):
        if self.blender_version >= 41:
            message = context.window_manager.invoke_confirm(self, event, title="Remove All Addon Keys?",
                                                            message="Remove All Addon Keymap Items (until restart)",
                                                            confirm_text="Remove", icon='WARNING')
        else:
            message = context.window_manager.invoke_confirm(self, event)
        return message


classes = (WM_OT_RemoveAddonKeymapItems,)
register, unregister = bpy.utils.register_classes_factory(classes)