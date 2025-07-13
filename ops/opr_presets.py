import bpy
from ..utils.utl_json import (keyconfig_to_json, json_to_keyconfig)
from ..utils.utl_keymap_editing import apply_del_rule

class WM_OT_SaveJSONPreset(bpy.types.Operator):
    bl_idname = "wm.save_json_preset"
    bl_label = "Save Preset"
    bl_description = "Save Preset"

    def execute(self, context):
        kc_addon_fix = bpy.context.window_manager.keyconfigs["kc_addon_fix"]
        keyconfig_to_json(kc_addon_fix)
        apply_del_rule(kc_addon_fix)
        return {'FINISHED'}


classes = (WM_OT_SaveJSONPreset,)
register, unregister = bpy.utils.register_classes_factory(classes)