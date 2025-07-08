import bpy
import json
import os
from ..utils.utl_addon_preferences import presets_get_path


def keyconfig_to_json(kc):
    data = {}
    with open(os.path.join(presets_get_path(), "keymap_items_del.json"), "w", encoding="utf-8") as file:
        for keymap in kc.keymaps:
            data.update({keymap.name: {'space_type': keymap.space_type,
                                       'region_type': keymap.region_type,
                                       'modal': keymap.is_modal,
                                       'items': {}}})
            for n, item in enumerate(keymap.keymap_items):
                id = f"key_{str(n)}"
                data[keymap.name]['items'].update({id: {'idname': item.idname,
                                  'type': item.type,
                                  'value': item.value,
                                  'any': item.any,
                                  'shift': item.shift,
                                  'ctrl': item.ctrl,
                                  'alt': item.alt,
                                  'oskey': item.oskey,
                                  'hyper': item.hyper,
                                  'key_modifier': item.key_modifier,
                                  'direction': item.direction,
                                  'repeat': item.repeat}})
        json.dump(data, file, indent=4)


def json_to_keyconfig():
    kcs = bpy.context.window_manager.keyconfigs
    if 'kc_from_json' in kcs: kcs.remove(kcs['kc_from_json'])

    with open(os.path.join(presets_get_path(), "keymap_items_del.json"), "r", encoding="utf-8") as file:
        data = json.load(file)

    kc = bpy.context.window_manager.keyconfigs.new("kc_from_json")

    for key in data.keys():
        km = kc.keymaps.new(name=key, space_type=data[key]['space_type'],
                            region_type=data[key]['region_type'], modal=data[key]['modal'])
        for item in data[key]['items']:
            value = data[key]['items'][item]
            km.keymap_items.new(idname=value['idname'],
                                type=value['type'],
                                value=value['value'],
                                any=value['any'],
                                shift=value['shift'],
                                ctrl=value['ctrl'],
                                alt=value['alt'],
                                oskey=value['oskey'],
                                hyper=value['hyper'],
                                key_modifier=value['key_modifier'],
                                direction=value['direction'],
                                repeat=value['repeat'])