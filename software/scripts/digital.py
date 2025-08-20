#!/usr/bin/python3

from Adafruit_BBIO.SPI import SPI
#import Adafruit_BBIO.GPIO as GPIO
#-------------------------------------------------------
import selection
# initialize the bus and device /dev/spidev1.0
spi = SPI(0,0)
#-------------------------------------------------------
# initialization of variables
device = "11"

# port A: always INPUT
# port B: defined by DIP_witch
#			--> if SW1 = off: OUTPUT
#			--> if SW1 =  on: INPUT
#=======================================================
#	WRITE value in DIGITAL PORT
#=======================================================
def write(value):
	spi.writebytes([value])
#=======================================================
#	READ value in DIGITAL PORT
#=======================================================
def read():
	data = spi.readbytes(1)
	return hex(data[0])
#=======================================================
#	CHECK if digital ports are working fine
#=======================================================
def check():
	# this function will write digital values (from 0x00
	# until 0xFF) in the output of digital ports A, and
	# then read with the respective input of the digital
	# ports B
	count = 0
	it = 0
	while(1):
		for dig in range(0, 256):
			# select board 0, port B (OUT)
			selection.PB(0)
			write(dig)
			#---------------------------
			# select board 1, port B (OUT)
			selection.PB(1)
			write(dig)
			#---------------------------
			# select board 2, port B (OUT)
			selection.PB(2)
			write(dig)
			#---------------------------
			# select board 3, port B (OUT)
			selection.PB(3)
			write(dig)
			#===========================
			# select board 0, port A (IN)
			selection.PA(0)
			check = read()
			if (check == dig):
				pass
			else:
				print "ERROR"
				count += 1
			#---------------------------
			# select board 1, port A (IN)
			selection.PA(1)
			check = read()
			if (check == dig):
				pass
			else:
				print "ERROR"
				count += 1
			#---------------------------
			# select board 2, port A (IN)
			selection.PA(2)
			check = read()
			if (check == dig):
				pass
			else:
				print "ERROR"
				count += 1
			#---------------------------
			# select board 3, port A (IN)
			selection.PA(3)
			check = read()
			if (check == dig):
				pass
			else:
				print "ERROR"
				count += 1

		print "Number of errors of it_" + str(it) + " = " + str(count)
		it += 1
