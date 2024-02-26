# -------------------------------------------------------------
#
# Description:
#   Pins 2-9 are connected to the same segment of ever 7-segment display
#   Pins 10-13 controls 4 different 7-segment displays
#
#   The trick is that they blink very fast, and the 10-13 pins control,
#   which one and only of the displays will be 'ON' at given time.
#
# -------------------------------------------------------------

import machine
import utime
import time

# ===============================

# SEGMENT pins for all display together
SEGMENT_A = machine.Pin(2, machine.Pin.OUT)
SEGMENT_A.value(1)
SEGMENT_B = machine.Pin(3, machine.Pin.OUT)
SEGMENT_B.value(1)
SEGMENT_C = machine.Pin(4, machine.Pin.OUT)
SEGMENT_C.value(1)
SEGMENT_D = machine.Pin(5, machine.Pin.OUT)
SEGMENT_D.value(1)
SEGMENT_E = machine.Pin(6, machine.Pin.OUT)
SEGMENT_E.value(1)
SEGMENT_F = machine.Pin(7, machine.Pin.OUT)
SEGMENT_F.value(1)
SEGMENT_G = machine.Pin(8, machine.Pin.OUT)
SEGMENT_G.value(1)
SEGMENT_H = machine.Pin(9, machine.Pin.OUT)
SEGMENT_H.value(1)

# ON/OFF pins for each display
DISPLAY_1 = machine.Pin(10, machine.Pin.OUT)
DISPLAY_1.value(1)
DISPLAY_2 = machine.Pin(11, machine.Pin.OUT)
DISPLAY_2.value(1)
DISPLAY_3 = machine.Pin(12, machine.Pin.OUT)
DISPLAY_3.value(1)
DISPLAY_4 = machine.Pin(13, machine.Pin.OUT)
DISPLAY_4.value(1)

# ===============================

def seg(value):

    truth_table = [
                    [1,1,1,1,1,1,0],
                    [0,1,1,0,0,0,0],
                    [1,1,0,1,1,0,1],
                    [1,1,1,1,0,0,1],
                    [0,1,1,0,0,1,1],
                    [1,0,1,1,0,1,1],
                    [1,0,1,1,1,1,1],
                    [1,1,1,0,0,0,0],
                    [1,1,1,1,1,1,1],
                    [1,1,1,1,0,1,1]
                  ]

    #print(truth_table[value])

    SEGMENT_A.value(truth_table[value][0])
    SEGMENT_B.value(truth_table[value][1])
    SEGMENT_C.value(truth_table[value][2])
    SEGMENT_D.value(truth_table[value][3])
    SEGMENT_E.value(truth_table[value][4])
    SEGMENT_F.value(truth_table[value][5])
    SEGMENT_G.value(truth_table[value][6])
    # NOT setting "dot" SEGMENT_H

# ===============================

def all_display_off():
    utime.sleep_ms(4)
    DISPLAY_1.value(1)
    DISPLAY_2.value(1)
    DISPLAY_3.value(1)
    DISPLAY_4.value(1)

# ===============================

while True:
    year, month, day, hour, mins, secs, weekday, yearday = time.localtime()

    sec_str = "0" + str(secs) if secs < 10 else str(secs)
    min_str = "0" + str(mins) if mins < 10 else str(mins)
    txt = min_str + sec_str

    for index, display in enumerate([DISPLAY_1, DISPLAY_2, DISPLAY_3, DISPLAY_4]):
        all_display_off()
        seg(int(txt[3-index]))
        display.value(0)

# ===============================
