import zipimport
from pathlib import Path


def load_plugins(path):
    plugins = []
    for zip_plugin in path.glob("*.zip"):
        # print(zip_plugin)
        importer = zipimport.zipimporter(zip_plugin)
        plugin_module = importer.load_module("plugin")  # for plugin.py inside
        plugins.append(getattr(plugin_module, "main"))  # for main function inside
    # print(plugins)    # list of address
    # [<function main at 0x000002B35188C678>, <function main at 0x000002B3518D4438>]
    return plugins


if __name__ == "__main__":
    path = Path("plugins/")
    plugins = load_plugins(path)
    for plugin in plugins:
        plugin("Hello, Hung!", "How are you!")
