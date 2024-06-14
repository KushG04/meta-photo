"""
module for organizing the images based on their metadata
"""

import os
import shutil
from datetime import datetime
from metadata_extractor import get_image_metadata

def organize_images_date(base_path):
    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)
        if os.path.isfile(file_path):
            metadata = get_image_metadata(file_path)
            date_taken = metadata.get('EXIF DateTimeOriginal', None)
            if date_taken:
                date_taken = datetime.strptime(str(date_taken), '%Y:%m:%d %H:%M:%S')
                target_folder = os.path.join(base_path, str(date_taken.year), str(date_taken.month))
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))

def organize_images_camera_model(base_path):
    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)
        if os.path.isfile(file_path):
            metadata = get_image_metadata(file_path)
            camera_model = metadata.get('Image Model', 'Unknown')
            target_folder = os.path.join(base_path, camera_model)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))