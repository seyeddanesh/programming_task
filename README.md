# Introduction 
The purpose of this exercise is assess you comfort in using python to manipulate images.
The exercise has two initial core tasks, and one additional optional task. We have 
provided functions to read an image from disk and display it on the screen,
so you will not need to do this yourself.

# Setup 
Install the dependencies listed in requirements.txt (imageio, matplotlib, and numpy).
You can do this in a bash terminal by running:
```
pip install -r requirements.txt
```

# Core Task 
## Part 1 - Draw Circle
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
## Part 2 - Draw Equilateral Triangle
Similar to Part 1, but this time we ask that you write a function that draws a random triangle instead
of a circle.
- The input image is the same, a numpy array of uint8 with shape (height, width, 3).
- The image is RGB.
- The triangle that will be drawn should have 3 equal sides (A equilateral triangle)
- The trangle should have a random size, and random rotation
- The function should pick a random side length for the triangle which will be at least a size equal
to 10 pixels in length and at most a size equal to the height of the image.
- The random side length must be drawn from a uniform (flat) distribution.
- The orientation of the triangle should be chosen at random from a uniform distribution
- The function should pick a random location in the image which will be the center point of the
  triangle.
- The triangle must fit entirely within the image.
- The function should return a new image, leaving the input image unaltered.
- The triangle must be filled with black.

# Extra Task 
If you would like to, you can make the circle drawing function (Part 1) more complicated.
This will show us more of your skills, and give us more to talk about if we proceed to interview.
This is NOT required. If you do just the core parts this will still meet our minimum threshold.
Make a new function similar to the add_circle that:
- Draw multiple circles that don't touch.
- The number of circles is randomly chosen between 1 and 10.
- Each circle is drawn to the same specifications as defined above (random radius and location).

# Implement and Run

Modify the add_circle and add_triangle function in the code, and to run, from the terminal:
```
python modify_image.py
```
If you run as is, the function currently returns the input image unmodified.
