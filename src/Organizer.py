import os
import shutil

file_types = {
    "jpg": "Images",
    "png": "Images",
    "gif": "Images",
    "mp4": "Videos",
    "mov": "Videos",
    "avi": "Videos",
    "doc": "Documents",
    "docx": "Documents",
    "pdf": "Documents",
    "txt": "Text",
    "py": "Python Scripts"
}


def move_file(filename):
    extension = filename.split(".")[-1]
    if extension in file_types:
        folder_name = file_types[extension]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        shutil.move(filename, os.path.join(folder_name, filename))


cwd = os.getcwd()

for filename in os.listdir(cwd):
    if os.path.isfile(filename) and filename != "organizer.py":
        move_file(filename)

# To use the script, save this code to a file named "organizer.py" and run it in your
# Python environment.Remember to modify the file_types dictionary to match your preferred folder names.
