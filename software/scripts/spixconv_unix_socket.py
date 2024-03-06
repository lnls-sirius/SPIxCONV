#!/usr/bin/python
# -*- coding: utf-8 -*-

#import spixconv_unix_socket as a

import socket
import sys
import os
import time
import logging
import argparse
import time
from threading import Thread, Lock
from Queue import Queue

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
global ADC_array


digital_output = 0x00
ADC_array = {}
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
    global lock
    with lock:
        ADC_array[board] = 10 * [0]
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
    global lock
    global board_calibration
    #global MIN_SCALE, MAX_SCALE, FULL_SCALE
    #value = int(round(((voltage - MIN_SCALE)/FULL_SCALE)*131071 + 131072))
    code = int(code)
    with lock:
        selection.dac(board)
        dac.write(code, board_calibration[board]["DAC gain"], board_calibration[board]["DAC offset"])
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
    global lock
    global board_calibration
    with lock:
        selection.dac(board)
        code = dac.read(board_calibration[board]["DAC gain"], board_calibration[board]["DAC offset"])
    return code
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
    global lock
    global board_calibration
    with lock:
        selection.adc(board)
        code = adc.read(board_calibration[board]["ADC gain"], board_calibration[board]["ADC offset"])
    # remove the oldest measure of the array
    #ADC_array[board].pop(0)
    ADC_array[board] = []
    # append new value to the array
    ADC_array[board].append(code)
    # complete array size to be 10 (in case of error)
    while (len(ADC_array[board]) != 10):
        ADC_array[board].append(code)
    #print(ADC_array)
    #print(max(ADC_array))
    return max(ADC_array[board])
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
    global lock
    global board_calibration
    #global MIN_SCALE, MAX_SCALE, FULL_SCALE
    with lock:
        selection.adc(board)
        code = adc.read(board_calibration[board]["ADC gain"], board_calibration[board]["ADC offset"])
    #volts = adc.meanVolts(1000)
    #volts = adc.readVolts()
    #volts = (volts / 10) * (FULL_SCALE - MIN_SCALE)
    #return round(volts,6)
    return code
#==============================================================================
#    Configure digital pins as input or output
#==============================================================================
def set_direction_bit(board, port, bit, value):
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
    global lock
    with lock:
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
        #print "direction BEFORE = " + str(direction)
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
        #print "direction AFTER = " + str(direction) + "\n=========================="

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
    global lock
    #-----------------------------------
    # update digital output stored value
    global digital_output
    digital_output = value
    with lock:
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
    global lock
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
    with lock:
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
    global lock
    with lock:
        selection.gpioAB(board)
        config_byte = gpio.GSR1()
    return config_byte
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
    global lock
    with lock:
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
    global lock
    with lock:
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
    global lock
    with lock:
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
#    Get steps config with hostname
#==============================================================================
def get_ip_hostname():
    # get hostname
    hostname = socket.gethostname()
    #----------------------------
    # get IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return hostname, ip
#==============================================================================
#    Get steps config with hostname
#==============================================================================
def get_steps_var(ip, hostname):
    #return voltage_factor, step_trigger, step_delay, nb_steps
    '''
    return:
      - voltage_factor
      - step_trigger
      - step_delay
    '''
    global logger

    # CHECK HOSTNAME FOR CONFIGURING
    #First, check if hostname must be changed - USB STICK
    if not os.path.exists("/media/usb"):
        os.system("mkdir /media/usb")
        
    if os.path.exists("/dev/sda1"):
        os.system("mount /dev/sda1 /media/usb")

        if os.path.isfile("/media/usb/ConfigByHostname.txt"):
            with open("/media/usb/ConfigByHostname.txt") as name:
                hostname = name.readline().split("\n")[0]
                name.close()

            with open("/etc/hostname", "w") as hostnameFile:
                hostnameFile.write(hostname)
                hostnameFile.close()
            logger.info('New Hostname: {}'.format(hostname))
    
        os.system("umount /dev/sda1")

        
    if((hostname == 'TB-InjSept') or (hostname == 'TS-InjSeptG-1') or (hostname == 'TS-InjSeptG-2') or (hostname == 'TS-InjSeptF') or (hostname == 'TS-EjeSeptF') or (hostname == 'TS-EjeSeptG')):
        logger.info('Hostname identified: {}'.format(hostname))
        return 100, 200, 2, 4
        
    if(hostname == 'BO-InjKckr'):
        logger.info('Hostname identified: {}'.format(hostname))
        return 1000, 500, 2, 4

    if(hostname == 'BO-EjeKckr'):
        logger.info('Hostname identified: {}'.format(hostname))
        return 1000, 1000, 2, 4

    if((hostname == 'SI-InjDpKckr') or (hostname == 'SI-InjNLKckr')):
        logger.info('Hostname identified: {}'.format(hostname))
        return 1500, 2000, 2, 4

    if(hostname == 'SI-PingH'):
        logger.info('Hostname identified: {}'.format(hostname))
        return 3000, 2000, 2, 4
       
    if(hostname == 'SI-PingV'):
        logger.info('Hostname identified: {}'.format(hostname))
        return 1000, 2000, 2, 4

    # ELSE: RETURN A DEFAULT VALUE
    else:
        logger.info('Hostname identified ({}) IS UNKNOWN! WORST CASE SELECTED.'.format(hostname))
        return 3000, 2000, 2, 4

    #raise ValueError(f'hostname {hostname} not supported')
