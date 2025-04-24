# 61. Write a program to zip and unzip a file.

import zipfile
import os

def zip_file(file_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(file_path, os.path.basename(file_path))
    print(f"{file_path} zipped into {zip_name}")
def unzip_file(zip_name, extract_to='.'):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"{zip_name} extracted to {extract_to}")
# Zip the file
zip_file("sample.txt", "sample.zip")

# Unzip the file
unzip_file("sample.zip", "./unzipped_files")
