import pytest
import pandas as pd
from data2viz.data_import import import_data

def test_import_csv():
    data = import_data('data.csv')
    assert isinstance(data, pd.DataFrame)
    assert 'category' in data.columns

def test_import_excel():
    data = import_data('data.xlsx')
    assert isinstance(data, pd.DataFrame)
    assert 'category' in data.columns

def test_import_sqlite():
    # Пример для SQLite; требуется настройка тестовой базы данных
    pass