#==============================================================================

if __name__ == '__main__':
    global board_address
    global board_address_2
    global board_address_3
    global board_calibration
    global connection
    global logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)-15s [%(levelname)s] %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S')
    logger = logging.getLogger()

    parser = argparse.ArgumentParser(description='SPIxCONV Socket Binding', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('board_address', type=int, help='Board address.')
    parser.add_argument('--tcp', help='Use a TCP socket instead of an UNIX.', action='store_true')
    parser.add_argument('--port', '-p', dest='port', type=int, help='TCP server port.', default=5005)
    parser.add_argument('--unix-address', dest='unix_socket_address', help='UNIX socket address.', default='/tmp/socket_spixconv')
    parser.add_argument('--nlk', '-nlk', dest='nlk', type=bool, help='NLK magnet', default=False)
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
        if(flash.ID_read(addr) == 4):
            board_address = addr
            break

    if "NLK" in socket.gethostname():
        board_address = 7
        board_address_2 = 6
        board_address_3 = 5

    #print(board_address, board_address_2, board_address_3)


    board_calibration = {}
    #----------------------------
    # create general queue
    queue_general = Queue()
    # create voltage adjustment queue
    queue_voltage = Queue()
    #----------------------------
    def write_to_list():
        global board_address
        global board_address_2
        global board_address_3
        global connection
        global voltage_factor
        global step_trigger
        global step_delay
        global trigger
        global steps
        global last_setpoint
        global board_calibration
        global logger

        try:
            
            sock = socket.socket(socket.AF_INET if args.tcp else socket.AF_UNIX, socket.SOCK_STREAM)
            if args.tcp:
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            #config(args.board_address)
            config(board_address)
            time.sleep(1)
            board_calibration[board_address] = {"DAC gain":dac.GAIN,
                                                "DAC offset":dac.OFFSET,
                                                "ADC gain":adc.GAIN,
                                                "ADC offset":adc.OFFSET}
            if "NLK" in socket.gethostname():
                config(board_address_2)
                time.sleep(1)
                board_calibration[board_address_2] = {"DAC gain":dac.GAIN,
                                                    "DAC offset":dac.OFFSET,
                                                    "ADC gain":adc.GAIN,
                                                    "ADC offset":adc.OFFSET}
                config(board_address_3)
                time.sleep(1)
                board_calibration[board_address_3] = {"DAC gain":dac.GAIN,
                                                    "DAC offset":dac.OFFSET,
                                                    "ADC gain":adc.GAIN,
                                                    "ADC offset":adc.OFFSET}
    
            logger.info(board_calibration)
            sock.bind(server_address)
            logger.info('Created socket at {} '.format(server_address))
            sock.listen(1)
    
            #interlocks = "External,High voltage power supply overvoltage,High voltage power supply overcurrent,Personnel protection,Temperature,AC power,Switch"
            logger.info("unix socket running!")
            #----------------------------
            # read Voltage-RB at initialization             
            last_setpoint = read_analog_output(board_address)
            #----------------------------
            # get hostname and IP
            hostname, ip = get_ip_hostname()
            #----------------------------
            # initialize steps variable
            voltage_factor, step_trigger, step_delay, steps = get_steps_var(ip, hostname)
            trigger = step_trigger/(10.0*voltage_factor) * 131072
            #----------------------------
            # LF (line feed) = 0x0A
            LF = 0x0A
            # CR (carriage return) = 0x0D
            CR = 0x0D
            #----------------------------
            while True:
                connection, client_address = sock.accept()
                connection.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) # Enable KeepAlive functionality
                connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 1) # Wait 1 sec before testing keepalive
                connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 3) # Retry keepalive after 3 secs
                connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 3) # Retry keepalive 3 times
                try:
                    logger.info('Client connected {} '.format(client_address))
                    while True:
                        msg = connection.recv(512)
                        if msg:
                            commands = msg.split('\r\n')
                            for data in commands:
                                if data:
