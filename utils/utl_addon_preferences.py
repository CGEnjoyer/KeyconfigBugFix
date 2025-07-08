import bpy
import os


def presets_makedir():
    folder_path = presets_get_path()
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def presets_get_path():
    return os.path.join(bpy.utils.user_resource('SCRIPTS'), "presets", get_addon_name())


def get_addon_name():
    return __package__.partition(".")[0]


def get_preferences():
    return bpy.context.preferences.addons[get_addon_name()].preferences