# Set up raspberry pi with only your laptop
1. Format the SD Card (try this tool https://www.sdcard.org/downloads/formatter/index.html)
2. Download Raspberry Pi Imager from https://www.raspberrypi.org/downloads/
3. Install Raspbian system to SD card using Raspberry Pi Imager
4. Go to root directory of the sd card
5. Go to `<root>/Volumes/boot`
6. Create an empty file called `ssh`
7. Create a file called `wpa_supplicant.conf`
8. Enter the following into `wpa_supplicant.conf`:
    ```
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=<TWO_LETTER_ISO_COUNTRY_CODE>

    network={
        ssid="<WIFI_NETWORK_NAME>"
        psk="<WIFI_PASSWORD>"
        key_mgmt=WPA-PSK
    }
    ```
9. Eject the SD Card and insert it into Raspberry Pi
10. Start up Raspberry Pi, assuming it connects to the wifi you setup
11. (For Mac) Download "Lan Scan" from Mac App Store.
12. Scan for the Ip Address for Your Rapsberry Pi, write it down somewhere.
13. `ssh pi@<RASPBERRYPI_IP_ADDRESS>`
14. Log in with Default Password: `raspberry`

# Setup Rapsberry Pi to show desktop despite no hdmi plugged in during bootup
1. `sudo raspi-conifg`
2. select 7 for Advance Options
3. select 5 for any resolution (do not choose default)
4. `sudo poweroff`
5. Start up Rapsberry Pi again
6. `ssh pi@<RPI_IP_ADDRESS>` with password `raspberry`
7. Download VNC Viewer https://www.realvnc.com/en/connect/download/viewer/ on your laptop
8. Open VNC Viewer and enter your Rapsberry Pi IP Address
9. Enter default password `raspberry`
10. You should be able to remote desktop into your raspberrypi

Sources:
- https://www.raspberrypi.org/documentation/
- https://medium.com/@maheshsenni/setting-up-a-raspberry-pi-without-keyboard-and-mouse-headless-9359e0926807
- https://desertbot.io/blog/headless-raspberry-pi-3-bplus-ssh-wifi-setup

# Tutorial Guide
https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_Raspberry_Pi/archive/master.zip
- GPIO Pins tutorial
- Tutrial for Using vim in terminal
- Example code for manipulating hardward
- Example of hardward installations


# Connect Raspberry Pi to Bare Conductive Touch Board (which is an Arduino Leonardo)
- https://www.youtube.com/watch?v=QumIhvYtRKQ
- https://maker.pro/raspberry-pi/tutorial/how-to-connect-and-interface-raspberry-pi-with-arduino
- https://www.bareconductive.com/make/setting-up-arduino-with-your-touch-board/
    Note it is possible to install Arduino IDE into your raspberry pi
    We need to figure out what kind of output the touch boards send to Rapsberry PI
    Once we can parse the output, we can use it program the ligthing pattern on the LED Strips
- Good tutorial on LED Strip for Raspberry Pi
    https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/
- Example of LED Visualization on Piano:
    https://github.com/onlaj/Piano-LED-Visualizer


# Connect Multiple Bare Conductive Touch Board
- https://www.bareconductive.com/make/12-tracks-touch-board/

# How to access files in your rapsberry pi from your PC
https://www.youtube.com/watch?v=Cpekkzc80Do&list=PLNnwglGGYoTvy37TSGFlv-aFkpg7owWrE&index=5

# Misc in Rapsberry Pi Terminal
- `hostname -I` to get the IP Address
- `sudo raspi-config` to access the bios
- Working with File Permission https://www.dummies.com/computers/raspberry-pi/working-with-file-permissions-on-your-raspberry-pi/