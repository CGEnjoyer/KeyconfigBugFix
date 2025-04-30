import bpy


def get_addon_name():
    return __package__.partition(".")[0]


def get_preferences():
    return bpy.context.preferences.addons[get_addon_name()].preferences