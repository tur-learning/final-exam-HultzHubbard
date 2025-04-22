## How to use code:

# configure code
config.json holds details of which models to use and weither to use processed or raw images
    - When running main.py file, user will be prompted to input this information and rest of programs will be base on this information

# functions
main.py file contains main program code
dust3r.py contains the API code for dust3r
mast3r.py contains the API code for mast3r
preprocess_image.py contains the API code for processing the images and removing the backgrounds
download_images.py downloads the raw images from photos.zip
utils.py  contains utilities
    - extracts information from json files so the config.json file can be used
    - converts png fils to jpg
    - turns a file into a zip

# store and view retreived 3D model
model.glb holds the 3D model after the API retreive the final result
viewer.html can be used to view the model (enter "python -m http.server" in terminal and follow instructions)