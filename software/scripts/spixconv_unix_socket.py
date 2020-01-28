#!/usr/bin/python
# -*- coding: utf-8 -*-

#import spixconv_unix_socket as a

import socket
import sys
import os
import time
import logging
import argparse

#from epics import caput, caget
'''
===============================================================================
    Unix socket "protocol"
===============================================================================
code    correspondent function
-----   ------------------------------------------
0x00:   --reserved--
0x01:   config(board)
0x02:   set_digital_output_byte(board, value)
0x03:   set_digital_output_bit(board, bit, value)
0x04:   read_digital_input_byte(board)
0x05:   read_digital_input_bit(board, bit_pos)
0x06:   set_analog_output(board, voltage)
0x07:   read_analog_input(board)
0x08:   reset(board)
0x09:   --available--
...          ...
0xFE    --available--
0xFF:   --reserved--
===============================================================================
código  função correspondente
-----   ------------------------------------------
0x00:   --reservado--
0x01:   config(board)
0x02:   setar_saida_digital_byte(board, value)
0x03:   setar_saida_digital_bit(board, bit, value)
0x04:   ler_entrada_digital_byte(board)
0x05:   ler_entrada_digital_bit(board, bit)
0x06:   setar_saida_analogica(board, voltage)
0x07:   ler_entrada_analogica(board)
0x08:   resetar(board)
0x09:   --disponível--
...          ...
0xFE    --disponível--
0xFF:   --reservado--
'''
#==============================================================================
import init
import selection
import dac
import adc
import flash
import gpio

global digital_output
digital_output = 0x00
#==============================================================================
#global MIN_SCALE, MAX_SCALE, FULL_SCALE
#MIN_SCALE = 0
#--------------------
# Glassman: PS/EQ001R1.2GT2
#MAX_SCALE = 1000.0
#--------------------
# Glassman: ET1.5R1300
#MAX_SCALE = 1500.0
#--------------------
# Glassman: FR10P30
#MAX_SCALE = 10000.0
#--------------------
# Glassman: PS/WX15P70.0-22
#MAX_SCALE = 15000.0
#--------------------
# Glassman: PS/WX30P35.0-22
#MAX_SCALE = 10000.0
#--------------------
#FULL_SCALE = MAX_SCALE - MIN_SCALE
#==============================================================================
#   Turn on DAC and ADC, and configure DAC
#==============================================================================
def config(board):
    '''
    input parameters:
        - board: board address
    output parameters:
        - none
    ----------------------------
    description:
        this function turns on DAC and ADC circuit and configure DAC.
    '''
    # ADC_array is used to store the last 10 ADC measures
    # when an ADC measure is requested, intead the raw measure,
    # it returns the maximum value of the array (the last 10 measures)
    # this is to avoid change in ADC measure due to capacitor discharges
    #
    #            R           SW
    #     _____/\/\/\________/ ____
    #    |              |          |
    # PS |            C |          |
    #  -----          -----      MAGNET
    #   ---           -----        |
    #    |              |          |
    #   GND            GND        GND

    global ADC_array
    ADC_array = 10 * [0]
    dac.on(board)
    adc.on(board)
    time.sleep(1)
    dac.config(board)
    gpio.config(board)
#==============================================================================
#    Write a value in analog output
#==============================================================================
def set_analog_output(board, code):
    '''
    input parameters:
        - board:    board address
        - voltage:  value in Volts (from MIN_SCALE to FULL_SCALE)
    output parameters:
        - none
    ----------------------------
    description:
        this function writes an analog output (from -10V to 10V, but only used
        monopolar range, i.e., 0 to +10V, mapped in 0 to FULL_SCALE voltage).
    '''
    #global MIN_SCALE, MAX_SCALE, FULL_SCALE
    #value = int(round(((voltage - MIN_SCALE)/FULL_SCALE)*131071 + 131072))
    code = int(code)
    selection.dac(board)
    dac.write(code)
    #print code
#==============================================================================
#    Read the value set in analog output
#==============================================================================
def read_analog_output(board):
    '''
    input parameters:
        - board:    board address
    output parameters:
        - code set in DAC (from 0 to 262143, correspondent to -10V to 10V)
    ----------------------------
    description:
        this function reads the code set in the analog output (from 0 to 262143)
    '''
    selection.dac(board)
    return dac.read(board)
