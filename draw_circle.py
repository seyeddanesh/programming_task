"""
################
# Introduction #
################

The purpose of this exercise is to check that you can perform tasks using Python and numpy.

The exercise has a core part and optional extras.

Submitting just the core part is absolutely fine.
If, however, if you are enjoying the task and have spare time (we know that people are busy and not
everyone will) then you can expand the code by adding extra features. This is detailed below.

We have provided functions to read an image from disk and display it on the screen,
so you will not need to do this yourself.


#########
# Setup #
#########

Install the dependencies listed in requirements.txt (imageio, matplotlib, and numpy).
You can do this in a bash terminal by running:
   pip install -r requirements.txt


#############
# Core Task #
#############

The task is to write a function that takes an image as input and draws a circle somewhere on it.

There are image processing libraries that have functions to do this (like opencv or Pillow) but we
would like to see if you can do it yourself using numpy and the Python standard library.

- The input image is a numpy array of uint8 with shape (height, width, 3).
- The image is RGB.
- The function should pick a random diameter for the circle which will be at least 10 pixels and at
  most the height of the image.
- The random diameter must be drawn from a uniform (flat) distribution.
- The function should pick a random location in the image which will be the center point of the
  circle.
- The circle must fit entirely within the image.
- The function should return a new image, leaving the input image unaltered.
- The circle must be filled with black.


##########
# Extras #
##########

If you would like to, you can make the function more complicated.
This will show us more of your skills, and give us more to talk about if we proceed to interview.
This is NOT required. If you do just the core part this will still meet our minimum threshold.

Make a new function for these, so we can still look at your original.

- Fill the circle with blue, instead of black.
- Fill the circle with a gradient, black in the middle and blue at the edge, varying linearly.
- Draw muiltiple circles that don't touch.
  The number of circles is randomly chosen between 1 and 10.
  Each circle is drawn to the same specifications as defined above (random radius and location).
"""


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

    #TODO: Re-define the task here.

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
    display_rgb_image(altered_image)
