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