import bpy
from ..utils.utl_json_presets import (keyconfig_to_preset_del)
from ..utils.utl_keymap_editing import apply_del_rule

class KBF_OT_SavePresets(bpy.types.Operator):
    bl_idname = "kbf.save_presets"
    bl_label = "Apply And Save Preset"
    bl_description = "Apply And Save Preset"

    def execute(self, context):
        kc_addon_restore = bpy.context.window_manager.keyconfigs['addon_restore']
        keyconfig_to_preset_del(kc_addon_restore)
        apply_del_rule(kc_addon_restore)
        return {'FINISHED'}


classes = (KBF_OT_SavePresets,)
register, unregister = bpy.utils.register_classes_factory(classes)