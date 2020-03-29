# followed here
# https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/bread-board-setup-for-input-buttons

from gpiozero import Button
from signal import pause
from os import system;

print ('Program is starting ... ')


button1 = Button(23) # define Button pin according to BCM Numbering
button2 = Button(24)
button3 = Button(25)

def onButton1Pressed():
    print("Button 1 is pressed")
    system('omxplayer temple-bell.mp3 &')

def onButton2Pressed():
    print("Button 2 is pressed")
    system('omxplayer temple-bell-bigger.mp3 &')

def onButton3Pressed():
    print("Button 3 is pressed")
    system('omxplayer temple-bell-huge.mp3 &')

button1.when_pressed = onButton1Pressed
button2.when_pressed = onButton2Pressed
button3.when_pressed = onButton3Pressed

pause()
