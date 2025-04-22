from gradio_client import Client, handle_file
import os, shutil
from pathlib import Path
from utils import convert_png_to_jpg, zip_images
import zipfile

def preprocess():
    # This variable can be put in the config file
    root = "downloads"
    images_path = os.listdir(root)

    # Visit this page to view the possible models that can be used:
    # https://huggingface.co/spaces/KenjieDec/RemBG
    client = Client("KenjieDec/RemBG")

    preprocessed_dir = Path("preprocessed").resolve()
    # Initially removes dir
    try:
        shutil.rmtree(preprocessed_dir)
    except FileNotFoundError:
        pass  # Skips deletion if the folder isn’t found
    preprocessed_dir.mkdir(exist_ok=True)

    for idx, image in enumerate(images_path, start=1):
        try: 
            result = client.predict(
                file=handle_file(os.path.join(root, image)),
                mask="Default",
                model="u2netp", # You can change the model if you wish, or add it as a config parameter
                x=3,
                y=3,
                api_name="/inference"
            )
            print("Image processing sucessful")
        except:
            print("Image processing unsucessful")
        
        result = Path(result)
        print(result)
        print("Copying preprocessed image to 'preprocessed' directory")
        processed_filename = f"processed_image_{idx}{result.suffix}"
        shutil.copyfile(result, os.path.join("preprocessed", processed_filename))

    # Images are converted to jpg for integration with dust3r model
    convert_png_to_jpg(preprocessed_dir)

    # Delete existing processed_images.zip if it exists
    processed_zip = Path("processed_images.zip")
    if processed_zip.exists():
        processed_zip.unlink()  # Deletes the file
        
    # Create a ZIP archive of processed images
    zip_images("preprocessed", "processed_images.zip")
