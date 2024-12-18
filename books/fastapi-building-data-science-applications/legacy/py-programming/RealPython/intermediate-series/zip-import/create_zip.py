import zipfile

'''
with zipfile.PyZipFile("hello.zip", mode="w") as zip_module:
    zip_module.writepy("hello.py")

with zipfile.PyZipFile("hello.zip", mode="r") as zip_module:
    zip_module.printdir()
# '''

with zipfile.PyZipFile("goodbye_pkg.zip", mode="w") as zip_pkg:
    zip_pkg.writepy("goodbye")

with zipfile.PyZipFile("goodbye_pkg.zip", mode="r") as zip_pkg:
    zip_pkg.printdir()
