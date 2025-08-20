#!/usr/bin/python3

from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO
import math
import time
import dac
#-------------------------------------------------------
# initialize the bus and device /dev/spidev1.0
spi0 = SPI(0,0)
#defining mode (CPOL = 0; CPHA = 1)
spi0.mode = 1
#defining speed (in bps)
spi0.msh = 10000000
#-------------------------------------------------------
# mnemonics for GPIO
BUSY = "P9_20"
CNV = "P9_23"
#-------------------------------------------------------
# defining outputs
GPIO.setup(CNV, GPIO.OUT)
#-------------------------------------------------------
# defining inputs
GPIO.setup(BUSY, GPIO.IN)
#-------------------------------------------------------
# initialization of outputs
GPIO.output(CNV, GPIO.LOW)
#=======================================================
#    ADC calibration parameters
#=======================================================
# global variables
global GAIN
global OFFSET
global REFERENCE
#REFERENCE = 13107
#GAIN = 1
#OFFSET = 0
REFERENCE = 13140.5627
GAIN = 1.00043749802
OFFSET = -32.9127
#=======================================================
#    read a value in DAC (value in binary code)
#=======================================================
def read():
    # global variables
    global REFERENCE, GAIN, OFFSET
    # CNVST = 0 --> start conversion
    GPIO.output(CNV, GPIO.LOW)
    #################################
    # wait for the rising of BUSY
    #################################
    #while(GPIO.input(BUSY) == 0):
    #    pass # does nothing
    # delay of 1us
    #time.sleep(0.1)
    #--------------------------------
    # bring CNVST back to "1" state
    GPIO.output(CNV, GPIO.HIGH)
    #################################
    # wait for the falling of BUSY (end of conversion)
    #################################
    #while(GPIO.input(BUSY) == 1):
    #    pass
    #--------------------------------

    # read data from ADC
    #data = spi0.readbytes(1)
    #adc = data[0]
    #adc = adc << 8

    #data = spi0.readbytes(1)
    #data = data[0]
    #adc += data
    #adc = adc << 8

    #data = spi0.readbytes(1)
    #data = data[0]
    #adc += data
    #adc = adc >> 6

    data = spi0.readbytes(3)
    adc = (data[0] << 10) + (data[1] << 2) + (data[2] >> 6)
    # applying GAIN and OFFSET corretion
    adc = int(round((adc - REFERENCE) * GAIN + OFFSET + REFERENCE))
    return adc
#=======================================================
#    read a value in DAC (value in Volts)
#=======================================================
def readVolts():
    adc = read()*1.0
    adc = (adc/262143)*20 - 10
    adc = round(adc, 6)
    return adc
#=======================================================
#    read ADC many times and calculate a mean
#=======================================================
def mean(value):
    # defining variables for MAX, MIN and MEAN (ADC measure)
    measure = []
    min_adc = 0
    max_adc = 0
    mean_adc = 0.0
    i = 0
    #-------------------------------------------------------
    while(i < value):
        adc = read()
#        adc_print(adc)
        measure.append(adc)
        # calculate ADC min, max and mean values
        # setting first values
        if(i == 0):
            min_adc = adc
            max_adc = adc
            mean_adc = float(adc)
        else:
            if(adc < min_adc):
                min_adc = adc
            if(adc > max_adc):
                max_adc = adc
            mean_adc = (mean_adc*i + adc)/(i + 1)
        i += 1
    #-------------------------------------------------------
    #calculate standard deviation
    diff = measure
    diff[:] = [x - mean_adc for x in measure]
    diff_square = [x**2 for x in diff]
    std_var = sum(diff_square)/(len(measure)*1.0)
    std_var = math.sqrt(std_var)
    std_var = "{0:.3f}".format(std_var)
    mean_adc = "{0:.2f}".format(mean_adc)
    #-------------------------------------------------------
    diff = max_adc - min_adc
    print "\nnumber of measures = " + str(value)
    print "standard variation = " + std_var
    print "width of histogram = " + str(diff)
    print "mean = " + mean_adc
    print "minimum = " + str(min_adc)
    print "maximum = " + str(max_adc) + "\n"
    return [std_var, diff, mean_adc, min_adc, max_adc]
#=======================================================
#                  ADC Calibration
#=======================================================
# this function runs an ADC calibration for the selected board
# DAC should be already calibrated for this calibration
# it runs a stability test for two different set points
# the mean of this two points are used as a reference
# for the calibration.
def calibration():
    # global variables
    global GAIN, OFFSET, REFERENCE
    # set up DAC
    dac.config()
    calibration = [-9, 9]
    total_measures = 10000
    # defining variables for MAX, MIN and MEAN (ADC measure)
    min_adc = [0] * 5
    max_adc = [0] * 5
    mean_adc = [0] * 5
    std_var = [0] * 5
    i = 0
    j = 0
    ############################################################
    interval = []
    for x in calibration:
        measure = []
        #print "  ============================================================================"
        #print "  |                           CALIBRATION:                                   |"
        #print "  ============================================================================"

        # select DAC and write correspondent value
        base = int(((x+10)/(20/float(262144))))
        interval.append(base)
        dac.write(base)
        time.sleep(30)
        measure = []
        for i in range (total_measures):
            #------------------------------------------------------
            # "adc_value = read()" without considering previous calibration
            # CNVST = 0 --> start conversion
            GPIO.output(CNV, GPIO.LOW)
            # bring CNVST back to "1" state
            GPIO.output(CNV, GPIO.HIGH)
            # read three bytes
            data = spi0.readbytes(3)
            adc_value = (data[0] << 10) + (data[1] << 2) + (data[2] >> 6)
            #------------------------------------------------------
            measure.append(adc_value)
            # check if it is the first measure
            if(i == 0):
                min_adc[j] = measure[0]
                max_adc[j] = measure[0]
                mean_adc[j] = measure[0]*1.0
            # if not, calculate max, min and mean
            else:
                if(measure[i] < min_adc[j]):
                    min_adc[j] = measure[i]
                if(measure[i] > max_adc[j]):
                    max_adc[j] = measure[i]
                mean_adc[j] = (mean_adc[j]*i + measure[i])/(i + 1)
            i += 1
            adc_volt = float(adc_value)/262143*20-10
            adc_volt_str = str(adc_volt)
            adc_volt_str = adc_volt_str[0:adc_volt_str.find(".")+8]
            #sys.stdout.write("  | " + str(adc_value) + "\t" + str(adc_value) + "\t\t\t\t\t\t\t" + "|" + "\n")
        j += 1
    REFERENCE = mean_adc[0]
    # calculating gain correction
    theoretical_step = 20.0 / 262143
    calibrated_step = 18.0 / (mean_adc[1] - mean_adc[0])
    GAIN = calibrated_step / theoretical_step
    # calculating offset correction (around code 131072, 0V)
    interval = 9.0 / theoretical_step
    OFFSET = 131072 - interval - mean_adc[0]
    # return two parameters: gain and offset
    #output = [REFERENCE, GAIN, OFFSET]
    print "\treference = " + str(REFERENCE)
    print "\tgain = " + str(GAIN)
    print "\toffset = " + str(OFFSET)
    #return output
#---------------------------------------------------------------------
def read_calibration(board):
    # global variables
    global GAIN, OFFSET, REFERENCE
    print "\treference = " + str(REFERENCE)
    print "\tgain = " + str(GAIN)
    print "\toffset = " + str(OFFSET)

