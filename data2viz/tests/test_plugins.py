import pytest
from data2viz.plugins import PluginSystem


# Тестирование регистрации плагина
def test_register_plugin():
    plugin_system = PluginSystem()

    def sample_plugin(x):
        return x * 2

    plugin_system.register_plugin('sample', sample_plugin)

    # Проверяем, что плагин зарегистрирован
    assert 'sample' in plugin_system.plugins
    assert plugin_system.plugins['sample'] == sample_plugin


# Тестирование выполнения зарегистрированного плагина
def test_execute_plugin():
    plugin_system = PluginSystem()

    def sample_plugin(x):
        return x * 2

    plugin_system.register_plugin('sample', sample_plugin)
    result = plugin_system.execute_plugin('sample', 5)

    # Проверяем, что плагин возвращает правильный результат
    assert result == 10


# Тестирование выполнения несуществующего плагина
def test_execute_non_existent_plugin():
    plugin_system = PluginSystem()

    with pytest.raises(ValueError, match="Plugin not found"):
        plugin_system.execute_plugin('non_existent_plugin', 5)
