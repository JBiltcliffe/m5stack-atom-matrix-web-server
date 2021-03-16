from m5stack import *
from m5ui import *
from uiflow import *
import network

rgb.set_screen([0x0000ff,0,0,0,0x0000ff,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0x0000ff,0,0,0,0x0000ff])

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('gloopy2', 'joannaisbeautiful')

rgb.set_screen([0x00ff00,0,0,0,0x00ff00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0x00ff00,0,0,0,0x00ff00])


import machine
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]


html = """<!DOCTYPE html>
<html>
 <head> <title>ESP8266 Pins</title> </head>
 <body> <h1>ESP8266 Pins</h1>
 <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
 </body>
</html>
"""

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




  cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
  cl.send(html)
  cl.close()