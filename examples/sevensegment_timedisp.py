import time
import datetime
from Adafruit_LED_Backpack import SevenSegment

display = SevenSegment.SevenSegment()
display.begin()
c = False

while True:
   c = True if not c else False
   now = datetime.datetime.now()
   m = now.strftime("%M")
   h = now.strftime("%I")
   tim = float(str(h)+str(m))
   display.clear()
   display.print_float(tim, decimal_digits=0)
   display.set_colon(c)
   display.write_display()
   time.sleep(1)

