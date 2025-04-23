import bpy


class WM_OT_DebugCheckAddonKeys(bpy.types.Operator):
    bl_idname = "wm.debug_check_addon_keys"
    bl_label = "Check Addon Keys (Console)"
    bl_description = "Show all addon key on console"

    def execute(self, context):
        for keymap in bpy.context.window_manager.keyconfigs.addon.keymaps:
            for item in keymap.keymap_items:
                print("in {} -------> {}".format(keymap.name, item.name))
        return {'FINISHED'}


classes = (WM_OT_DebugCheckAddonKeys,)
register, unregister = bpy.utils.register_classes_factory(classes)