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
    - dowload the content of a zip file to a folder for usage
    - add a photo to dowloads so they can be used in the code
    - delete an unwanted photo
    - function to configure program parameters 

# store and view retreived 3D model
model.glb holds the 3D model after the API retreive the final result
viewer.html can be used to view the model (enter "python -m http.server" in terminal and follow instructions)

# Flow
1. downloads pictures from photos.zip
2. gets user input on if there are new zip files to download
3. gets user input on if there are photos they want to add or delete from the relevent files for the program
4. resets config.json to default (everything false)
5. user inputs whether they want to process images first or not
6. user inputs whether they want to use dust3r or mast3r 3D image generators
7. computer uses inputs to determin whether or not to process images and which generator to use
8. path determined by the computer is then executed
9. result is stored in model.glb
10. run "python -m http.server"