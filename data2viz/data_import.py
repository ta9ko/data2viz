import pandas as pd
from sqlalchemy import create_engine


def import_data(source, **kwargs):
    if source.endswith('.csv'):
        data = pd.read_csv(source)
    elif source.endswith('.xlsx'):
        data = pd.read_excel(source)
    elif isinstance(source, str) and source.startswith('sqlite:///'):
        engine = create_engine(source)
        data = pd.read_sql(kwargs.get('query', 'SELECT * FROM table_name'), engine)
    else:
        raise ValueError("Unsupported data source format")

    data.columns = data.columns.str.strip()  # Strip whitespace from column names
    return data
