#Please install the Image package using pip install Image command
from PIL import Image
 
img = Image.open('C:/python/images/download1.png')
output = []
for col in range(img.size[0]):
    for row in range(img.size[1]):
        pixel = img.getpixel((col,row))
        if pixel[2] > 0:
            output.append((col,row))
 
for pixel in output:
    print(pixel)
