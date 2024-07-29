import pytest
import pandas as pd
from data2viz.visualization import create_chart

def test_create_bar_chart():
    data = pd.DataFrame({
        'x_col': [1, 2, 3],
        'y_col': [10, 20, 30]
    })
    fig = create_chart(data, 'bar', x='x_col', y='y_col')
    assert fig is not None

def test_create_line_chart():
    data = pd.DataFrame({
        'x_col': [1, 2, 3],
        'y_col': [10, 20, 30]
    })
    fig = create_chart(data, 'line', x='x_col', y='y_col')
    assert fig is not None
