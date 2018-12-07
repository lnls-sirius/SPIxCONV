#!/usr/bin/python
# -*- coding: utf-8 -*-#

import serial
import time

conn = serial.Serial(
    # If the multimeter is connected via RS-232, use the next port:
    #port = "/dev/ttyS0",
    # If the multimeter is connected via USB, use the next port:
    port = "/dev/ttyUSB0",
    baudrate = 9600,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    timeout = None,
    xonxoff = False,
    rtscts = False,
    writeTimeout = None,
    dsrdtr = True,
    interCharTimeout = None)

conn.write("*RST\r\n")

conn.write("SYST:REM\r\n")
conn.write("*CLS\r\n")
conn.write("SYST:RWL\r\n")

conn.write("VOLT:DC:NPLC 200\r\n")
conn.write("INP:FILT:STAT OFF\r\n")

# choose either Channel 1 or Channel 2:
#conn.write("ROUT:TERM FRON1\r\n")
conn.write("ROUT:TERM FRON2\r\n")

def reset():
    conn.write("*RST\r\n")

    conn.write("SYST:LOC\r\n")
    #conn.write("SYST:REM\r\n")
    conn.write("*CLS\r\n")
    conn.write("SYST:RWL\r\n")

    conn.write("VOLT:DC:NPLC 200\r\n")
    conn.write("INP:FILT:STAT OFF\r\n")

    conn.write("ROUT:TERM FRON2\r\n")

def read():
    conn.write("READ?\r\n")
    #conn.timeout = 20.0
    answer = conn.read(17)
    '''
    answer = conn.read(1)
    conn.timeout = 0.1
    next_byte = conn.read(1)
    while (next_byte != ""):
        answer += next_byte
        next_byte = conn.read(1)
    '''
    # separate multimeter (floating point) in significand and exponent (with base 10)
    answer_int  = answer[0:answer.find("E")]
    answer_exp  = answer[answer.find("E")+1:]
    # change from str to float and int
    answer_int = float(answer_int)
    answer_exp = int(answer_exp)
    # calculate voltage measure read
    answer_int = answer_int*(10**answer_exp)
    return answer_int
'''
    #conn.timeout = None
#    answer = conn.read(17)
#    return answer[0:len(answer) - 2]
#    return answer
#conn.close()
'''
def read_lsb():
    conn.write("READ?\r\n")
    #conn.timeout = 20.0
    answer = conn.read(17)
    # separate multimeter (floating point) in significand and exponent (with base 10)
    answer_int  = answer[0:answer.find("E")]
    answer_exp  = answer[answer.find("E")+1:]
    # change from str to float and int
    answer_int = float(answer_int)
    answer_exp = int(answer_exp)
    # calculate voltage measure read
    answer_int = answer_int*(10**answer_exp)
    # convert to integer LSB
    answer_lsb = (answer_int+10)/20*262143
    answer_lsb = int(answer_lsb)
    return answer_lsb
