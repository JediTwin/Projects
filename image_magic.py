# Image Magic
# Load an image and manipulate the pixels

from PIL import Image


def to_greyscale(pixel: tuple, algo="average") -> tuple:
    """Convert a picture into greyscale.
    Can also specify the greyscale algorithm.

    Args:
        pixel: a 3-tuple of ints from 0-255, e.g. (140, 120, 255)
            represents (red, green, blue)
        algo: the greyscale conversion algorithm
        specified by user
        valid values are "average", "luma"
        Defaults to "average"

    Returns:
        a 3-tuple pixel (r, g, b) in greyscale
    """
    red, green, blue = pixel

    # calculate the grey pixel
    if algo.lower() == "luma":
        grey = int(red * 0.3 + green * 0.59 + blue * 0.11)

    else:
        grey = int((red + green + blue) / 3)

    return grey, grey, grey

def brighter(pixel: tuple, magnitude: int) -> tuple:
    """ Increases the brightness of a pixel

    Args:
        pixel a 3-tuple of (red, green, blue) subpixels

        magnitude: an int from 0-255 that indicates how much to increase brightness

    Returns:
        a 3-tuple representing a brighter pixel
    """
    # break down the pixel into subpixels
    red, green, blue = pixel

    MAX = 255

    if red + magnitude > MAX:
        red = MAX
    else:
        red += magnitude

    if green + magnitude > MAX:
        green = MAX
    else:
        green += magnitude

    if blue + magnitude > MAX:
        blue = MAX
    else:
        blue += magnitude

    return red, green, blue


# Load the image (pumpkin)
image = Image.open('./halloween-unsplash.jpg')
output_image = Image.open('./halloween-unsplash.jpg')

# Grab pixel information
a_pixel = image.getpixel((0, 0))  # Grab pixel (0, 0) top-left

# Iterate over every pixel
image_width = image.width
image_height = image.height

# Modify the image to convert it to grayscale
# (r, g, b) --> (?, ?, ?)
# Take the r, g, b, add them up and divide by 3
# replace r g b with the average

# # top to bottom
# for y in range(image_height):
#     # Left to right
#     for x in range(image_width):
#         # Grab pixel information for THIS pixel
#         pixel = image.getpixel((x, y))
#
#         # call to_greyscale
#         grey_pixel = to_greyscale(pixel, "average")
#
#         # put that in new image
#         output_image.putpixel((x, y), grey_pixel)
#
# output_image.save(f'greyscale2.jpg')

# top to bottom
for y in range(image_height):
    # Left to right
    for x in range(image_width):
        # Grab pixel information for THIS pixel
        pixel = image.getpixel((x, y))

        brighter_pixel = brighter(pixel, 50)

        output_image.putpixel((x, y), brighter_pixel)

output_image.save('brighterer.jpg')
