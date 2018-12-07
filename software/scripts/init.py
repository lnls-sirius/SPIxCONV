#!/usr/bin/python
from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO
#-------------------------------------------------------
# initialize the bus and device /dev/spidev1.0
spi = SPI(0,0)
#defining mode (CPOL = 0; CPHA = 1)
spi.mode = 1
#defining speed (in bps)
spi.msh = 10000000
#-------------------------------------------------------
