import bpy
import json
import os
from ..utils.utl_addon_preferences import presets_get_path


def keyconfig_to_json(kc):
    data = {}
    with open(os.path.join(presets_get_path(), "keymap_items_del.json"), "w", encoding="utf-8") as file:
        for keymap in kc.keymaps:
            data.update({keymap.name: {}})
            for n, item in enumerate(keymap.keymap_items):
                if item.active:
                    continue
                id = f"key_{str(n)}"
                data[keymap.name].update({id: {'idname': item.idname,
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


def json_to_keyconfig(kc):
    with open(os.path.join(presets_get_path(), "keymap_items_del.json"), "r", encoding="utf-8") as file:
        data = json.load(file)

    for key in data.keys():
        if key not in kc.keymaps:
            continue
        for item in data[key]:
            value = data[key][item]
            kmi = kc.keymaps[key].keymap_items[value['idname']]
            if not value['idname'] == kmi.idname: continue
            if not value['type'] == kmi.type: continue
            if not value['value'] == kmi.value: continue
            if not value['any'] == kmi.any: continue
            if not value['shift'] == kmi.shift: continue
            if not value['ctrl'] == kmi.ctrl: continue
            if not value['alt'] == kmi.alt: continue
            if not value['oskey'] == kmi.oskey: continue
            if not value['hyper'] == kmi.hyper: continue
            if not value['key_modifier'] == kmi.key_modifier: continue
            if not value['direction'] == kmi.direction: continue
            if not value['repeat'] == kmi.repeat: continue
            kmi.active = False



