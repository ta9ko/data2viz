from data2viz.templates import TemplateGallery


def test_get_template():
    template = TemplateGallery.get_template('basic_bar')
    assert template is not None
    assert 'chart_type' in template
    assert 'kwargs' in template


def test_get_template_invalid():
    template = TemplateGallery.get_template('invalid_template')
    assert template is None
