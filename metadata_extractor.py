"""
module for extracting metadata from the image files
"""

from PIL import Image
import exifread

def extract_metadata(image_path):
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)
    return tags

def get_image_metadata(image_path):
    image = Image.open(image_path)
    metadata = {
        "File Name": image.filename,
        "Format": image.format,
        "Mode": image.mode,
        "Size": image.size
    }
    exif_data = extract_metadata(image_path)
    for tag in exif_data.keys():
        metadata[tag] = exif_data[tag]
    return metadata