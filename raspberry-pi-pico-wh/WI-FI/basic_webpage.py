# -------------------------------------------------------------
#
# Description:
#   Connect to a Wi-Fi network nearby, serves a webpage
#
# -------------------------------------------------------------

import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

ssid = '<SSID OF MY WI-FI>'
password = '<PASSWORD FOR MY WI-FI>'

def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()
