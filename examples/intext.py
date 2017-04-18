import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=60)

# Clear display, clearing the display actually clears the buffer 
# disp.clear()

# display shows default buffer
disp.display()

time.sleep(3.0)

#Clear display buffer and then display
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

# Load font
font = ImageFont.truetype('ka1.ttf', 10)

# Write some text.
draw.text((4,4), 'Hello World!', font=font)

# Display image.
disp.image(image)
disp.display()

print 'Press Ctrl-C to quit.'
while True:
	s=[]
	print 'Enter the text you wish to show on Nokia PCD.'
	# A for loop for 4 lines of input each in one space of the "s" array 
	for i in range(4):
		s.append(raw_input('Line '+str(i)+': ')) 
 
	# Draw a white filled box to clear the image.
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	# Clearing screen before writing new string
	disp.clear()
	disp.display()
	# String to image using font
	for i in range(4):
		draw.text((2,2+11*i), s[i], font=font)

	disp.image(image)
	# displaying image
	disp.display() 
	time.sleep(1.0)
