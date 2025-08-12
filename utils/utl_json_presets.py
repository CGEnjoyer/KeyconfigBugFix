import json
import os
from ..utils.utl_directories_manager import get_presets_path


def keyconfig_to_preset_del(kc):
    data = {}
    with open(os.path.join(get_presets_path(), "addon_keymap_items_del.json"), "w", encoding="utf-8") as file:
        for km in kc.keymaps:
            data.update({km.name: {}})
            for n, kmi in enumerate(km.keymap_items):
                if kmi.active:
                    continue
                id = f"key_{str(n)}"
                data[km.name].update({id: {'idname': kmi.idname,
                                               'type': kmi.type,
                                               'value': kmi.value,
                                               'any': kmi.any,
                                               'shift': kmi.shift,
                                               'ctrl': kmi.ctrl,
                                               'alt': kmi.alt,
                                               'oskey': kmi.oskey,
                                               'hyper': kmi.hyper,
                                               'key_modifier': kmi.key_modifier,
                                               'direction': kmi.direction,
                                               'repeat': kmi.repeat}})
        json.dump(data, file, indent=4)


def preset_to_keyconfig_del(kc):
    with open(os.path.join(get_presets_path(), "addon_keymap_items_del.json"), "r", encoding="utf-8") as file:
        data = json.load(file)

    for key in data.keys():
        if key not in kc.keymaps:
            continue
        for item in data[key]:
            value = data[key][item]
            for kmi in kc.keymaps[key].keymap_items:
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



