import plotly.express as px


def create_chart(data, chart_type, **kwargs):
    if chart_type == 'bar':
        fig = px.bar(data, **kwargs)
    elif chart_type == 'line':
        fig = px.line(data, **kwargs)
    elif chart_type == 'pie':
        fig = px.pie(data, **kwargs)
    elif chart_type == 'heatmap':
        fig = px.density_heatmap(data, **kwargs)
    else:
        raise ValueError("Unsupported chart type")

    fig.update_layout(autosize=True)
    fig.show()
    return fig
