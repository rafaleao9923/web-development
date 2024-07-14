import zipfile

plugins = ("web_message", "tk_message")
for plugin in plugins:
    with zipfile.PyZipFile(f"{plugin}.zip", mode="w") as zip_plugin:
        zip_plugin.writepy(plugin)
