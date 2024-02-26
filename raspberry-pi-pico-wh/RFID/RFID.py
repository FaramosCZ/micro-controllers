# -------------------------------------------------------------
#
# Description:
#   Print some info about the RFID card every time it scans one
#   Also powers up a LED during every scan
#
# -------------------------------------------------------------

from machine import Pin
from mfrc522 import MFRC522
import utime

reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

print("\nBring TAG closer...\n")

saved_card_id = ""

led = Pin(17, Pin.OUT)

while True:
    led.value(0)
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            led.value(1)
            card = int.from_bytes(bytes(uid),"little",False)
            if str(card) == saved_card_id:
                utime.sleep_ms(50)
                continue
            saved_card_id = str(card)
            print("CARD ID: "+saved_card_id)
            utime.sleep_ms(50)
