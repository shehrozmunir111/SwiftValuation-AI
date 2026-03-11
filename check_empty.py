import os

root = "."

empty_folders = []
empty_files = []

for path, dirs, files in os.walk(root):
    if not dirs and not files:
        empty_folders.append(path)
    for file in files:
        full_path = os.path.join(path, file)
        if os.path.getsize(full_path) == 0:
            empty_files.append(full_path)

print("\nEMPTY FOLDERS:\n")
for f in empty_folders:
    print(f)

print("\nEMPTY FILES:\n")
for f in empty_files:
    print(f)