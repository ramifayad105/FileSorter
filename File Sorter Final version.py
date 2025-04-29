import os
import sys
import shutil
import tkinter as tk

# Correct base path
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

# Map extensions to folders
extension_to_folder = {
    ".xlsx": "excel files",
    ".docx": "word files",
    ".pptx": "powerpoint files",
    ".txt": "text files",
    ".mp3": "audio files",    
    ".wav": "wav files",
    ".mp4": "video files",      
    ".mov": "video files",      
    ".png": "image files",
    ".jpeg": "image files",
    ".jpg": "image files",
    ".gif": "image files",
    ".pdf": "pdf files",
    ".html": "html files",
}

# List only files, not folders
file_names = [f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))]

# Track needed folders
needed_folders = set()

# First pass: figure out needed folders
for file in file_names:
    ext = os.path.splitext(file)[1].lower()
    if ext in extension_to_folder:
        needed_folders.add(extension_to_folder[ext])

# Create only needed folders
folders_created = 0
for folder in needed_folders:
    folder_path = os.path.join(base_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        folders_created += 1

# Second pass: move files into correct folders
for file in file_names:
    ext = os.path.splitext(file)[1].lower()
    folder = extension_to_folder.get(ext)
    if folder:
        shutil.move(os.path.join(base_path, file), os.path.join(base_path, folder, file))

# Popup window to show how many folders were created
root = tk.Tk()
root.title("Folders Created")
root.geometry("300x100")
root.eval('tk::PlaceWindow . center')

message = f"{folders_created} folder(s) created." if folders_created > 0 else "No new folders created."
label = tk.Label(root, text=message, font=("Arial", 12))
label.pack(expand=True)

root.after(3000, root.destroy)
root.mainloop()