#==============================================================================
#    Read maximum of 10 last analog measures
#==============================================================================
def read_analog_input(board):
    '''
    input parameters:
        - board: board address
    output parameters:
        - code:  maximum value of last 10 measures (in Volts, from MIN_SCALE to FULL_SCALE)
    ----------------------------
    description:
        this function reads an analog input (from -10V to 10V, but only used
        monopolar range, i.e., 0 to +10V, mapped in 0 to FULL_SCALE voltage).
    '''
    selection.adc(board)
    code = adc.read()
    # remove the oldest measure of the array
    ADC_array.pop(0)
    # append new value to the array
    ADC_array.append(code)
    # complete array size to be 10 (in case of error)
    while (len(ADC_array) != 10):
        ADC_array.append(0)
    #print(ADC_array)
    #print(max(ADC_array))
    return max(ADC_array)
#==============================================================================
#    Read raw value in analog input
#==============================================================================
def read_analog_input_raw(board):
    '''
    input parameters:
        - board: board address
    output parameters:
        - code:  raw value of ADC measures (in Volts, from MIN_SCALE to FULL_SCALE)
    ----------------------------
    description:
        this function reads an analog input (from -10V to 10V, but only used
        monopolar range, i.e., 0 to +10V, mapped in 0 to FULL_SCALE voltage).
    '''
    #global MIN_SCALE, MAX_SCALE, FULL_SCALE
    selection.adc(board)
    #volts = adc.meanVolts(1000)
    #volts = adc.readVolts()
    code = adc.read()
    #volts = (volts / 10) * (FULL_SCALE - MIN_SCALE)
    #return round(volts,6)
    return code
#==============================================================================
#    Configure digital pins as input or output
#==============================================================================
    '''
    input parameters:
        - board: board address
        - port:  pin port that will be configured (A, B, C or D)
        - bit:   bit position (MSB = 7, LSB = 0)
        - value: "0" for OUTPUT
                 "1" for INPUT
    output parameters:
        - none
    ----------------------------
    description:
        this function defines the direction of a bit.
    '''
def set_direction_bit(board, port, bit, value):
    # select the correspondent device
    if((port == "A") or (port == "B")):
        selection.gpioAB(board)
    else:
        selection.gpioCD(board)
    #-----------------------------------
    # read current configuration
    if((port == "A") or (port == "C")):
        direction = int(gpio.OCR1_read())
    else:
        direction = int(gpio.OCR2_read())
    print "direction BEFORE = " + str(direction)
    #-----------------------------------
    # if bit will be set as INPUT ("1" state), performs an "or" with previous byte
    if (value):
        direction = (direction | (1 << bit))
    # if bit will be set as OUTPUT ("0" state), performs an "and" with previous byte
    else:
        # mask is an XOR of 0xFF and bit position
        mask = 0xFF ^ (1 << bit)
        direction = (direction & mask)
    #-----------------------------------
    # rewrite previous byte with bit updated
    if((port == "A") or (port == "C")):
        gpio.OCR1_write(direction)
    else:
        gpio.OCR2_write(direction)
    print "direction AFTER = " + str(direction) + "\n=========================="

#==============================================================================
#    Write a value in digital output port (Port B)
#==============================================================================
# write a full byte
def set_digital_output_byte(board, value):
    '''
    input parameters:
        - board: board address
        - value: byte that will be written
    output parameters:
        - none
    ----------------------------
    description:
        this function writes a full byte in digital port B.
    '''
    #-----------------------------------
    # update digital output stored value
    global digital_output
    digital_output = value
    flash.sector_write(board, 0x68, [value])
    #-----------------------------------
    selection.gpioAB(board)
    gpio.OCR2_write(value)
#-------------------------------------------------------
# change just one bit at time
def set_portB_digital_output_bit(board, bit, value):
    '''
    input parameters:
        - board: board address
        - bit:   bit position (MSB = 7, LSB = 0)
        - value: "0" or "1"
    output parameters:
        - none
    ----------------------------
    description:
        this function modifies a single bit in digital port B.
    '''
    #-----------------------------------
    # previous state stored in lower part of block 5 (0x050000)
    #  current state stored in upper part of block 5 (0x058000)

    # restore digital output stored value
    global digital_output
    # read previous state
    #digital_output = flash.read(board, 0x050000, 1)
    #digital_output = digital_output[0]
    #-----------------------------------
    # if bit to be written is "1", performs an "or" with previous byte
    if (value):
        digital_output = (digital_output | (1 << bit))
    # if bit to be written is "0", performs an "and" with previous byte
    else:
        # mask is an XOR of 0xFF and bit position
        mask = 0xFF ^ (1 << bit)
        digital_output = (digital_output & mask)
    # rewrite previous byte with bit updated
    #-----------------------------------
    # write new digital output in current state address (0x058000)
    #flash.sector_write(board, 0x058000, [digital_output, 0xFF])
    # update digital output stored value in previous state (0x050000)
    #flash.sector_write(board, 0x050000, [digital_output, 0xFF])
    #-----------------------------------
    selection.gpioAB(board)
    gpio.OCR2_write(digital_output)
