import bpy


def remove_addon_keymap_items():
    for keymap in bpy.context.window_manager.keyconfigs.addon.keymaps:
        for item in keymap.keymap_items:
            keymap.keymap_items.remove(item)


def restore_addon_keymap_items():
    kc = bpy.context.window_manager.keyconfigs['kc_addon_fix']
    kc_addons = bpy.context.window_manager.keyconfigs.addon
    remove_addon_keymap_items()
    keymap_items_copy(kc, kc_addons)
    for keymap in kc_addons.keymaps:
        for item in keymap.keymap_items:
            item.active = True


def restore_all_keymaps():
    for keymap in bpy.context.window_manager.keyconfigs.default.keymaps:
        keymap.restore_to_default()


def keymap_items_copy(source_keyconfig, target_keyconfig, only_active=False):
    for keymap in source_keyconfig.keymaps:
        km = target_keyconfig.keymaps.new(name=keymap.name, space_type=keymap.space_type,
                                          region_type=keymap.region_type, modal=keymap.is_modal)
        for item in source_keyconfig.keymaps[keymap.name].keymap_items:
            if only_active and item.active:
                km.keymap_items.new_from_item(item)
            elif not only_active:
                km.keymap_items.new_from_item(item)


def apply_del_rule(kc):
    kc_addons = bpy.context.window_manager.keyconfigs.addon
    remove_addon_keymap_items()
    keymap_items_copy(kc, kc_addons, only_active=True)

