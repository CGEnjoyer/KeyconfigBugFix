import bpy


class WM_OT_TESTOPR(bpy.types.Operator):
    bl_idname = "wm.test_opr"
    bl_label = "Test OPR"
    bl_description = "Test opr"

    boolprop_d: bpy.props.BoolProperty(name="Boolprop D", default=False)
    boolprop_m: bpy.props.BoolProperty(name="Boolprop M", default=False)
    boolvector_d: bpy.props.BoolVectorProperty(name="Bool V D")
    boolvector_m: bpy.props.BoolVectorProperty(name="Bool V M")
    enumrop_d: bpy.props.EnumProperty(items=[('fst_enum', "First Enum", "lol disc", 'GROUP_BONE', 0),
                                             ('scd_enum', "Second Enum", "lol disc 2", 'MODIFIER_ON', 1)],
                                      name="Enum Prop D")
    enumrop_m: bpy.props.EnumProperty(items=[('fst_enum', "First Enum", "lol disc", 'GROUP_BONE', 0),
                                             ('scd_enum', "Second Enum", "lol disc 2", 'MODIFIER_ON', 1)],
                                      name="Enum Prop M")
    floatprop_d: bpy.props.FloatProperty(name="Float Prop D")
    floatprop_m: bpy.props.FloatProperty(name="Float Prop M")
    floatvprop_d: bpy.props.FloatVectorProperty(name="Float V Prop D")
    floatvprop_m: bpy.props.FloatVectorProperty(name="Float V Prop M")
    intprop_d: bpy.props.IntProperty(name="Int Prop D")
    intprop_m: bpy.props.IntProperty(name="Int Prop M")
    intvprop_d: bpy.props.IntVectorProperty(name="Int V Prop D")
    intvprop_m: bpy.props.IntVectorProperty(name="Int V Prop M")
    strprop_d: bpy.props.StringProperty(name="Str Prop D")
    strprop_m: bpy.props.StringProperty(name="Str Prop M")

    def execute(self, context):
        return {'FINISHED'}


addon_keymaps = []

classes = (WM_OT_TESTOPR,)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.context.window_manager.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
    kmi = bpy.context.window_manager.keyconfigs.addon.keymaps['Window'].keymap_items.new(
        "wm.test_opr", type='W', value='CLICK_DRAG', ctrl=True, shift=True, alt=True, oskey=True, direction='SOUTH')
    kmi.properties.boolprop_m = True
    kmi.properties.boolvector_m = (True, True, False)
    kmi.properties.enumrop_m = 'scd_enum'
    kmi.properties.floatprop_m = 24.9834
    kmi.properties.floatvprop_m = (24.9834, 1234.333, 0.422)
    kmi.properties.intprop_m = 19223
    kmi.properties.intvprop_m = (123, 543, 224132)
    kmi.properties.strprop_m = "WErefwe Weewwea"
    kmi = bpy.context.window_manager.keyconfigs.addon.keymaps['Window'].keymap_items.new(
        "wm.test_opr", type='D', value='CLICK_DRAG', ctrl=True, shift=True, alt=True, oskey=True, direction='SOUTH')

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)