import bpy
from ..utils.utl_keymap_editing import (keymap_items_copy,
                                        remove_addon_keymap_items,
                                        restore_all_keymaps)


class WM_OT_SaveCurrentKeyconfig(bpy.types.Operator):
    bl_idname = "wm.save_current_keyconfig"
    bl_label = "Save Keyconfig"
    bl_description = "Save active keyconfig without addon keys"

    keymaps_restore: bpy.props.BoolProperty(name="Restore All Keymaps", default=False)

    def execute(self, context):
        kcs = bpy.context.window_manager.keyconfigs
        kc_addon = kcs.addon
        kc_tmp = kcs.new("tmp_addons_keyconfig")


        # copy addon keymaps to temporary keyconfig
        keymap_items_copy(kc_addon, kc_tmp)

        # remove all addon keymap items
        remove_addon_keymap_items()

        # update and save keyconfig
        kcs.update()
        if kcs.active.name in ['Blender', 'Blender_27x', 'Industry_Compatible']:
            bpy.ops.wm.keyconfig_preset_add(name=kcs.active.name + "Redefined")
        else:
            bpy.ops.wm.keyconfig_preset_add(name=kcs.active.name)

        # copy keymaps from tmp to addon
        keymap_items_copy(kc_tmp, kc_addon)
        kcs.remove(kc_tmp)

        if self.keymaps_restore: restore_all_keymaps()

        return {'FINISHED'}


class WM_OT_SaveCurrentKeyconfigAs(bpy.types.Operator):
    bl_idname = "wm.save_current_keyconfig_as"
    bl_label = "Save Keyconfig As..."
    bl_description = "Save active keyconfig with new name without addon keys"

    keymaps_restore: bpy.props.BoolProperty(name="Restore All Keymaps", default=False)
    kc_new_name: bpy.props.StringProperty(name="New Name", default="")

    def execute(self, context):
        kcs = bpy.context.window_manager.keyconfigs
        kc_addon = kcs.addon
        kc_tmp = kcs.new("tmp_addons_keyconfig")

        # copy addon keymaps to temporary keyconfig
        keymap_items_copy(kc_addon, kc_tmp)

        # remove all addon keymap items
        remove_addon_keymap_items()

        # update and save keyconfig
        kcs.update()
        bpy.ops.wm.keyconfig_preset_add(name=self.kc_new_name)

        # copy keymaps from tmp to addon
        keymap_items_copy(kc_tmp, kc_addon)
        kcs.remove(kc_tmp)

        if self.keymaps_restore: restore_all_keymaps()

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(self, "kc_new_name")
        col.prop(self, "keymaps_restore")


classes = (WM_OT_SaveCurrentKeyconfig, WM_OT_SaveCurrentKeyconfigAs)
register, unregister = bpy.utils.register_classes_factory(classes)