#                                    logger.info("Comando recebido: {}".format(ord(data[0])))
                                    #==============================================================
                                    # set GPIO pin direction
                                    if (data[0] == "\x01"):
                                        logger.info('Command received: set GPIO direction')
                                        queue_general.put([data[0], "dummy_address", data[2], data[3], data[4]])
                                    #==============================================================
                                    # adjust DAC output value
                                    elif (data[0] == "\x02"):
                                        # update last setpoint
                                        logger.info('Command received: voltage setpoint')
                                        last_setpoint = int(data[2:])
                                        #-----------------------------------------
                                        queue_voltage.put([board_address, data[2:]])
                                    #==============================================================
                                    # read DAC setpoint value
                                    elif (data[0] == "\x03"):
                                        connection.sendall(str(read_analog_output(board_address)) + "\r\n")
                                    #==============================================================
                                    # read maximum of 10 last ADC input value
                                    elif (data[0] == "\x04"):
                                        #voltage = read_analog_input(ord(command[1]))
                                        voltage = read_analog_input(board_address)
                                        connection.sendall(str(voltage) + "\r\n")
                                        #print str(voltage)
                                    #==============================================================
                                    # write a whole byte in digital Port B
                                    elif (data[0] == "\x05"):
                                        logger.info('Command received: write byte (port B)')
                                        queue_general.put([data[0], "dummy_address", data[2]])
                                    #==============================================================
                                    # write a bit in Port B GPIO
                                    #elif (data[0] == "\x06"):
                                    #    queue_general.put([data[0], "dummy_address", data[2], data[3]])
                                    #==============================================================
                                    # read the whole byte in digital Port A
                                    elif (data[0] == "\x07"):
                                        logger.info('Command received: write byte (port A)')
                                        #byte = read_digital_input_byte(ord(command[1]))
                                        byte = read_digital_input_byte(board_address)
                                        connection.sendall(str(byte) + "\r\n")
                                        #print byte
                                    #==============================================================
                                    # read a bit in Port B GPIO
                                    elif (data[0] == "\x08"):
                                        #bit = read_digital_input_bit(ord(command[1]), ord(command[2]))
                                        bit = read_digital_input_bit(board_address, ord(data[2]))
                                        connection.sendall(str(bit) + "\r\n")
#                                        logger.info(bit)
                                    #==============================================================
                                    # generate a pulse in RESET bit (Port B, bit 3)
                                    elif (data[0] == "\x09"):
                                        logger.info('Command received: Reset')
                                        queue_general.put([data[0], "dummy_address", data[2]])
                                    #==============================================================
                                    # read interlock labels
                                    #elif (data[0] == "\x0A"):
                                    #    pass
                                    #==============================================================
                                    # read a Port B bit setpoint
                                    elif (data[0] == "\x0B"):
                                        #bit = read_portB_digital_output_bit(ord(command[1]), ord(command[2]))
                                        bit = read_portB_digital_output_bit(board_address, ord(data[2]))
                                        connection.sendall(str(bit) + "\r\n")
                                    #==============================================================
                                    # write bit in port B
                                    elif (data[0] == "\x0C"):
                                        logger.info('Command received: write bit (port B)')
                                        queue_general.put([data[0], "dummy_address", data[2], data[3]])
                                    #==============================================================
                                    # read input bit of port A
                                    #elif (data[0] == "\x0D"):
                                    #    pass
                                    #==============================================================
                                    # read input bit of port B
                                    elif (data[0] == "\x0E"):
                                        #bit = read_portB_digital_input_bit(ord(command[1]), ord(command[2]))
                                        bit = read_portB_digital_input_bit(board_address, ord(data[2]))
