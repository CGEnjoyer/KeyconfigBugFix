import bpy
from ..utils.utl_keymap_editing import restore_all_keymaps


class WM_OT_RestoreKeyconfig(bpy.types.Operator):
    bl_idname = "wm.restore_keyconfig"
    bl_label = "Restore All Keymaps"
    bl_description = "Restore all keymaps to saved state"

    blender_version = int((str(bpy.app.version[0])[:1]) + (str(bpy.app.version[1])[:1]))

    def execute(self, context):
        restore_all_keymaps()
        return {'FINISHED'}

    def invoke(self, context, event):
        if self.blender_version >= 41:
            message = context.window_manager.invoke_confirm(self, event, title="Restore Keymaps?",
                                                            message="Restore all keymaps to saved state",
                                                            confirm_text="Restore", icon='WARNING')
        else:
            message = context.window_manager.invoke_confirm(self, event)
        return message


classes = (WM_OT_RestoreKeyconfig,)
register, unregister = bpy.utils.register_classes_factory(classes)