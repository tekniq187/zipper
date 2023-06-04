import os
import zipfile

folder_name = input("Please enter the name of the folder to zip: ")

zip_name = f"{folder_name}.zip"

with zipfile.ZipFile(zip_name, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
    for root, dirs, files in os.walk(folder_name):
        for f in files:
            file_path = os.path.join(root, f)
            arc_name = os.path.relpath(file_path, folder_name)
            zip_file.write(file_path, arc_name)

print(f"{zip_name} created successfully!")