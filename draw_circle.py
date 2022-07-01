import imageio.v3 as iio
import matplotlib.pyplot as plt
import numpy as np


def read_rgb_image(path):
    """
    Get an image from disk and return as a numpy array.

    Arguments
    ---------
    path: a str or pathlib.Path object.

    Returns
    -------
    A numpy array of shape (height, width, 3) and dtype np.uint8.
    """
    img = iio.imread(str(path))
    if img is None:
        raise RuntimeError("Could not open file at " + str(path))
    return img


def display_rgb_image(image):
    """
    Display an image on the screen.

    To close the image, go to the terminal where the program is running and press Enter.

    Arguments
    ---------
    image: a numpy array of shape (height, width, 3) and dtype np.uint8.

    Returns
    -------
    None
    """
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.show()
    input("Press Enter to continue.")


def add_circle(image):
    """
    Add a circle to an image.

    The task is to write a function that takes an image as input and draws a circle
    somewhere on it.
    
    There are image processing libraries that have functions to do this (like opencv or
    Pillow) but we would like to see if you can do it yourself using numpy and the Python
    standard library.
    
    - The input image is a numpy array of uint8 with shape (height, width, 3).
    - The image byte order is RGB.
    - Your function should pick a random diameter for the circle which will be at minimum
      10 pixels and at most the height of the image.
    - The random diameter must be selected from a uniform (flat) distribution.
    - Your function should pick a random location in the image which will be the center
      point of the circle.
    - The circle must fit entirely within the image.
    - The function should return a new image, leaving the input image unaltered.
    - The circle must be filled with black.

    Arguments
    ---------
    image: a numpy array of shape (height, width, 3) and dtype np.uint8.

    Returns
    -------
    A numpy array of shape (height, width, 3) and dtype np.uint8.
    """
    
    return image



if __name__ == "__main__":
    input_image = read_rgb_image("input.png")
    altered_image = add_circle(input_image)
    display_rgb_image(altered_image)

