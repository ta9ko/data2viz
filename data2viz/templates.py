class TemplateGallery:
    @staticmethod
    def get_template(template_name):
        templates = {
            'basic_bar': {'chart_type': 'bar', 'kwargs': {'x': 'x_col', 'y': 'y_col'}},
            'basic_line': {'chart_type': 'line', 'kwargs': {'x': 'x_col', 'y': 'y_col'}},
            'basic_pie': {'chart_type': 'pie', 'kwargs': {'names': 'category', 'values': 'value'}},
            'basic_heatmap': {'chart_type': 'heatmap', 'kwargs': {'x': 'x_col', 'y': 'y_col', 'z': 'z_col'}}
        }
        return templates.get(template_name, None)
