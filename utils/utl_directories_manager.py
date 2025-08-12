import bpy
import os
import json


def make_directory_presets():
    path = get_presets_path()
    if not os.path.exists(path):
        os.makedirs(path)


def make_json_presets():
    path = os.path.join(get_presets_path(), "addon_keymap_items_del.json")
    if not os.path.exists(path):
        file = open(path, "w", encoding="utf-8")
        json.dump({}, file, indent=4)


def get_presets_path():
    return os.path.join(bpy.utils.user_resource('SCRIPTS'), "presets", get_addon_name())


def get_addon_name():
    return __package__.partition(".")[0]


def get_preferences():
    return bpy.context.preferences.addons[get_addon_name()].preferences