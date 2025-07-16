import bpy
import os
from bpy.app.handlers import persistent
from bl_keymap_utils import keymap_hierarchy
from ..utils.utl_keymap_editing import (remove_addon_keymap_items, keymap_items_copy, apply_del_rule,
                                        restore_addon_keymap_items)
from ..ui.ui_keymap_preview import (keymap_hierarchy_generator, keymap_organize,
                                    keyitem_prop_preview)
from ..utils.utl_addon_preferences import (get_addon_name, presets_get_path)
from ..utils.utl_json import (keyconfig_to_json, json_to_keyconfig)

class KeyconfigBugFixAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = get_addon_name()

    tabs: bpy.props.EnumProperty(items=[("SETTINGS", "Settings", ""),
                                        ("ADDONS_KEYMAPS", "Addons Keymaps", "")],
                                 default="SETTINGS")

    auto_remove_keys: bpy.props.BoolProperty(name="Auto Delete Addons Keys", default=False)

    menu_save_keyconfig: bpy.props.BoolProperty(name="Show Save Keyconfig", default=True)
    menu_save_keyconfig_as: bpy.props.BoolProperty(name="Show Save Keyconfig As...", default=True)
    menu_save_and_restore: bpy.props.BoolProperty(name="Show Save & Restore Keyconfig", default=True)
    menu_restore_keyconfig: bpy.props.BoolProperty(name="Show Restore All Keymaps", default=True)
    menu_remove_addon_keymap_items: bpy.props.BoolProperty(name="Show Remove All Addon Keys", default=True)
    menu_restore_addon_keymap_items: bpy.props.BoolProperty(name="Show Restore All Addon Keys", default=True)
    menu_save_json_preset: bpy.props.BoolProperty(name="Show Apply And Save Preset", default=True)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        if not self.auto_remove_keys:
            row.prop(self, "tabs", expand=True)
            layout.separator()
            if self.tabs == 'SETTINGS':
                self.draw_settings_tab(layout)
            if self.tabs == 'ADDONS_KEYMAPS':
                self.draw_keymaps_tab(layout)
        else:
            self.draw_settings_tab(layout)

    def draw_settings_tab(self, layout):
        row = layout.row()
        row.label(text="Delete all addon keys when blender launch")
        row = layout.row()
        row.prop(self, "auto_remove_keys")
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


    def draw_keymaps_tab(self, layout):
        kc_addon_fix = bpy.context.window_manager.keyconfigs["kc_addon_fix"]

        hierarchy = dict.fromkeys(keymap_hierarchy_generator(keymap_hierarchy.generate()))
        kc_addon_fix_names = [i.name for i in kc_addon_fix.keymaps]
        ordered_keymaps = keymap_organize(kc_addon_fix_names, hierarchy)

        col = layout.column()
        row = col.row()
        row.operator("wm.save_json_preset")
        for keymap in ordered_keymaps:
            col = layout.column()
            row = col.row()
            row.prop(kc_addon_fix.keymaps[keymap], "show_expanded_children", text="", emboss=False)
            row.label(text=kc_addon_fix.keymaps[keymap].name)
            for addon_keymap in kc_addon_fix.keymaps:
                if addon_keymap.name == keymap and addon_keymap.show_expanded_children:
                    for item in reversed(addon_keymap.keymap_items):
                        self.draw_keyitem_preview(layout, item)


    def draw_keyitem_preview(self, layout, key):
        col = layout.column()

        if key.show_expanded:
            col = col.column(align=True)
            box = col.box()
        else:
            box = col.box()

        split = box.split(factor=0.6)

        row = split.row(align=True)
        row.prop(key, "active", text="", emboss=False)
        row.prop(key, "show_expanded", text="", emboss=False)
        row.label(text=key.name)

        row = split.row(align=True)
        box = row.box()
        box.label(text=f"{key.to_string()}")

        if key.show_expanded:
            box = col.box()
            keyitem_prop_preview(key, box)

    def draw_add_keys_tab(self, layout):
        pass


@persistent
def kc_fix_load_handler(dummy):
    kcs = bpy.context.window_manager.keyconfigs
    kc_addons = kcs.addon

    try:
        kcs['kc_addon_fix']
    except:
        kc_addon_fix = kcs.new("kc_addon_fix")
        keymap_items_copy(kc_addons, kc_addon_fix)
        json_to_keyconfig(kc_addon_fix)
        apply_del_rule(kc_addon_fix)

    try:
        if bpy.context.preferences.addons[get_addon_name()].preferences['auto_remove_keys']:
            remove_addon_keymap_items()
    except:
        pass

    kcs.update()


classes = (KeyconfigBugFixAddonPreferences,)


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.app.handlers.load_post.append(kc_fix_load_handler)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    #restore_addon_keymap_items()

    bpy.app.handlers.load_post.remove(kc_fix_load_handler)