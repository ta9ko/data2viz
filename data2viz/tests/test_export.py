import pytest
from data2viz.export import export_visualization
import plotly.graph_objects as go

def test_export_html():
    fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[10, 20, 30])])
    export_visualization(fig, 'html', 'test_chart.html')
    # Проверяем, что файл создан
    import os
    assert os.path.exists('test_chart.html')

def test_export_png():
    fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[10, 20, 30])])
    export_visualization(fig, 'png', 'test_chart.png')
    # Проверяем, что файл создан
    import os
    assert os.path.exists('test_chart.png')
