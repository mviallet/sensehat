"""
Examples of using the Sense HAT python library: Sensing the environment

Ref: https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat
"""

# Import the Sense HAT python interface
from sense_hat import SenseHat

# Instantiate an interface witht the HAT
sense = SenseHat()

#
# Read pressure, temperature, humidity
#

# N.B.: The temperature is read from the pressure and/or humidity sensor
pressure = sense.get_pressure()
temperature = sense.get_temperature()
humidity = sense.get_humidity()

# Print the results
result = "Pre: %.1f Temp: %.1f Hum: %.1f" % (pressure, temperature, humidity)
sense.show_message(result)

#
# Sense the Inertial Measurement Unit
#

# Read the orientation of the module
# N.B.: This is read from the accelerometer
orientation = sense.get_orientation_degrees() # radians version exists too
print("Pitch {0} Roll {1} Yaw {2}".format(orientation["pitch"], orientation["roll"], orientation["yaw"]))

# Get the accelerator information in G's
accel = sense.get_accelerometer_raw()
sense.show_message("x: %.1f y: %.1f z: %1.f" % (accel["x"], accel["y"], accel["z"]))

# Show the orientation graphically
sense.show_letter("J")
x = round(accel["x"], 0)
while x < 1:
   accel = sense.get_accelerometer_raw()
   x = round(accel["x"], 0)
   y = round(accel["y"], 0)
   z = round(accel["z"], 0)

   if x==-1:
     sense.set_rotation(180)
   elif y==1:
     sense.set_rotation(90)
   elif y==-1:
     sense.set_rotation(270)
   else:
     sense.set_rotation(0)
sense.clear()

#
# Sense the joystick
#

# Print the direction, stop with down
finished = False
while not finished:
   for event in sense.stick.get_events():
      print(event.direction, event.action)
      if event.action == 'pressed':
         if event.direction == 'left':
            sense.show_letter("L")
         if event.direction == 'right':
            sense.show_letter("R")
         if event.direction == 'up':
            sense.show_letter("U")
         finished = event.direction == 'down'
sense.clear()

# Associate function with event
def pushed_up(event):
   print(event)

sense.stick_direction_up = pushed_up
