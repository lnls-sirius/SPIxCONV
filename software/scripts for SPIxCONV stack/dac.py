#!/usr/bin/python
from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO
import time
#-------------------------------------------------------
# DAC
# initialize the bus and device /dev/spidev2.0
spi1 = SPI(1,0)
#defining mode (CPOL = 0; CPHA = 1)
spi1.mode = 1
#defining speed (in bps)
spi1.msh = 10000000
#-------------------------------------------------------
# mnemonics for GPIO
RST = "P9_26"
CLR = "P9_25"
LDAC = "P9_24"
#-------------------------------------------------------
# defining outputs
GPIO.setup(RST, GPIO.OUT)
GPIO.setup(CLR, GPIO.OUT)
GPIO.setup(LDAC, GPIO.OUT)
#-------------------------------------------------------
# initialization of outputs
GPIO.output(RST, GPIO.HIGH)
GPIO.output(CLR, GPIO.HIGH)
GPIO.output(LDAC, GPIO.LOW)
#=======================================================
#    DAC calibration parameters
#=======================================================
# global variables
global GAIN
global OFFSET
# calibration realized on 27/oct/2017
#GAIN = 1
#OFFSET = 0
GAIN = 1.00006366999
OFFSET = -1.757554175
#=======================================================
#    config DAC
#=======================================================
def config():
    # send configuration byte
    # DAC control register: SDODIS = 0 (SDO enabled)
    spi1.writebytes([0x20,0x03,0x12])
    writeVolts(0)
    # DAC control register: SDODIS = 1 (SDO disabled)
    #spi1.writebytes([0x20, 0x03, 0x32])
#=======================================================
#    write a value in DAC (value in binary code)
#=======================================================
def write(value):
    # global variables
    global GAIN, OFFSET
    code = int(round((13107 + (value - 13107)*GAIN + OFFSET)))
    # prepare to send data to the Control Register
    bytes = ( (1 << 20) + (code << 2) )
    byte_1 = (bytes & 0xFF0000) >> 16
    byte_2 = (bytes & 0x00FF00) >> 8
    byte_3 = (bytes & 0x0000FF)
    spi1.writebytes([byte_1,byte_2,byte_3])
    # LDAC via hardwareLDAC
    #GPIO.output(LDAC, GPIO.LOW)
    #GPIO.output(LDAC, GPIO.HIGH)
    # pulse LDAC via software
    spi1.writebytes([0x40,0x00,0x01])
#=======================================================
#    write a value in DAC (value in Volts)
#=======================================================
def writeVolts(value):
    if( (value < -10) or (value > 10)):
        print "invalid argument"
    else:
        value = int(round((value + 10.0)/20 * 262143))
        write(value)
#=======================================================
#    read the value in DAC
#=======================================================
def read():
    spi1.xfer2([0x90,0x00,0x00])
    dac = spi1.readbytes(3)
    dac = 0x03ffff & (((dac[0] << 16) + (dac[1] << 8) + dac[2]) >> 2)
    return dac
#=======================================================
#    CLEAR the DAC of correspondent board
#=======================================================
def clear():
    GPIO.output(CLR, GPIO.HIGH)
    GPIO.output(CLR, GPIO.LOW)
#=======================================================
#    RESET the DAC of correspondent board
#=======================================================
def reset():
    GPIO.output(RST, GPIO.HIGH)
    GPIO.output(RST, GPIO.LOW)
#=======================================================
#                  DAC Calibration
#=======================================================
# this function runs a DAC calibration for the selected board
# it adjusts the DAC for two known voltages (-9V and +9V),
# waits 60s after each adjust and measure the voltage with the
# help of the DMM 34420A from Agilent. After that, calculates
# the angular and linear coefficient to fit the line as the
# theoretical model.
def calibration():
    import Agilent34420A
    # global variables
    global GAIN, OFFSET
    # set up DAC
    config()
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
        spi1.writebytes([byte_1,byte_2,byte_3])
        # LDAC via hardwareLDAC
        #GPIO.output(LDAC, GPIO.LOW)
        #GPIO.output(LDAC, GPIO.HIGH)
        # pulse LDAC via software
        spi1.writebytes([0x40,0x00,0x01])
        #---------------------------------------------------------
        time.sleep(30)
        measure.append(Agilent34420A.read())
    # calculating gain correction
    theoretical_step = 20.0/262143
    calibrated_step = (measure[1] - measure[0]) / (calibration_code[1] - calibration_code[0])
    GAIN = theoretical_step / calibrated_step
    # calculating offset correction (around code 131072, 0V)
    code_found = (-measure[0]/theoretical_step) + 13107
    OFFSET = code_found - 131072
    # return two parameters: gain and offset
    #output = [GAIN, OFFSET]
    print "\tgain = " + str(GAIN)
    print "\toffset = " + str(OFFSET)
    #return output
#---------------------------------------------------------------------
def read_calibration():
    # global variables
    global GAIN, OFFSET
    print "\tgain = " + str(GAIN)
    print "\toffset = " + str(OFFSET)

