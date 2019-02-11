#!/usr/bin/python
from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO
#-------------------------------------------------------
# initialize the bus and device /dev/spidev1.0
spi = SPI(0,0)
# mnemonics for GPIO
RS = "P9_26"
# defining outputs
GPIO.setup(RS, GPIO.OUT)
# initialization of outputs
GPIO.output(RS, GPIO.LOW)

#=======================================================

# RS = 0 --> data to devices
# RS = 1 --> select address

# select the device inside the board
# address 0: 0x0__
# address 1: 0x9__
# address 2: 0xA__
# address 3: 0x3__
# address 4: 0xC__
# address 5: 0x5__
# address 6: 0x6__
# address 7: 0xF__

# select the board in the stack
# device 0: 0x__0 (DAC)
# device 1: 0x__9 (ADC)
# device 2: 0x__A (FLASH)
# device 3: 0x__3 (Digital Port A)
# device 4: 0x__C (Digital Port B)
# device 5: 0x__5 (decoder: other functionalities)
# device 6: 0x__6 (flip-flops' CLK)
# device 7: 0x__F (board type)

# other functionalities
# decoder 0: 0x__0 (turn ON  DAC circuit)
# decoder 1: 0x__9 (turn OFF DAC)
# decoder 2: 0x__A (turn ON  ADC circuit)
# decoder 3: 0x__3 (turn OFF ADC circuit)
# decoder 4: 0x__C (preset of CLR and RESET FFs)
# decoder 5: 0x__5 (DAC clear)
# decoder 6: 0x__6 (DAC reset)
# decoder 7: 0x__F (--unused--)

#=======================================================
#	select address
#=======================================================
def address(value):
	#spi.mode = 1
	# store the device selected
	global device
	device = "{:02x}".format(value)

	# RS = 1 --> address
	GPIO.output(RS, GPIO.HIGH)
	# select device
	spi.writebytes([value])
	# RS = 0 --> slaves
	GPIO.output(RS, GPIO.LOW)
#=======================================================
#	select DAC address
#=======================================================
# from datasheet: SPI mode 1 and 2 supported
# in practical aspects (with CPLD correction): SPI modes 1, 2 and 3 supported
def dac(board):
	#spi.mode = 1
	if(board%8 == 0):
		address(int("00", 16))
	elif(board%8 == 1):
		address(int("90", 16))
	elif(board%8 == 2):
		address(int("A0", 16))
	elif(board%8 == 3):
		address(int("30", 16))
	elif(board%8 == 4):
		address(int("C0", 16))
	elif(board%8 == 5):
		address(int("50", 16))
	elif(board%8 == 6):
		address(int("60", 16))
	elif(board%8 == 7):
		address(int("F0", 16))
# =======================================================
#	select ADC address
# =======================================================
# SPI mode 0 and 3 supported natively
# in practical aspects (with CPLD correction): SPI mode 1 supported
def adc(board):
	#spi.mode = 1
	if(board%8 == 0):
		address(int("09", 16))
	elif(board%8 == 1):
		address(int("99", 16))
	elif(board%8 == 2):
		address(int("A9", 16))
	elif(board%8 == 3):
		address(int("39", 16))
	elif(board%8 == 4):
		address(int("C9", 16))
	elif(board%8 == 5):
		address(int("59", 16))
	elif(board%8 == 6):
		address(int("69", 16))
	elif(board%8 == 7):
		address(int("F9", 16))
# =======================================================
#	select FF (for powering DAC and ADC)
# =======================================================
def clk_ff(board):
	#spi.mode = 1
	if(board%8 == 0):
		address(int("0A", 16))
	elif(board%8 == 1):
		address(int("9A", 16))
	elif(board%8 == 2):
		address(int("AA", 16))
	elif(board%8 == 3):
		address(int("3A", 16))
	elif(board%8 == 4):
		address(int("CA", 16))
	elif(board%8 == 5):
		address(int("5A", 16))
	elif(board%8 == 6):
		address(int("6A", 16))
	elif(board%8 == 7):
		address(int("FA", 16))
	# generate CLK pulse
	spi.writebytes([0x00])
