#!/usr/bin/python
from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO
import time
#-------------------------------------------------------
# initialize the bus and device /dev/spidev1.0
spi0 = SPI(0,0)     #ADC
# initialize the bus and device /dev/spidev2.0
spi1 = SPI(1,0)     #DAC
#-------------------------------------------------------
#Set the maximum clock frequency
spi0.msh=100000
spi1.msh=100000
#-------------------------------------------------------
# mnemonics for GPIO
RST = "P9_26"
CLR = "P9_25"
LDAC = "P9_24"
BUSY = "P9_20"
CNV = "P9_23"
PWR_SYS = "P9_16"
#PWR_SYS = "P9_15"
#-------------------------------------------------------
# defining outputs
GPIO.setup(RST, GPIO.OUT)
GPIO.setup(CLR, GPIO.OUT)
GPIO.setup(LDAC, GPIO.OUT)
GPIO.setup(CNV, GPIO.OUT)
GPIO.setup(PWR_SYS, GPIO.OUT)
#-------------------------------------------------------
# defining inputs
GPIO.setup(BUSY, GPIO.IN)
#-------------------------------------------------------
# initialization of outputs
GPIO.output(RST, GPIO.LOW)
GPIO.output(CLR, GPIO.LOW)
GPIO.output(LDAC, GPIO.LOW)
GPIO.output(CNV, GPIO.LOW)
GPIO.output(PWR_SYS, GPIO.LOW)
#=======================================================
#	pinout for DAC and ADC bus
#=======================================================
'''
DAC pins
	SPI1_CS:	"P9_28"
	SPI1_SCLK:	"P9_31"
	SPI1_MOSI:	"P9_29"
	SPI1_MISO:	"P9_30"
	GPIO_RST:	"P9_26"
	GPIO_CLR:	"P9_25"
	GPIO_LDAC:	"P9_24"

ADC pins
	SPI0_CS:	"P9_17"
	SPI0_SCLK:	"P9_22"
	SPI0_MISO:	"P9_18"
	GPIO_BUSY:	"P9_20"
	GPIO_CNV:	"P9_23"

GPIO pins
	GPIO_0: "P9_11"
	GPIO_1: "P9_12"
	GPIO_2: "P9_13"
	GPIO_3: "P9_14"

	GPIO_4: "P8_11"
	GPIO_5: "P8_12"
	GPIO_6: "P8_13"
	GPIO_7: "P8_14"

POWER SYSTEM:
	PWR_SYS = "P9_16"
'''
#=======================================================
#	testing SPI
#=======================================================

while(1):
	# RST = 1 --> address
#	GPIO.output(RST, GPIO.HIGH)
#	time.sleep(0.001)
	# RST = 0 --> slaves
#	GPIO.output(RST, GPIO.LOW)
#	time.sleep(0.001)

	# send data through SPI
	spi1.writebytes([0x20, 0x03, 0x12])
	spi0.writebytes([0x02, 0x30, 0x21])

#	GPIO.output(PWR_SYS, GPIO.HIGH)
#	GPIO.output(RST, GPIO.HIGH)
#	GPIO.output(CLR, GPIO.HIGH)
#	GPIO.output(LDAC, GPIO.HIGH)
#	GPIO.output(CNV, GPIO.HIGH)

#	GPIO.output(PWR_SYS, GPIO.LOW)
#	GPIO.output(RST, GPIO.LOW)
#	GPIO.output(CLR, GPIO.LOW)
#	GPIO.output(LDAC, GPIO.LOW)
#	GPIO.output(CNV, GPIO.LOW)
