# -------------------------------------------------------------
#
# Description:
#   Prints out version of the language and version of the board
#
# -------------------------------------------------------------

import sys
import os

print("MicroPython version:", sys.version)
print("Micro:bit firmware version:", os.uname().release)