# =======================================================
#	select DIGITAL PORT A (always INPUT)
# =======================================================
#def PA(board):
def gpioAB(board):
	#spi.mode = 1
	if(board%8 == 0):
		address(int("03", 16))
	elif(board%8 == 1):
		address(int("93", 16))
	elif(board%8 == 2):
		address(int("A3", 16))
	elif(board%8 == 3):
		address(int("33", 16))
	elif(board%8 == 4):
		address(int("C3", 16))
	elif(board%8 == 5):
		address(int("53", 16))
	elif(board%8 == 6):
		address(int("63", 16))
	elif(board%8 == 7):
		address(int("F3", 16))
	#spi.mode = 0
# =======================================================
#	select DIGITAL PORT B (either INPUT or OUTPUT)
# =======================================================
#def PB(board):
def gpioCD(board):
	#spi.mode = 1
	if(board%8 == 0):
		address(int("0C", 16))
	elif(board%8 == 1):
		address(int("9C", 16))
	elif(board%8 == 2):
		address(int("AC", 16))
	elif(board%8 == 3):
		address(int("3C", 16))
	elif(board%8 == 4):
		address(int("CC", 16))
	elif(board%8 == 5):
		address(int("5C", 16))
	elif(board%8 == 6):
		address(int("6C", 16))
	elif(board%8 == 7):
		address(int("FC", 16))
	#spi.mode = 0
# =======================================================
#	select DECODER REGISTER
# =======================================================
# select the command inside decoder register
# device 0: JK-FF to power  ON DAC circuit
# device 1: JK-FF to power OFF DAC circuit
# device 2: JK-FF to power  ON ADC circuit
# device 3: JK-FF to power OFF ADC circuit
# device 4: PRESET both DAC control JK-FF (CLEAR and RESET)
# device 5: JK-FF to CLEAR DAC
# device 6: JK-FF to RESET DAC
# device 7: --not used--
def decoder(board):
	#spi.mode = 1
	if(board%8 == 0):
		address(int("05", 16))
	elif(board%8 == 1):
		address(int("95", 16))
	elif(board%8 == 2):
		address(int("A5", 16))
	elif(board%8 == 3):
		address(int("35", 16))
	elif(board%8 == 4):
		address(int("C5", 16))
	elif(board%8 == 5):
		address(int("55", 16))
	elif(board%8 == 6):
		address(int("65", 16))
	elif(board%8 == 7):
		address(int("F5", 16))
# =======================================================
#	select FLASH address
# =======================================================
# SPI mode 0 and 3 supported natively
def flash(board):
	#spi.mode = 1
	if(board%8 == 0):
		address(int("06", 16))
	elif(board%8 == 1):
		address(int("96", 16))
	elif(board%8 == 2):
		address(int("A6", 16))
	elif(board%8 == 3):
		address(int("36", 16))
	elif(board%8 == 4):
		address(int("C6", 16))
	elif(board%8 == 5):
		address(int("56", 16))
	elif(board%8 == 6):
		address(int("66", 16))
	elif(board%8 == 7):
		address(int("F6", 16))
# =======================================================
#	select BOARD TYPE register
# =======================================================
def board_ID(board):
	#spi.mode = 1
	if(board%8 == 0):
		address(int("0F", 16))
	elif(board%8 == 1):
		address(int("9F", 16))
	elif(board%8 == 2):
		address(int("AF", 16))
	elif(board%8 == 3):
		address(int("3F", 16))
	elif(board%8 == 4):
		address(int("CF", 16))
	elif(board%8 == 5):
		address(int("5F", 16))
	elif(board%8 == 6):
		address(int("6F", 16))
	elif(board%8 == 7):
		address(int("FF", 16))

	data = spi.readbytes(1)
	return data[0]
