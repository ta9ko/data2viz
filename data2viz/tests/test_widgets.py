import pytest
import ipywidgets as widgets
from data2viz.widgets import create_widget

def test_create_dropdown():
    widget = create_widget('dropdown', options=['A', 'B', 'C'], value='A', description='Select:')
    assert isinstance(widget, widgets.Dropdown)

def test_create_slider():
    widget = create_widget('slider', min=0, max=10, value=5, description='Value:')
    assert isinstance(widget, widgets.IntSlider)
