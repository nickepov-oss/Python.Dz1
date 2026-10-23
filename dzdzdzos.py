import os
path = input("Path: ")
if os.path.exists(path):
    for item in os.listdir(path):
        print(item)