#==============================================================================
#    Read a value in digital input port (Port A)
#==============================================================================
# read a full byte
def read_digital_input_byte(board):
    '''
    input parameters:
        - board: board address
        - bit:   bit position (MSB = 7, LSB = 0)
    output parameters:
        - byte read in digital Port A
    ----------------------------
    description:
        this function reads a full byte in digital port A.
    '''
    selection.gpioAB(board)
    return gpio.GSR1()
#-------------------------------------------------------
# read just one bit at time
def read_portA_digital_input_bit(board, bit_pos):
    '''
    input parameters:
        - board:    board address
        - bit_pos:  bit position (MSB = 7, LSB = 0)
    output parameters:
        - bit_val:  value of the bit in position "pos"
    ----------------------------
    description:
        this function reads a single bit in digital port A.
    '''
    selection.gpioAB(board)
    # digital.read() returns a string represented in hexadecimal (e.g.: '0x54')
    byte = int(gpio.GSR1())
    # performs an "and" between byte and mask
    mask = (1 << bit_pos)
    bit = (byte & mask) >> bit_pos
    return bit
#-------------------------------------------------------
# read just one bit at time
def read_portB_digital_input_bit(board, bit_pos):
    '''
    input parameters:
        - board:    board address
        - bit_pos:  bit position (MSB = 7, LSB = 0)
    output parameters:
        - bit_val:  value of the bit in position "pos"
    ----------------------------
    description:
        this function reads a single bit in digital port A.
    '''
    selection.gpioAB(board)
    # digital.read() returns a string represented in hexadecimal (e.g.: '0x54')
    byte = int(gpio.GSR2())
    # performs an "and" between byte and mask
    mask = (1 << bit_pos)
    bit = (byte & mask) >> bit_pos
    return bit
#==============================================================================
#    Read Port B output bit setpoint
#==============================================================================
def read_portB_digital_output_bit(board, bit_pos):
    '''
    input parameters:
        - board:    board address
        - bit_pos:  bit position (MSB = 7, LSB = 0)
    output parameters:
        - bit:      value of the bit in position "pos"
    ----------------------------
    description:
        this function reads the setpoint of a single bit in digital port B.
    '''
    selection.gpioAB(board)
    byte = int(gpio.OCR2_read())
    # performs an "and" between byte and mask
    mask = (1 << bit_pos)
    bit = (byte & mask) >> bit_pos
    return bit
#==============================================================================
#    Send a pulse to be used as a reset
#==============================================================================
def reset(board, polatization):
    '''
    input parameters:
        - board:    board address
    output parameters:
        - none
    ----------------------------
    description:
        this function generates a pulse in bit 3 of digital output (port B).
        this pulse is used as a reset and should last from 200ms to 500ms.
    '''
    # generate pulse in RESET bit:
    #set_digital_output_bit(board, bit, value)
    if (polatization == 1):
        set_portB_digital_output_bit(board, 3, 1)
    elif (polatization == 0):
        set_portB_digital_output_bit(board, 3, 0)
    #caput("TB-04:PM-InjS:Reset-Cmd", 0)