#                                        logger.info("Bit {}: {}".format(ord(data[2]), bit))
                                        connection.sendall(str(bit) + "\r\n")
                                    #==============================================================
                                    # read raw ADC input value
                                    elif (data[0] == "\x0F"):
                                        #voltage = read_analog_input_raw(ord(command[1]))
                                        voltage = read_analog_input_raw(board_address)
                                        connection.sendall(str(voltage) + "\r\n")
                                        #print str(voltage)
                                    #==============================================================
                                    # DAC setpoint parameters initialization 
                                    elif (data[0] == "\x10"):
                                        logger.info('Command received: init parameters at IOC reboot')
                                        init_values = data[2:].split(',')
                                        #------------------------------
                                        # separate values received
                                        voltage_factor = int(init_values[1])
                                        step_trigger = int(init_values[2])
                                        step_delay = int(init_values[3])
                                        #------------------------------
                                        # calculate trigger in DAC code
                                        trigger = step_trigger/(10.0*voltage_factor) * 131072
                                        steps = 4
                                        #------------------------------
                                        # return DAC RB (readback) value
                                        # dac_code = [0, 262143]
                                        last_setpoint = dac_code = read_analog_output(board_address)
                                        # voltage = [-10, 10]
                                        percentage = (dac_code - 131072.0)/131072
                                        # value = [131072, 10]
                                        value = int(percentage * voltage_factor * 131072 + 131072)
                                        connection.sendall(str(value) + "\r\n")
                                    #==============================================================
                                    # read input bit of port A
                                    elif (data[0] == "\x11"):
                                        #bit = read_portA_digital_input_bit(ord(command[1]), ord(command[2]))
                                        bit = read_portA_digital_input_bit(board_address, ord(data[2]))
