# KeyconfigBugFix

This addon helps to avoid the problem of duplicating hotkeys when saving a preset

About issue: https://projects.blender.org/blender/blender-addons/issues/88518

## WARNING!
### known issue:
A bug may affect the Enable/Disable of other addons.
To **fix problems** with enabling other addons, **restart Blender**
[**About Bug**](https://github.com/CGEnjoyer/KeyconfigBugFix/issues/2#issue-3237466526)

I have tested this addon on different versions and in different conditions, but I still recommend making a backup of all user settings before using it.

## Installation

* Download KeyconfigBugFix.zip from the latest available release: https://github.com/CGEnjoyer/KeyconfigBugFix/releases
* Open the Edit > Preferences... > Add-ons > Install from Disck...

## Where are these located in blender?

### Main Save Operators

Edit > Preferences... > Save & Load Menu (USERPREF_MT_save_load)

<img src="https://github.com/CGEnjoyer/src/blob/9b0d19b42c6542fa336641bd3848e44395671d1f/KeyconfigBugFix/src_KeyconfigBugFix_menu.png" width="400">

### Addon Preferences & Debug operator

Edit > Preferences... > Add-ons > Keyconfig Bug Fix

<img src="https://github.com/CGEnjoyer/src/blob/9b0d19b42c6542fa336641bd3848e44395671d1f/KeyconfigBugFix/src_KeyconfigBugFix_addonPrefs.png" width="400">

## Features

### Keyconfig Operators

#### Save Keyconfig & Save Keyconfig As...

This is the main function that saves keyconfig without keys from addons and does not create duplicates. 
Save operator resave current keyconfig with the same name.
If current keyconfig 'Blender', 'Blender_27x', 'Industry_Compatible' — save config_name + "Redefined".
Save As... allows you to save the keyconfig with a chosen name and restore all keys

#### Save And Restore Keyconfig

Save keyconfig and automaticly restore all keymaps

#### Restore All Keymaps

Now you don't have to manually press the "Restore" buttons for each keymap category

#### Remove All Addon Keys

Removes all keys from addons that are added automatically when blender starts. After restart, the removed buttons will be added again.

#### Check Addon Keys

Show all addon keys which are currently active in the keyconfig

<img src="https://github.com/CGEnjoyer/src/blob/9b0d19b42c6542fa336641bd3848e44395671d1f/KeyconfigBugFix/src_KeyconfigBugFix_checkKeys.png" width="400">

### Addon Preferences

#### Auto Delete Addons Keys

This setting allows you to automatically remove addon keys every time you start Blender. This is actually very useful for me as I prefer to manually create keys for myself

## About Duplicate Bug

Blender stores your hotkeys in bpy.context.window_manager.keyconfigs.user

Hotkeys that are added automatically when Blender starts and registered from addons stores in bpy.context.window_manager.keyconfigs.addon

If you interact with keys (delete, add, change) and save or export keyconfig, then the addon keys will also be included in the user keys list

To accurately reproduce the bug, you need to change the user keys, not the addon keys.

Contrary to the opinion from https://projects.blender.org/blender/blender-addons/issues/88518 The "All Keymap" button does not affect the reproduction of the bug. For example, if you have changes in keymaps['Window'] and there are also keys from addons, then in keyconfigName.py the keys of keymaps['Window'] will be exported with the keys from the addon

## How does this work?

It's very simple! The script creates a temporary keyconfig and duplicates all addon buttons into it, then deletes all keys from keyconfigs.addon and saves the user preset, then restores all keyconfigs.addon from the temporary keyconfig again

For understanding, see:

* utils/utl_keymap_editing.py
* ops/opr_save_current_keyconfig.py
