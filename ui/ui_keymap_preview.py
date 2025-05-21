import bpy


def keymap_hierarchy_generator(hierarchy):
    for item in hierarchy:
        if isinstance(item, tuple):
            yield item[0]
        for sub in item:
            if isinstance(sub, list):
                yield from keymap_hierarchy_generator(sub)

def keymap_organize(keymaps, hierarchy):
    for item in hierarchy:
        if item in keymaps:
            yield item

def nice_key_name(key_name):
    names = {'NONE': "",
             'ANY': "Any",
             'PRESS': "Press",
             'RELEASE': "Release",
             'CLICK': "Click",
             'DOUBLE_CLICK': "Double Click",
             'CLICK_DRAG': "Click Drag",
             'NOTHING': "Nothing",
             'LEFTMOUSE': "Left Mouse",
             'MIDDLEMOUSE': "Middle Mouse",
             'RIGHTMOUSE': "Right Mouse",
             'BUTTON4MOUSE': "Button 4 Mouse",
             'BUTTON5MOUSE': "Button 5 Mouse",
             'BUTTON6MOUSE': "Button 6 Mouse",
             'BUTTON7MOUSE': "Button 7 Mouse",
             'PEN': "Pen",
             'ERASER': "Eraser",
             'MOUSEMOVE': "Mouse Move",
             'INBETWEEN_MOUSEMOVE': "In-between Move",
             'TRACKPADPAN': "Mouse/Trackpad Pan",
             'TRACKPADZOOM': "Mouse/Trackpad Zoom",
             'MOUSEROTATE': "Mouse/Trackpad Rotate",
             'MOUSESMARTZOOM': "Mouse/Trackpad Smart Zoom",
             'WHEELUPMOUSE': "Wheel Up",
             'WHEELDOWNMOUSE': "Wheel Down",
             'WHEELINMOUSE': "Wheel In",
             'WHEELOUTMOUSE': "Wheel Out",
             'ZERO': "0",
             'ONE': "1",
             'TWO': "2",
             'THREE': "3",
             'FOUR': "4",
             'FIVE': "5",
             'SIX': "6",
             'SEVEN': "7",
             'EIGHT': "8",
             'NINE': "9",
             'LEFT_CTRL': "Left Ctrl",
             'LEFT_ALT': "Left Alt",
             'LEFT_SHIFT': "Left Shift",
             'RIGHT_ALT': "Right Alt",
             'RIGHT_CTRL': "Right Ctrl",
             'RIGHT_SHIFT': "Right Shift",
             'OSKEY': "OS Key",
             'APP': "Application",
             'GRLESS': "Grless",
             'ESC': "Esc",
             'TAB': "Tab",
             'RET': "Return",
             'SPACE': "Space Bar",
             'LINE_FEED': "Line Feed",
             'BACK_SPACE': "Backspace",
             'DEL': "Delete",
             'SEMI_COLON': ";",
             'PERIOD': ".",
             'COMMA': ",",
             'QUOTE': "“",
             'ACCENT_GRAVE': "`",
             'MINUS': "-",
             'PLUS': "+",
             'SLASH': "/",
             'BACK_SLASH': "\\",
             'EQUAL': "=",
             'LEFT_BRACKET': "[",
             'RIGHT_BRACKET': "]",
             'LEFT_ARROW': "Left Arrow",
             'DOWN_ARROW': "Down Arrow",
             'RIGHT_ARROW': "Right Arrow",
             'UP_ARROW': "Up Arrow",
             'NUMPAD_0': "Numpad 0",
             'NUMPAD_1': "Numpad 1",
             'NUMPAD_2': "Numpad 2",
             'NUMPAD_3': "Numpad 3",
             'NUMPAD_4': "Numpad 4",
             'NUMPAD_5': "Numpad 5",
             'NUMPAD_6': "Numpad 6",
             'NUMPAD_7': "Numpad 7",
             'NUMPAD_8': "Numpad 8",
             'NUMPAD_9': "Numpad 9",
             'NUMPAD_PERIOD': "Numpad .",
             'NUMPAD_SLASH': "Numpad /",
             'NUMPAD_ASTERIX': "Numpad *",
             'NUMPAD_MINUS': "Numpad -",
             'NUMPAD_ENTER': "Numpad Enter",
             'NUMPAD_PLUS': "Numpad +",
             'PAUSE': "Pause",
             'INSERT': "Insert",
             'HOME': "Home",
             'PAGE_UP': "Page Up",
             'PAGE_DOWN': "Page Down",
             'END': "End",
             'MEDIA_PLAY': "Media Play/Pause",
             'MEDIA_STOP': "Media Stop",
             'MEDIA_FIRST': "Media First",
             'MEDIA_LAST': "Media Last",
             'TEXTINPUT': "Text Input",
             'WINDOW_DEACTIVATE': "Window Deactivate",
             'TIMER0': "Timer 0",
             'TIMER1': "Timer 1",
             'TIMER2': "Timer 2",
             'TIMER_JOBS': "Timer Jobs",
             'TIMER_AUTOSAVE': "Timer Autosave",
             'TIMER_REPORT': "Timer Report",
             'TIMERREGION': "Timer Region",
             }
    try:
        return names[key_name]
    except:
        return key_name

