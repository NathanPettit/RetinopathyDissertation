import os
import glob
from PIL import Image

current_dir = os.getcwd()
directory = os.listdir(current_dir)

#convert tif files into jpgs so tensorflow can use them
for file in glob.glob('*.tif'):
    im = Image.open(file)
    file = str(file).rstrip(".tif")
    im.save(file + '.jpg', 'JPEG')

#delete tif files once converted
for file in directory:
    if file.endswith(".tif"):
        os.remove(os.path.join(current_dir, file))