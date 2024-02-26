# -------------------------------------------------------------
#
# Description:
#   This script listens in loop for a messages over radio
#   Then the message is parsed and appropriate LED is powered on
#
# -------------------------------------------------------------

from microbit import *
import radio
radio.on()

while True:
    # Try to receive data through radio
    incoming = radio.receive()

    if incoming:
        # Split the received data into parts
        parts = incoming.split(":")

        if len(parts) == 3 and parts[0] == "LED":
            # Extract LED coordinates from the received data
            led_x = int(parts[1])
            led_y = int(parts[2])

            # Display the LED coordinates
            display.clear()
            display.set_pixel(led_x, led_y, 9)
