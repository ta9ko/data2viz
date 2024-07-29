class PluginSystem:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, func):
        self.plugins[name] = func

    def execute_plugin(self, name, *args, **kwargs):
        if name in self.plugins:
            return self.plugins[name](*args, **kwargs)
        else:
            raise ValueError("Plugin not found")
