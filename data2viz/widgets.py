import ipywidgets as widgets

def create_widget(widget_type, **kwargs):
    if widget_type == 'dropdown':
        return widgets.Dropdown(**kwargs)
    elif widget_type == 'slider':
        return widgets.IntSlider(**kwargs)
    elif widget_type == 'checkbox':
        return widgets.Checkbox(**kwargs)
    else:
        raise ValueError("Unsupported widget type")