#                                        logger.info("Bit {}: {}".format(ord(data[2]), bit))
                                        connection.sendall(str(bit) + "\r\n")
                                    #==============================================================
                                    # available command
                                    #elif (data[0] == "\x12"):
                                    #pass
                                    #==============================================================
                                    #==============================================================
                                    elif ("NLK" in socket.gethostname()):
                                        # NLK UPGRADE ----- DAC #2 setpoint parameters initialization 
                                        if (data[0] == "\x20"):
                                            logger.info('Command received for DAC #2: init parameters at IOC reboot')
                                            # return DAC RB (readback) value
                                            # dac_code = [0, 262143] - voltage = [-10, 10]
                                            percentage = (read_analog_output(board_address_2) - 131072.0)/131072
                                            # value = [131072, 10]
                                            value = int(percentage * voltage_factor * 131072 + 131072)
                                            connection.sendall(str(value) + "\r\n")
                                        #==============================================================
                                        # NLK UPGRADE ----- adjust DAC #2 output value
                                        elif (data[0] == "\x22"):
                                            # update last setpoint
                                            logger.info('Command received: voltage setpoint')
                                            queue_voltage.put([board_address_2, data[2:]])
                                        #==============================================================
                                        # NLK UPGRADE ----- read DAC #2 setpoint value
                                        elif (data[0] == "\x23"):
                                            connection.sendall(str(read_analog_output(board_address_2)) + "\r\n")
                                        #==============================================================
                                        # NLK UPGRADE ----- read maximum of 10 last ADC #2 input value
                                        elif (data[0] == "\x24"):
                                            voltage = read_analog_input(board_address_2)
                                            connection.sendall(str(voltage) + "\r\n")
                                        #==============================================================
                                        # NLK UPGRADE ----- read raw ADC #2 input value
                                        elif (data[0] == "\x2F"):
                                            voltage = read_analog_input_raw(board_address_2)
                                            connection.sendall(str(voltage) + "\r\n")
                                        #==============================================================
                                        # NLK UPGRADE ----- DAC #3 setpoint parameters initialization 
                                        elif (data[0] == "\x30"):
                                            logger.info('Command received for DAC #3: init parameters at IOC reboot')
                                            # return DAC RB (readback) value
                                            # dac_code = [0, 262143] - voltage = [-10, 10]
                                            percentage = (read_analog_output(board_address_3) - 131072.0)/131072
                                            # value = [131072, 10]
                                            value = int(percentage * voltage_factor * 131072 + 131072)
                                            connection.sendall(str(value) + "\r\n")
                                        #==============================================================
                                        # NLK UPGRADE ----- adjust DAC #3 output value
                                        elif (data[0] == "\x32"):
                                            # update last setpoint
                                            logger.info('Command received: voltage setpoint')
                                            queue_voltage.put([board_address_3, data[2:]])
                                        #==============================================================
                                        # NLK UPGRADE ----- read DAC #3 setpoint value
                                        elif (data[0] == "\x33"):
                                            connection.sendall(str(read_analog_output(board_address_3)) + "\r\n")
                                        #==============================================================
                                        # NLK UPGRADE ----- read maximum of 10 last ADC #3 input value
                                        elif (data[0] == "\x34"):
                                            voltage = read_analog_input(board_address_3)
                                            connection.sendall(str(voltage) + "\r\n")
                                        #==============================================================
                                        # NLK UPGRADE ----- read raw ADC #3 input value
                                        elif (data[0] == "\x3F"):
                                            voltage = read_analog_input_raw(board_address_3)
                                            connection.sendall(str(voltage) + "\r\n")
                                        #==============================================================

                        else:
                            break
                except Exception as e:
                    #logger.exception('Connection Error !')
                    logger.exception('Exception in socket thread: ', e)
                finally:
                    logger.info('Closing connection {}'.format(client_address))
                    connection.close()
        finally:
            sock.close()
    
    # thread that reads from 
    def read_from_list():
        global board_address
        global last_setpoint
        global logger
        while(True):
            try:
                while(True):
                    # wait until there is a command in the list
                    #while(queue_general.empty()):
                    #    pass
                    command = queue_general.get(block=True)
                    #==============================================================
                    # set GPIO pin direction
                    if (command[0] == "\x01"):
                        #set_direction_bit(int(ord(command[1])), command[2], int(ord(command[3])), int(command[4]))
                        set_direction_bit(board_address, command[2], int(ord(command[3])), int(command[4]))
                    #==============================================================
                    # adjust DAC output value
                    #elif (command[0] == "\x02"):
                    #==============================================================
                    # read DAC setpoint value
                    #elif (command[0] == "\x03"):
                    #==============================================================
                    # read maximum of 10 last ADC input value
                    #elif (command[0] == "\x04"):
                    #==============================================================
                    # write a whole byte in digital Port B
                    elif (command[0] == "\x05"):
                        #set_digital_output_byte(ord(command[1]), ord(command[2]))
                        set_digital_output_byte(board_address, ord(command[2]))
                    #==============================================================
                    # write a bit in Port B GPIO
                    #elif (command[0] == "\x06"):
                    #    #set_digital_output_bit(int(ord(command[1])), int(ord(command[2])), int(command[3]))
                    #    set_portB_digital_output_bit(board_address, int(ord(command[2])), int(command[3]))
                    #==============================================================
                    # read the whole byte in digital Port A
                    #elif (command[0] == "\x07"):
                    #==============================================================
                    # read a bit in Port B GPIO
                    #elif (command[0] == "\x08"):
                    #==============================================================
                    # generate a pulse in RESET bit (Port B, bit 3)
                    elif (command[0] == "\x09"):
                        #reset(ord(command[1]), int(command[2]))
                        logger.info('Reset command')
                        reset(board_address, int(command[2]))
                    #==============================================================
                    # read interlock labels
                    elif (command[0] == "\x0A"):
                        #connection.sendall(interlocks)
                        pass
                    #==============================================================
                    # read a Port B bit setpoint
                    #elif (command[0] == "\x0B"):
                    #==============================================================
                    # write to port B bit
                    elif (command[0] == "\x0C"):
                        #set_portB_digital_output_bit(int(ord(command[1])), int(ord(command[2])), int(command[3]))
                        #-----------------------------------------
                        # check if command is related to PwrState-Sel (bit 1) and
                        #   ... if command is to power the PS on and
                        #   ... if PS is turned off
                        #if ( (int(ord(command[2])) == 1) and (int(command[3]) == 1) and (read_portB_digital_input_bit(board_address, 7) == 0) ):
                        if ( (int(ord(command[2])) == 1) and (int(command[3]) == 1) and (read_portB_digital_output_bit(board_address, 1) == 0) ):
                            #logger.info('Turning PS on')
                            logger.info('Set voltage to zero to turn PS on')
                            # force voltage setpoint to be zero
                            queue_voltage.put([board_address, 131072])
                            # wait until voltage setpoint is zero
                            while (read_analog_output(board_address) != 131072):
                                pass
                            # power the PS on 
                            logger.info('Turning PS on...')
                            set_portB_digital_output_bit(board_address, int(ord(command[2])), 1)
                            time.sleep(0.5)
                            #-----------------------------
                            # wait until PwrState-Sts (bit 7) is 1
                            #while (read_portB_digital_input_bit(board_address, 7) != 1):
                            #    pass
                            #-----------------------------
                            # wait until PwrState-Sel (bit 1) is 0
                            while (read_portB_digital_output_bit(board_address, 1) != 1):
                                pass
                            logger.info('PS is on')
                            #-----------------------------
                            # restore last voltage setpoint
                            logger.info('Restoring voltage setpoint...')
                            queue_voltage.put([board_address, last_setpoint])
                        #-----------------------------------------
                        else:
                            cmd = ord(command[2])
                            bit = int(command[3])
                            if (cmd == 1):
                                if (bit == 0):
                                    logger.info('PS off')
                                elif (bit == 1):
                                    logger.info('PS on')
                            elif (cmd == 2):
                                if (bit == 0):
                                    logger.info('Pulse disabled')
                                elif (bit == 1):
                                    logger.info('Pulse enabled')
                            else:
                                logger.info('Change bit {}'.format(bit))
                            set_portB_digital_output_bit(board_address, int(ord(command[2])), int(command[3]))
                    #==============================================================
                    #
                    #elif (command[0] == "\x0D"):
                    #==============================================================
                    #
                    #elif (command[0] == "\x0E"):
                    #==============================================================
                    # read raw ADC input value
                    #elif (command[0] == "\x0F"):
                    #==============================================================
                    # available command
                    #elif (command[0] == "\x10"):
                    #==============================================================
            except:
                logger.exception('Error in thread 2! (reading from list)')


    def voltage_adjustment():
        global last_setpoint
        global logger
        global board_calibration

        while(True):
            try:
                while(True):
                    # wait until there is a command in the list
                    #while(queue_voltage.empty()):
                        # check if Voltage-SP is equal to Voltage-RB
                        #if((last_setpoint < (read_analog_output(board_address) - 1)) or (last_setpoint > (read_analog_output(board_address) + 1))):
                        #    logger.info('SP different from RB')
                        #    queue_voltage.put(last_setpoint)
                    #    pass
                    #==============================================================
                    # adjust DAC output value
                    # command[0] = "\x0"
                    voltage_steps(queue_voltage.get(block = True))
            except:
                logger.exception('Error in thread 3! (voltage thread)')

    def voltage_steps(info):
        # info = [board, value]
        global voltage_factor
        global step_trigger
        global step_delay
        global trigger
        global steps
        global logger
        global board_calibration

        board = info[0]
        value = int(info[1])
        current = read_analog_output(board)
        logger.info("Board: {} - Value {} - Current: {}".format(board, value, current))
        #-----------------------------------------
        # if PS is off, implement setpoint directly
        #if (read_portB_digital_input_bit(board_address, 7) == 0):
        #if (read_portB_digital_output_bit(board_address, 1) == 0):
        #    set_analog_output(board_address, value)
        #-----------------------------------------
        #else:
        # check difference between current and intended setpoint
        diff = value - current
        #-----------------------------------------
        # if difference is lower than the amount to activate the steps trigger
        # then implement new setpoint directly
        if diff < trigger:
            logger.info('Voltage setpoint: {:.2f}'.format((value-131072.0)/131072*voltage_factor*10) + ' V')
            set_analog_output(board, value)
        #-----------------------------------------
        # if difference is higher than the amount to activate the steps trigger
        # then calculate calculate graduals setpoints
        else:
            #logger.info('Voltage adjustment exceeds limiar: gradual adjust required!')
            setpoints = [int(current+(i*diff)/steps) for i in range(1,steps)]
            # loop for "steps-1" gradual setpoints
            for i, voltage in enumerate(setpoints):
                logger.info(' - Voltage step %d: {:.2f}'.format((voltage-131072.0)/131072*voltage_factor*10) %(i+1) + ' V')
                set_analog_output(board, voltage)
                start = time.time()
                while(time.time() - start < step_delay):
                   time.sleep(0.1)
                    
            # adjust last step
            set_analog_output(board, value)
            logger.info(' - Voltage step %d: {:.2f}'.format((value-131072.0)/131072*voltage_factor*10) %(i+2) + ' V')
        #-----------------------------------------
        return

    # instantiate object Lock            
    global lock
    lock = Lock()
    # define threads            
    thr_1 = Thread(target=write_to_list, args=())
    thr_2 = Thread(target=read_from_list, args=())
    thr_3 = Thread(target=voltage_adjustment, args=())
    # start threads
    thr_1.start()
    time.sleep(3)
    thr_2.start()
    thr_3.start()
