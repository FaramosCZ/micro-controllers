# -------------------------------------------------------------
#
# Description:
#   This script uses the gyroscope in to axes (x,y).
#   Single LED is on, and it follows the tilt of the board, simulating movement of a ball on tilted plane
#   It has a SENSITIVITY value, which is further controlled by button A or B
#   When both A and B buttons are pressed at the same time, the debug mode starts, showing the LED
#   When NOT in debug mode, this code sends the data to another microbit board over radio
#
# -------------------------------------------------------------

from microbit import *
import radio
radio.on()

LED_X = LED_Y = 2
LAST_X, LAST_Y, LAST_Z = accelerometer.get_values()

SENSITIVITY = 100

display.clear()

DEBUG = False

while True:
    # Read the accelerometer data
    x, y, z = accelerometer.get_values()

    if x > (LAST_X + SENSITIVITY) and x > 0:
        LED_X = min(4, LED_X + 1)
        LAST_X = x
    elif x < (LAST_X - SENSITIVITY) and x < 0:
        LED_X = max(0, LED_X - 1)
        LAST_X = x

    if y > (LAST_Y + SENSITIVITY) and y > 0:
        LED_Y = min(4, LED_Y + 1)
        LAST_Y = y
    elif y < (LAST_Y - SENSITIVITY) and y < 0:
        LED_Y = max(0, LED_Y - 1)
        LAST_Y = y

    if button_a.is_pressed() and button_b.is_pressed():
        if DEBUG is True:
            DEBUG = False
            display.clear()
        else:
            DEBUG = True
        sleep(1000)
    elif button_a.is_pressed():
        SENSITIVITY = max(0, SENSITIVITY-10)
        print(SENSITIVITY)
        sleep(100)
    elif button_b.is_pressed():
        SENSITIVITY = min(1000, SENSITIVITY+10)
        print(SENSITIVITY)
        sleep(100)

    if DEBUG:
        # Turn off all LEDs
        display.clear()
        # Turn on the LED at coordinates
        display.set_pixel(LED_X, LED_Y, 9)

    # Send LED coordinates through radio
    radio.send("LED:{}:{}".format(LED_X, LED_Y))