def keyitem_preview(key_item):
    name = ""
    draw = False
    if key_item.any:
        name = "Any "
        draw = True
    else:
        if key_item.shift:
            name += "Shift "
            draw = True
        if key_item.ctrl:
            name += "Ctrl "
            draw = True
        if key_item.alt:
            name += "Alt "
            draw = True
        if key_item.oskey:
            name += "Cmd "
            draw = True
        if key_item.key_modifier != 'NONE':
            name += nice_key_name(key_item.key_modifier) + " "
            draw = True
    if draw:
        name += "+ "

    if key_item.value != 'ANY':
        name += f"{nice_key_name(key_item.value)} "
    name += f"{nice_key_name(key_item.type)}"

    return name

def keyitem_prop_preview(key_item, layout):
    keyitem_props = key_item.properties
    operator_props = keyitem_props.rna_type.properties
    keyitem_props_ids = keyitem_props.id_properties_ensure().to_dict().keys()
    if len(operator_props) > 1:
        row = layout.row()
        split = row.split(factor=0.1)
        split.column()
        default_col = split.column()
        reassigned_col = split.column()
        default_col.label(text="Default:")
        reassigned_col.label(text="Reassigned:")
        for pr in operator_props[1:]:
            if pr.identifier in keyitem_props_ids:
                reassigned_col.label(text=(f"{pr.name}: "
                                           f"{prop_preview(prop=pr, keyprop=keyitem_props[pr.identifier], mode=True)}"))
            else:
                default_col.label(text=f"{pr.name}: {prop_preview(prop=pr, mode=False)}")

def prop_preview(prop, mode, keyprop=None):
    type = prop.type
    if mode:
        if type == 'BOOLEAN':
            if prop.is_array:
                return f"{bool(keyprop[0]), bool(keyprop[1]), bool(keyprop[2])}"
            else:
                return f"{bool(keyprop)}"
        elif type == 'INT':
            if prop.is_array:
                return f"{keyprop[0], keyprop[1], keyprop[2]}"
            else:
                return f"{keyprop}"
        elif type == 'FLOAT':
            if prop.is_array:
                return f"{round(keyprop[0], 2), round(keyprop[1], 2), round(keyprop[2], 2)}"
            else:
                return f"{round(keyprop, 2)}"
        elif type == 'ENUM':
            return f"{prop.enum_items[keyprop].name}"
        elif type == 'STRING':
            return f"{keyprop}"

    else:
        if type == 'BOOLEAN':
            if prop.is_array:
                return f"{prop.default_array[0], prop.default_array[1], prop.default_array[2]}"
            else:
                return f"{prop.default}"
        elif type == 'INT':
            if prop.is_array:
                return f"{prop.default_array[0], prop.default_array[1], prop.default_array[2]}"
            else:
                return f"{prop.default}"
        elif type == 'FLOAT':
            if prop.is_array:
                return f"{round(prop.default_array[0], 2), round(prop.default_array[0], 2), round(prop.default_array[0], 2)}"
            else:
                return f"{round(prop.default, 2)}"
        elif type == 'ENUM':
            return f"{prop.enum_items[prop.default].name}"
        elif type == 'STRING':
            return f"{prop.default}"