#==============================================================================

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)-15s [%(levelname)s] %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S')
    logger = logging.getLogger()

    parser = argparse.ArgumentParser(description='SPIxCONV Socket Binding', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    #parser.add_argument('board_address', type=int, help='Board address.')
    parser.add_argument('--tcp', help='Use a TCP socket instead of an UNIX.', action='store_true')
    parser.add_argument('--port', '-p', dest='port', type=int, help='TCP server port.', default=5005)
    parser.add_argument('--unix-address', dest='unix_socket_address', help='UNIX socket address.', default='/tmp/socket_spixconv')
    args = parser.parse_args()

    server_address = ('0.0.0.0', args.port) if args.tcp else args.unix_socket_address

    if not args.tcp:
        try:
            # delete the file path
            os.unlink(server_address)
        except OSError:
            if os.path.exists(server_address):
                raise
    #----------------------------
    # identify board address:
    for addr in range(255):
        flash.ID_read(addr) == 4:
            board_address = addr
            break
    #----------------------------
    try:
        config(args.board_address)

        sock = socket.socket(socket.AF_INET if args.tcp else socket.AF_UNIX, socket.SOCK_STREAM)
        if args.tcp:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind(server_address)
        logger.info('Created socket at {} '.format(server_address))
        sock.listen(1)

        #interlocks = "External,High voltage power supply overvoltage,High voltage power supply overcurrent,Personnel protection,Temperature,AC power,Switch"
        logger.info("unix socket running!")

        while True:
            connection, client_address = sock.accept()
            try:
                logger.info('Client connected {} '.format(client_address))
                while True:
                    data = connection.recv(512)
                    if data:
                        #==============================================================
                        # set GPIO pin direction
                        if (data[0] == "\x01"):
                            set_direction_bit(int(ord(data[1])), data[2], int(ord(data[3])), int(data[4]))
                        #==============================================================
                        # adjust DAC output value
                        elif (data[0] == "\x02"):
                            # convert voltage parameter from string to float
                            value = float(data[2:len(data)])
                            set_analog_output(int(ord(data[1])), value)
                        #==============================================================
                        # read DAC setpoint value
                        elif (data[0] == "\x03"):
                            selection.dac(ord(data[1]))
                            dac_setpoint = dac.read()
                            connection.sendall(str(dac_setpoint) + "\r\n")
                        #==============================================================
                        # read maximum of 10 last ADC input value
                        elif (data[0] == "\x04"):
                            voltage = read_analog_input(ord(data[1]))
                            connection.sendall(str(voltage) + "\r\n")
                            #print str(voltage)
                        #==============================================================
                        # write a whole byte in digital Port B
                        elif (data[0] == "\x05"):
                            set_digital_output_byte(ord(data[1]), ord(data[2]))
                        #==============================================================
                        # write a bit in Port B GPIO
                        elif (data[0] == "\x06"):
                            set_digital_output_bit(int(ord(data[1])), int(ord(data[2])), int(data[3]))
                        #==============================================================
                        # read the whole byte in digital Port A
                        elif (data[0] == "\x07"):
                            byte = read_digital_input_byte(ord(data[1]))
                            connection.sendall(str(byte))
                            print byte
                        #==============================================================
                        # read a bit in Port B GPIO
                        elif (data[0] == "\x08"):
                            bit = read_digital_input_bit(ord(data[1]), ord(data[2]))
                            connection.sendall(str(bit))
                            #print bit
                        #==============================================================
                        # generate a pulse in RESET bit (Port B, bit 3)
                        elif (data[0] == "\x09"):
                            reset(ord(data[1]), int(data[2]))
                        #==============================================================
                        # read interlock labels
                        elif (data[0] == "\x0A"):
                            #connection.sendall(interlocks)
                            pass
                        #==============================================================
                        # read a Port B bit setpoint
                        elif (data[0] == "\x0B"):
                            bit = read_portB_digital_output_bit(ord(data[1]), ord(data[2]))
                            connection.sendall(str(bit))
                        #==============================================================
                        #
                        elif (data[0] == "\x0C"):
                            set_portB_digital_output_bit(int(ord(data[1])), int(ord(data[2])), int(data[3]))
                        #==============================================================
                        #
                        elif (data[0] == "\x0D"):
                            bit = read_portA_digital_input_bit(ord(data[1]), ord(data[2]))
                            connection.sendall(str(bit))
                        #==============================================================
                        #
                        elif (data[0] == "\x0E"):
                            bit = read_portB_digital_input_bit(ord(data[1]), ord(data[2]))
                            connection.sendall(str(bit))
                        #==============================================================
                        # read raw ADC input value
                        elif (data[0] == "\x0F"):
                            voltage = read_analog_input_raw(ord(data[1]))
                            connection.sendall(str(voltage) + "\r\n")
                            #print str(voltage)
                        #==============================================================
                        # available command
                        elif (data[0] == "\x10"):
                            pass

                    else:
                        break
            except:
                logger.exception('Connection Error !')
            finally:
                logger.info('Closing connection {}'.format(client_address))
                connection.close()
    finally:
        sock.close()

