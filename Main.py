"""
Main Program
- Establish connection with the database
- Read the sensors
- Commit readings to the database
"""
import DBInterface
from sense_hat import SenseHat
import socket

# Interface with the Sense HAT
sense = SenseHat()

# Read the sensors
temp = sense.temperature
pre = sense.pressure
hum = sense.humidity

# Connect to the database
db = DBInterface.Database('/home/pi/Projects/sensehat/sensehat.db')

# Write the data
db.Execute("INSERT INTO pth VALUES(date('now'), time('now'), ?, ?, ?, ?, ?)",
           (round(temp, 2), round(pre, 2), round(hum, 2), 'Living Room', socket.gethostname()) )

# Commit the changes and close
db.Commit()
db.Close()

# Write that everything went well
sense.show_message("DB Written", scroll_speed=0.1, text_colour = [255, 255, 255])
sense.clear()
