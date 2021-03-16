# m5stack-atom-matrix-web-server

This is a simple web server application to be run on a M5Stack Atom Matrix device to allow the user to control the LEDs via a simple web page or via an http get.  Currently it supports setting all the LEDs to green, red or off, however it would be very easy to extend to other colours or add pre-defined patterns if required.

The device will act as a wifi client and connect to the wifi specified in the main file.  Other systems can control the LEDs by doing a simple http get to the following:

http://[IP of device]/?led=red    - sets all LED's to red

http://[IP of device]/?led=green  - sets all LED's to green

http://[IP of device]/?led=off    - sets all LED's off

With thanks to the following example (https://community.m5stack.com/topic/1847/atom-matrix-basic-working-access-point-micropython) which formed the basis for this version, however that was acting as an access point and only set LEDs on or off where this version connects to an existing wifi connection allowing it to be controlled over http by other devices on the network. 
