# -------------------------------------------------------------
#
# Description:
#   This code demonstrate a very basic sound generation
#   Connect speaker between 'GPIO 0' and 'GND'
#
# -------------------------------------------------------------

from microbit import *

# Function to play a tone
def play_tone(pin, frequency, duration):
    pin.write_analog(512)  # Set the analog value to play a tone
    pin.set_analog_period_microseconds(int(1000000 / frequency))
    sleep(duration)
    pin.write_analog(0)  # Stop the tone
    pin.set_analog_period_microseconds(1000)

while True:
    # Play a tone on pin0
    play_tone(pin0, 440, 500)  # 440 Hz for 500 milliseconds
    sleep(500)  # Pause between tones
