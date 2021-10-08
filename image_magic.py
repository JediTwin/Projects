# Image Magic
# Load an image and manipulate the pixels

from PIL import Image


# Load the image (pumpkin)
image = Image.open('./halloween-unsplash.jpg')
output_image = Image.open('./halloween-unsplash.jpg')

# Grab pixel information
a_pixel = image.getpixel((0, 0)) # Grab pixel (0, 0) top-left

# Iterate over every pixel
image_width = image.width
image_height = image.height

# Modify the image to convert it to grayscale
# (r, g, b) --> (?, ?, ?)
# Take the r, g, b, add them up and divide by 3
# replace r g b with the average

# Top to bottom
for y in range(image_height):
    # Left to right
    for x in range(image_width):
        # Grab pixel information for THIS pixel
        pixel = image.getpixel((x, y))

        # grab r g b
        red, green, blue = pixel

        # calculate the average
        average = int((red + green + blue) / 3)

        # create new pixel
        gray_pixel = (average, average, average)

        # put that in new image
        output_image.putpixel((x, y), gray_pixel)

output_image.save('grayscale.jpg')
