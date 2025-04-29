import os
import random

# Automatically use the folder where the script is being run
output_dir = os.getcwd()

# Make sure the output directory exists (should already exist)
os.makedirs(output_dir, exist_ok=True)

# List of real file types only (no unknowns)
file_types = {
    "excel": [".xlsx"],
    "word": [".docx"],
    "powerpoint": [".pptx"],
    "text": [".txt"],
    "audio": [".mp3", ".wav"],
    "video": [".mp4", ".mov"],
    "image": [".png", ".jpeg", ".jpg", ".gif"],
    "pdf": [".pdf"],
    "html": [".html"],
}

# How many total files to create
num_files = 50

# Randomly create files
for i in range(1, num_files + 1):
    category = random.choice(list(file_types.keys()))
    extension = random.choice(file_types[category])
    file_name = f"testfile_{i}{extension}"
    file_path = os.path.join(output_dir, file_name)
    
    # Actually create the dummy file
    with open(file_path, 'w') as f:
        f.write(f"This is a dummy file for testing: {file_name}")

print(f"✅ Successfully created {num_files} files in: {output_dir}")