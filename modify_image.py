
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

    Arguments
    ---------
    image: a numpy array of shape (height, width, 3) and dtype np.uint8.

    Returns
    -------
    A numpy array of shape (height, width, 3) and dtype np.uint8.
    """

    
    # TODO: Add your implementation here.

    return image


def add_triangle(image):
    """
    Add a equilateral triangle to an image.

    Arguments
    ---------
    image: a numpy array of shape (height, width, 3) and dtype np.uint8.

    Returns
    -------
    A numpy array of shape (height, width, 3) and dtype np.uint8.
    """
    
    # TODO: Add your implementation here.

    return image



if __name__ == "__main__":
    input_image = read_rgb_image("input.png")
    altered_image = add_circle(input_image)
    altered_image = add_triangle(altered_image)
    display_rgb_image(altered_image)

