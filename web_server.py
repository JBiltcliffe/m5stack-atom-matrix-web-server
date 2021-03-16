from m5stack import *
from m5ui import *
from uiflow import *
import network

rgb.set_screen([0x0000ff,0,0,0,0x0000ff,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0x0000ff,0,0,0,0x0000ff])

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wifi SSID', 'Password')

rgb.set_screen([0x00ff00,0,0,0,0x00ff00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0x00ff00,0,0,0,0x00ff00])


import machine
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]




import socket
addr = socket.getaddrinfo('192.168.1.213', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(5)

request_state="NULL" 

while True:
  cl, addr = s.accept()
  request = cl.recv(1024)
  request = str(request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6 :
    request_state="ON"
    rgb.setColorAll(0xff0000)
  elif led_off == 6 :
    request_state="OFF" 
    rgb.setColorAll(0x000000)
  else :
    request_state="NULL" 


  html = """<html>
    <head> 
      <title>M5Stack Atom Matrix Web Server</title> 
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="icon" href="data:,"> 
      <style>
        html {font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
			  h1 {color: #0F3376; padding: 2vh;}
			  p {font-size: 1.5rem;}
			  .button{background-color: #00aa00; display: inline-block; border: none; 
			   border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; 
			   font-size: 30px; margin: 2px; cursor: pointer;} 
        .red_button {background-color: #ff0000;}
        .green_button {background-color: #ff00ff;}
        .off_button {background-color: #000000;}
      </style>
    </head>
    <body>
      <h1>M5Stack Web Server</h1> 
      <p>Response: <strong>""" + request_state + """</strong></p>	
      <p><a href="/?led=on"><button class="button red_button">RED</button></a></p>
      <p><a href="/?led=off"><button class="button off_button">OFF</button></a></p>
    </body>
    </html>
  """


  cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
  cl.send(html)
  cl.close()