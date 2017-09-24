"""
Testing the Sense HAT python library: LED matrix
"""
# Import various modules
from time import sleep
from numpy.random import randint

# Import the Sense HAT Python library
from sense_hat import SenseHat

# Create a SenseHat object
sense = SenseHat()

# Create a nice background color
nice_background = (100, 50, 50)

# Change the orientation of the matrix
sense.set_rotation(90)
#sense.flip_h()
#sense.flip_v()

# Show a message on the LED matrix
sense.show_message("Hello World!", scroll_speed=0.1, 
		   text_colour = [255, 255, 255], back_colour = nice_background)

# Erase everything
sense.clear()

# Show a single character
sense.show_letter("Z", text_colour = [255, 0, 0])

# Show a simple message
for c in "Maxime":
   sense.show_letter(c, text_colour = [255, 0, 0])
   sleep(0.5)
sense.clear()

# Set individual pixels. Here we identify the four corners of the matrix.
sense.set_pixel(0, 0, (0, 0, 255))
sense.set_pixel(0, 7, (0, 255, 0))
sense.set_pixel(7, 0, (255, 0, 0))
sense.set_pixel(7, 7, (255, 255, 255))

# Set all pixels at the same time
for k in range(5):
   pixels = randint(255, size=(64, 3))
   sense.set_pixels(pixels)
   sleep(0.5)
sense.clear()

