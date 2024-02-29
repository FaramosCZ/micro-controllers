from machine import Pin
import utime
import time

# In-built LED
led = Pin("LED", Pin.OUT)
led.value(0)

# SR505 sensor connected to:
#   GPIO Pin 0; GND; VSYS (needs 5V for correct operation)
PIR_PIN = 0
pir_sensor = Pin(PIR_PIN, Pin.IN)

MOVEMENT_REPORTED = 0

# Main loop
while True:

    # 1 sec is set just for debug purposes
    utime.sleep_ms(1000)

    # Check if motion is detected (rising edge)
    if pir_sensor.value() == 1 and MOVEMENT_REPORTED == 0:
        MOVEMENT_REPORTED = 1
        print("A")
        print("Motion detected!")
        print(time.localtime())
        led.value(1)

    elif pir_sensor.value() == 1 and MOVEMENT_REPORTED == 1:
        print("B")

    else:
        print("C")
        MOVEMENT_REPORTED = 0
        led.value(0)
