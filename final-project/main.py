# 1
# Import necessary modules
import json
from download_images import download_google_drive_file, file_ids
from dust3r import send_request
from mast3r import make3D
from preprocess import preprocess
from utils import load_data

# To download the info from photos.zip
# for i in file_ids:
#     download_google_drive_file(i)

# ----------------------------------------------------------------------------------------------------------------------------------
# 2
# input config.json to read configurations

# Define the JSON file path
json_file = "config.json"

# Load existing JSON data
try:
    with open(json_file, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}  # If the file doesn't exist, start with an empty dictionary

# set all values to "false"
key1 = "preprocess_image"
key2 = "use_mast3r"
key3 = "use_dust3r"
value = False

# Reset JSON data
data[key1] = value
data[key2] = value
data[key3] = value

with open(json_file, "w") as file:
    json.dump(data, file, indent=4)

# ---------------------------------------------------------------------------------------------------------------------------------

# Get user input about if they want to use processed images
print("There are two factors you need to input. Please answer as indicated.\n")
key = "preprocess_image"
init = input("Would you like to use processed images (images with the background removed)? If so, enter 'yes'. Else enter 'no': ")
while init not in ["yes", "no"]:
    init = input("You must enter either 'yes' or 'no'. Would you like to use processed images (images with the background removed)?: ")
if init == "yes":
    value = True
elif init == "no":
    value = False

# Update JSON data
data[key] = value

# Save the changes
with open(json_file, "w") as file:
    json.dump(data, file, indent=4)



# Get user input about which 3D processer they want to use
init = ""
while init not in ["mast3r", "dust3r"]:
    init = input("\nWhich 3D image generator do you wish to use, mast3r or dust3r? (you must answer with either mast3r or dust3r): ")
if init == "mast3r":   
    key = "use_mast3r"
    value = True
elif init == "dust3r":
    key = "use_dust3r"
    value = True
else:
    input("Which 3D image generator do you wish to use, mast3r or dust3r? (you must answer with either mast3r or dust3r): ")

# Update JSON data
data[key] = value

# Save the changes
with open(json_file, "w") as file:
    json.dump(data, file, indent=4)

print("Information updated successfully!")

# -------------------------------------------------------------------------------------------------------------------------------------

# # 3
# # get user input on configured parameters

config = load_data("config.json")

dust3r = config.get("use_dust3r", None)
mast3r = config.get("use_mast3r", None)
preprocessing = config.get("preprocess_image", None)

print("\nStarting 3D image generation\n")

if preprocessing == False:
    if dust3r == True:
        print("\nWe are going to use dust3r APIs")
        send_request("photos.zip")
    if mast3r == True:
        print("\nWe are going to use mast3r APIs")
        make3D("raw")
elif preprocessing == True:
    print("We are going to preprocess the image to remove the background")
    preprocess()
    if dust3r == True:
        print("\nWe are going to use dust3r APIs")
        send_request("processed_images.zip")
    if mast3r == True:
        print("\nWe are going to use mast3r APIs")
        make3D("process")