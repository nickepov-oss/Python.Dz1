import os
path = "C:\\Users\\Lenovo"
for path, dirnames, filenames in os. walk(path) :
    print(f"path - {path}")
    print(f"dirnames - {dirnames}")
    print(f"filenames - {filenames}")

dir1 = "Windows"
dir2 = "4K"
path1 = os. path. join(path, dir2)
print(path1)

path2 = os.path.normpath("C: \\Windows\ \Web")
print(os.path.isabs)