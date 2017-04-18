import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Raspberry Pi software SPI config:
# SCLK = 4
# DIN = 17
# DC = 23
# RST = 24
# CS = 8

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=70)

disp.display()
time.sleep(2.0)

# Clear display.
disp.clear()
disp.display()

# Load image and convert to 1 bit color.
#image = Image.open('happycat_lcd.ppm').convert('1')

print 'Press Ctrl-C to quit.'
while True:
	s = raw_input('Insert the image name, e.g. Bender.bmp')
	# Alternatively load a different format image, resize it, and convert to 1 bit color.
	image = Image.open(s).resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.ANTIALIAS).convert('1')
	# Display image.
	disp.image(image)
	disp.display()
	time.sleep(1.0)
