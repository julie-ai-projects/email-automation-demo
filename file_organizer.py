import os
import shutil
from datetime import datetime
from config import SOURCE_FOLDER, OUTPUT_FOLDER

def organize_files():
    print("📁 Organizing files...")

    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)

        if os.path.isfile(file_path):
            ext = filename.split(".")[-1].lower()
            folder = os.path.join(OUTPUT_FOLDER, ext)

            os.makedirs(folder, exist_ok=True)
            shutil.move(file_path, os.path.join(folder, filename))
            print(f"Moved: {filename} → {folder}")

    print("✅ File organization complete.")
