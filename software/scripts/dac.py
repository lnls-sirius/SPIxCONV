#!/usr/bin/python
from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO
#-------------------------------------------------------
import selection
import time
import flash
# initialize the bus and device /dev/spidev1.0
spi = SPI(0,0)
# mnemonics for GPIO
LDAC = "P9_24"    #DIO3
# defining outputs
GPIO.setup(LDAC, GPIO.OUT)
# initialization of outputs
GPIO.output(LDAC, GPIO.HIGH)
#-------------------------------------------------------
# initialization of variables
DELAY = 0    # used in ramp
# global variables
global GAIN
global OFFSET
GAIN = 1
OFFSET = 0
#=======================================================
#    Power on DAC circuit
#=======================================================
def on(board):
    global GAIN, OFFSET
    selection.decoder(board)
    # put PWR_GOOD_DAC to "1"
    spi.writebytes([0x00])
    selection.clk_ff(board)
    #------------------------
    # read calibration parameters
    selection.flash(board)
    GAIN = flash.dac_gain_read(board)
    if (GAIN == 0):
        GAIN = 1
    OFFSET = flash.dac_offset_read(board)
#=======================================================
#    Power off DAC circuit
#=======================================================
def off(board):
    selection.decoder(board)
    # put PWR_GOOD_DAC to "1"
    spi.writebytes([0x01])
    selection.clk_ff(board)
#=======================================================
#    Power off all DAC circuits (from board 0 to 7)
#=======================================================
def off_all():
    for board in range(8):
        selection.decoder(board)
        # put PWR_GOOD_DAC to "1"
        spi.writebytes([0x01])
        selection.clk_ff(board)
#=======================================================
#                  DAC Calibration
#=======================================================
# this function runs a DAC calibration for the selected board
# it adjusts the DAC for two known voltages (-9V and +9V),
# waits 60s after each adjust and measure the voltage with the
# help of the DMM 34420A from Agilent. After that, calculates
# the angular and linear coefficient to fit the line as the
# theoretical model.
def calibration(board):
    import Agilent34420A
    # turns on DAC circuit
    on(board)
    # global variables
    global GAIN, OFFSET
    GAIN = 1
    OFFSET = 0
    # set up DAC
    selection.dac(board)
    config(board)
    calibration = [-9, 9]
    calibration_code = []
    measure = []
    for x in calibration:
        base = int(round((x + 10.0)/20 * 262143))
        calibration_code.append(base)
        #---------------------------------------------------------
        # "write(base)" without considering previous calibration
        # prepare to send data to the Control Register
        bytes = ( (1 << 20) + (base << 2) )
        byte_1 = (bytes & 0xFF0000) >> 16
        byte_2 = (bytes & 0x00FF00) >> 8
        byte_3 = (bytes & 0x0000FF)
        spi.writebytes([byte_1,byte_2,byte_3])
        # LDAC via hardwareLDAC
        #GPIO.output(LDAC, GPIO.LOW)
        #GPIO.output(LDAC, GPIO.HIGH)
        # pulse LDAC via software
        spi.writebytes([0x40,0x00,0x01])
        #---------------------------------------------------------
        time.sleep(60)
        measure.append(Agilent34420A.read())
    # calculating gain correction
    theoretical_step = 20.0/262143
    calibrated_step = (measure[1] - measure[0]) / (calibration_code[1] - calibration_code[0])
    GAIN = theoretical_step / calibrated_step
    # calculating offset correction (around code 131072, 0V)
    code_found = (-measure[0]/theoretical_step) + 13107
    OFFSET = code_found - 131072
    # store both parameters (GAIN and OFFSET) in flash memory
    flash.dac_gain_write(board, GAIN)
    flash.dac_offset_write(board, OFFSET)
    # return two parameters: gain and offset
    #output = [GAIN, OFFSET]
    print "\tgain = " + str(GAIN)
    print "\toffset = " + str(OFFSET)
    #return output
#---------------------------------------------------------------------
def read_calibration(board):
    global GAIN, OFFSET
    # global variables
    GAIN = flash.dac_gain_read(3)
    OFFSET = flash.dac_offset_read(3)
    print "\tgain = " + str(GAIN)
    print "\toffset = " + str(OFFSET)
#=======================================================
#    config DAC
#=======================================================
def config(board):
    selection.dac(board)
    # send configuration byte
    # DAC control register: SDODIS = 0 (SDO enabled)
    spi.writebytes([0x20,0x03,0x12])
    # DAC control register: SDODIS = 1 (SDO disabled)
    #spi.writebytes([0x20, 0x03, 0x32])
    # write 0V on DAC exit
    writeVolts(0)
#=======================================================
#    write a value in DAC (value in binary code)
#=======================================================
def write(value):
    # global variables
    global GAIN, OFFSET
    code = int(round((13107 + (value - 13107)*GAIN + OFFSET)))
    if (code < 0):
        code = 0
    elif (code > 262143):
        code = 262143
    # prepare to send data to the Control Register
    bytes = ((1 << 20) + (code << 2))
    byte_1 = (bytes & 0xFF0000) >> 16
    byte_2 = (bytes & 0x00FF00) >> 8
    byte_3 = (bytes & 0x0000FF)
    spi.writebytes([byte_1,byte_2,byte_3])
    # LDAC via hardware (INTMOSI)
    #GPIO.output(LDAC, GPIO.LOW)
    #GPIO.output(LDAC, GPIO.HIGH)
    # pulse LDAC via software
    spi.writebytes([0x40,0x00,0x01])
#=======================================================
#    write a value in DAC (value in Volts)
#=======================================================
def writeVolts(value):
    # global variables
    global GAIN, OFFSET
    if( (value < -10) or (value > 10)):
        print "invalid argument"
    else:
        value = int(round((value + 10.0)/20 * 262143))
        code = int(round((13107 + (value - 13107)*GAIN + OFFSET)))
        # prepare to send data to the Control Register
        bytes = ( (1 << 20) + (code << 2) )
        byte_1 = (bytes & 0xFF0000) >> 16
        byte_2 = (bytes & 0x00FF00) >> 8
        byte_3 = (bytes & 0x0000FF)
        spi.writebytes([byte_1,byte_2,byte_3])
        # LDAC via hardwareLDAC
        #GPIO.output(LDAC, GPIO.LOW)
        #GPIO.output(LDAC, GPIO.HIGH)
        # pulse LDAC via software
        spi.writebytes([0x40,0x00,0x01])
#=======================================================
#    read the value in DAC
#=======================================================
def read():
    global GAIN, OFFSET
    spi.xfer2([0x90,0x00,0x00])
    dac = spi.readbytes(3)
    dac = 0x03ffff & (((dac[0] << 16) + (dac[1] << 8) + dac[2]) >> 2)
    # adjusting to calibration parameters
    code = (dac - 13107.0 - OFFSET)/GAIN + 13107
    return int(round(code))
#=======================================================
#    CLEAR the DAC of correspondent board
#=======================================================
def clear(board):
    # put CLR pin to "0"
    selection.decoder(board)
    spi.writebytes([0x05])
    selection.clk_ff(board)
    # put CLR and RESET pin back to "1"
    selection.decoder(board)
    spi.writebytes([0x04])
    selection.clk_ff(board)
#=======================================================
#    RESET the DAC of correspondent board
#=======================================================
def reset(board):
    # put RESET pin to "0"
    selection.decoder(board)
    spi.writebytes([0x06])
    selection.clk_ff(board)
    # put RESET and CLR pin back to "1"
    selection.decoder(board)
    spi.writebytes([0x04])
    selection.clk_ff(board)
#=======================================================
