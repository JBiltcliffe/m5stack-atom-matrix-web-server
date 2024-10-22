from m5stack import *
from m5ui import *
from uiflow import *
import network
import socket

#set corners to blue to show code is active
rgb.set_screen([0x0000ff,0,0,0,0x0000ff,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0x0000ff,0,0,0,0x0000ff])

#set up and connect to wifi
wlan = network.WLAN(network.STA_IF)
wlan.ifconfig(('192.168.1.240', '255.255.255.0', '192.168.0.254', '8.8.8.8'))  #remove this line for DHCP 
wlan.active(True)
wlan.connect('Wifi SSID', 'Wifi Password')

#set corners to orange while awaiting wifi connection
while not wlan.isconnected():
  rgb.set_screen([0xff8000,0,0,0,0xff8000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0xff8000,0,0,0,0xff8000])

#when wifi connected make corners green
rgb.set_screen([0x00ff00,0,0,0,0x00ff00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0x00ff00,0,0,0,0x00ff00])

#set up web server socket
addr = socket.getaddrinfo('192.168.1.240', 80)[0][-1]  #IP address of the Matrix needs to be entered here
s = socket.socket()
s.bind(addr)
s.listen(5)

request_state="NULL" 

#main loop for responding to web page request
while True:
  cl, addr = s.accept()
  request = cl.recv(1024)
  request = str(request)
  led_red = request.find('/?led=red')
  led_green = request.find('/?led=green')
  led_off = request.find('/?led=off')
  if led_red == 6 :
    request_state="RED"
    rgb.setColorAll(0xff0000)
  elif led_green == 6 :
    request_state="GREEN" 
    rgb.setColorAll(0x00ff00)
  elif led_off == 6 :
    request_state="OFF" 
    rgb.setColorAll(0x000000)
  else :
    request_state="Unknown" 


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
        .green_button {background-color: #00ff00;}
        .off_button {background-color: #000000;}
      </style>
    </head>
    <body>
      <h1>M5Stack Web Server</h1> 
      <p>LED State: <strong>""" + request_state + """</strong></p>	
      <p><a href="/?led=red"><button class="button red_button">RED</button></a>
        <a href="/?led=green"><button class="button green_button">GREEN</button></a></p>
      <p><a href="/?led=off"><button class="button off_button">OFF</button></a></p>
    </body>
    </html>
  """


  cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
  cl.send(html)
  cl.close()