"""
Generate HTML graphics for the sensor values
"""
import DBInterface
from datetime import datetime
from dateutil import tz
import plotly
from plotly.graph_objs import Scatter, Layout
from sense_hat import SenseHat

# Read values from database
db = DBInterface.Database('/home/pi/Projects/sensehat/sensehat.db')
results = db.Execute("SELECT today, timeofday, pressure, temperature, humidity FROM pth;")

date = []
pressure = []
temperature = []
humidity = []
for today, time, pre, temp, hum in results:
    date.append( datetime.strptime("%s %s" %(today, time), '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz.gettz('UTC')).astimezone(tz.tzlocal()) )
    pressure.append(pre)
    temperature.append(temp)
    humidity.append(hum)

# Generate plots
pressureGraph = plotly.offline.plot({"data": [Scatter(x=date, y=pressure)],
                                "layout": Layout(title="Pressure", height=450, yaxis=dict(title='hPa'))},
                               output_type='div', filename='pressure.html',
                               #image_height = 450, image_width = 200,
                               include_plotlyjs=False)

temperatureGraph = plotly.offline.plot({"data": [Scatter(x=date, y=temperature)],
                                   "layout": Layout(title="Temperature", height=450, yaxis=dict(title='Celsus'))},
                                  output_type='div', filename='temperature.html',
                                  #image_height = 450, image_width = 200,
                                  include_plotlyjs=False)

humidityGraph = plotly.offline.plot({"data": [Scatter(x=date, y=humidity)],
                                "layout": Layout(title="Humidity", height=450, yaxis=dict(title='%'))},
                               output_type='div', filename='humidity.html',
                               #image_height = 450, image_width = 200,
                               include_plotlyjs=False)

pressureOnlineGraph = plotly.plotly.plot({"data": [Scatter(x=date, y=pressure, name='pressure'), Scatter(x=date, y=temperature, name='temperature'), Scatter(x=date, y=humidity, name = 'humidity')]}, filename='pressure', fileopt='overwrite', auto_open=False)

# DOM
body = """
<html>
<head>
<script src="plotly-latest.min.js"></script>
<title>Raspberry Pi 2</title> 
<style>    
   body {         
      width: 1024px;         
      margin: 0 auto;         
      font-family: Tahoma, Verdana, Arial, sans-serif;     
      } 
</style> 
</head>
<body>
<h1> Sensors values </h1>
<p> Last update: %s </p>
%s
<a href=%s> Link to pressure plot </a>
%s
%s
</body>
</html>
""" % (datetime.now().strftime("%d-%m-%Y %H:%M:%S"), pressureGraph, pressureOnlineGraph, temperatureGraph, humidityGraph)

index = open('/var/www/html/index.html', 'w')
index.writelines(body)
index.close()

# Write that everything went well
sense = SenseHat()
sense.show_message("Webpage updated", scroll_speed=0.1, text_colour = [0, 255, 0])
sense.clear()
