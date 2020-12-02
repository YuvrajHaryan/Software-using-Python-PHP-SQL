from PIL import Image

img = Image.open('LoadedL.jpg') # image extension .png,.jpg
new_width  = 50 # Set height as per choice
new_height = 50 # set width as per choice
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('output8.png')