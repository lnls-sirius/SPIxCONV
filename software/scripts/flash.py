#!/usr/bin/python3

from Adafruit_BBIO.SPI import SPI
import selection
import sys
import struct
import time
#-------------------------------------------------------
# initialize the bus and device /dev/spidev1.0
spi = SPI(0,0)
'''
=============================================================================
    GENERAL INFORMATIONS
=============================================================================
    data stored         data format                 length       address
    -------------------------------------------------------------------------
    version:            255.255                      2 bytes     0x00 to 0x01
    date:               08/2017                      4 bytes     0x02 to 0x05
    board ID:           0x04                         1 byte      0x06
    board address:      from 0 to 7                  1 byte      0x07
    board type:         SPIxCONV                     8 bytes     0x08 to 0x0F
    copyright:          Controls Group              24 bytes     0x10 to 0x27
                        guilherme.franco@lnls.br    24 bytes     0x28 to 0x3F
                        rafael.ito@lnls.br          24 bytes     0x40 to 0x57
    DAC calibration:    gain                         4 bytes     0x58 to 0x5B
                        offset                       4 bytes     0x5C to 0x5F
    ADC calibration:    gain                         4 bytes     0x60 to 0x63
                        offset                       4 bytes     0x64 to 0x67
=============================================================================
    SCRIPTS INFORMATIONS
=============================================================================
    script                  file size       block (64 kB)   upper/lower part
    -------------------------------------------------------------------------
    init.py                 298 bytes       1 (0x010000)    lower half
    selection.py             6.1 kB         1 (0x018000)    upper half
    dac.py                  10.7 kB         2 (0x020000)    lower half
    adc.py                   9.6 kB         2 (0x028000)    upper half
    flash.py                22.3 kB         3 (0x030000)    lower half
    digital.py               2.7 kB         3 (0x038000)    upper half
    Agilent34420A.py         2.4 kB         4 (0x040000)    lower half
    tests.py                31.2 kB         4 (0x048000)    upper half
=============================================================================
    OTHER INFORMATIONS
=============================================================================
    Altera CPLD file (.bdf format):
        size:       118.1 kB
        blocks:     5 and 6 (128 kB)
        address:    0x050000 to 0x06FFFF
=============================================================================
    DIGITAL OUTPUT
=============================================================================
    data stored       description    block (64 kB)   length  upper/lower part
    -------------------------------------------------------------------------
    digital output:   previous state  5 (0x050000)   1 byte     lower half
     -verification    check if reset  5 (0x050008)   1 byte     lower half
    digital output:   current state   5 (0x058000)   1 byte     upper half
     -verification    check if reset  5 (0x058008)   1 byte     upper half
'''
#=====================================================================
# Board informations
#=====================================================================
# write board informations
def info_write(board):
    selection.flash(board)
    # general info
    version_write(board, 1.1)
    date_write(board, "15/08/2017")
    ID_write(board, 0x04)
    address_write(board, (int(board) % 8))
    boardtype_write(board, "SPIxCONV")
    group_write(board, "Controls Group")
    member1_write(board, "guilherme.franco@lnls.br")
    member2_write(board, "rafael.ito@lnls.br")
    # calibration info
    dac_gain_write(board, 1)
    dac_offset_write(board, 0)
    adc_gain_write(board, 1)
    adc_offset_write(board, 0)
# read board informations
def info_read(board):
    selection.flash(board)
    # general info
    version_read(board)
    date_read(board)
    ID_read(board)
    address_read(board)
    boardtype_read(board)
    group_read(board)
    member1_read(board)
    member2_read(board)
    # calibration info
    print("DAC gain       =  {}".format(dac_gain_read(board)))
    print("DAC offset     =  {}".format(dac_offset_read(board)))
    print("ADC gain       =  {}".format(adc_gain_read(board)))
    print("ADC offset     =  {}".format(adc_offset_read(board)))
#=====================================================================
# VERSION (2 bytes --> from 0x00 to 0x01)
#=====================================================================
# read version
def version_read(board):
    version = read(board, 0x00, 2)
    print("version: {}.{}".format(version[0], version[1]))
#---------------------------------------------------------------------
# write version
def version_write(board, version):
    # write new version
    version_str = str(version)
    v1 = int(version_str[0:(version_str.find("."))])
    v2 = int(version_str[(version_str.find(".") + 1):len(version_str)])
    #write(board, 0x00, [v1, v2])
    sector_write(board, 0x00, [v1, v2])
#=====================================================================
# DATE (3 bytes --> from 0x02 to 0x05)
#=====================================================================
# read date
def date_read(board):
    date = read(board, 0x02, 4)
    print("date: {:02d}/{:02d}/{}{}".format(date[0], date[1], date[2], date[3]))
#---------------------------------------------------------------------
# write date
def date_write(board, date):
    # date should be a string
    day    = int(date[0:2])
    month  = int(date[3:5])
    year_1 = int(date[6:8])
    year_2 = int(date[8:10])
    #write(board, 0x02, [day, month, year_1, year_2])
    sector_write(board, 0x02, [day, month, year_1, year_2])
#=====================================================================
# BOARD ID (1 bytes --> 0x06)
#=====================================================================
# read board ID
def ID_read(board):
    ID = read(board, 0x06, 1)
    print("board ID: 0x{:X}".format(ID[0]))
    return(ID[0])
#---------------------------------------------------------------------
# write board ID
def ID_write(board, ID):
    #write(board, 0x06, [ID])
    sector_write(board, 0x06, [ID])
#=====================================================================
# BOARD ADDRESS (1 bytes --> 0x07)
#=====================================================================
# read board address
def address_read(board):
    address = read(board, 0x07, 1)
    print("board address: {}".format(address[0]))
    return(address[0])
#---------------------------------------------------------------------
# write board address
def address_write(board, address):
    #write(board, 0x07, [address])
    sector_write(board, 0x07, [address])
#=====================================================================
# BOARD TYPE (8 bytes --> from 0x08 to 0x0F)
#=====================================================================
# read board type
def boardtype_read(board):
    boardtype = read(board, 0x08, 8)
    sys.stdout.write("board type: ")
    for i in range(8):
        sys.stdout.write(chr(boardtype[i]))
    sys.stdout.write("\n")
#---------------------------------------------------------------------
# write board type
def boardtype_write(board, boardtype):
    # boardtype should be a string
    if(len(boardtype) <= 8):
        boardtype_int = []
        for i in range(len(boardtype)):
            boardtype_int.append(ord(boardtype[i]))
        #write(board, 0x08, boardtype_int)
        sector_write(board, 0x08, boardtype_int)
    else:
        print("error: board type should not have more than 8 characters")
#=====================================================================
# COPYRIGHT GROUP (24 bytes --> from 0x10 to 0x27)
#=====================================================================
# read copyright group
def group_read(board):
    group = read(board, 0x10, 24)
    sys.stdout.write("copyright group: ")
    for i in range(24):
        sys.stdout.write(chr(group[i]))
    sys.stdout.write("\n")
#---------------------------------------------------------------------
# write copyright group
def group_write(board, group):
    # group should be a string
    if(len(group) <= 24):
        group_int = []
        for i in range(len(group)):
            group_int.append(ord(group[i]))
        for i in range(24 - len(group)):
            group_int.append(32)
        #write(board, 0x10, group_int)
        sector_write(board, 0x10, group_int)
    else:
        print("error: group should not have more than 24 characters")
#=====================================================================
# COPYRIGHT MEMBER 1 (24 bytes --> from 0x28 to 0x3F)
#=====================================================================
# read copyright member 1
def member1_read(board):
    member1 = read(board, 0x28, 24)
    sys.stdout.write("copyright member 1: ")
    for i in range(24):
        sys.stdout.write(chr(member1[i]))
    sys.stdout.write("\n")
#---------------------------------------------------------------------
# write read copyright member 1
def member1_write(board, member1):
    # group should be a string
    if(len(member1) <= 24):
        member1_int = []
        for i in range(len(member1)):
            member1_int.append(ord(member1[i]))
        for i in range(24 - len(member1)):
            member1_int.append(32)
        #write(board, 0x28, member1_int)
        sector_write(board, 0x28, member1_int)
    else:
        print("error: member field should not have more than 24 characters")
#=====================================================================
# COPYRIGHT MEMBER 2 (24 bytes --> from 0x40 to 0x57)
#=====================================================================
# read copyright member 2
def member2_read(board):
    member2 = read(board, 0x40, 24)
    sys.stdout.write("copyright member 2: ")
    for i in range(24):
        sys.stdout.write(chr(member2[i]))
    sys.stdout.write("\n")
#---------------------------------------------------------------------
# write read copyright member 2
def member2_write(board, member2):
    # group should be a string
    if(len(member2) <= 24):
        member2_int = []
        for i in range(len(member2)):
            member2_int.append(ord(member2[i]))
        for i in range(24 - len(member2)):
            member2_int.append(32)
        #write(board, 0x40, member2_int)
        sector_write(board, 0x40, member2_int)
    else:
        print("error: member field should not have more than 24 characters")
#=====================================================================
# DAC CALIBRATION (8 bytes --> from 0x58 to 0x5F)
#=====================================================================
# read DAC GAIN parameter
def dac_gain_read(board):
    gain = read(board, 0x58, 4)
    gain_bytes = []
    for i in range(4):
        gain_bytes.append(chr(gain[i]))
    string = gain_bytes[0] + gain_bytes[1] + gain_bytes[2] + gain_bytes[3]
    gain = struct.unpack('f', string)
    #print("DAC gain = %s" %gain)
    gain = float(gain[0])
    return gain
#---------------------------------------------------------------------
# write DAC GAIN parameter
def dac_gain_write(board, gain):
    gain = struct.pack('f', gain)
    gain_bytes = []
    for i in range(4):
        gain_bytes.append(ord(gain[i]))
    #write(board, 0x58, gain_bytes)
    sector_write(board, 0x58, gain_bytes)
#---------------------------------------------------------------------
# read DAC OFFSET parameter
def dac_offset_read(board):
    offset = read(board, 0x5C, 4)
    offset_bytes = []
    for i in range(4):
        offset_bytes.append(chr(offset[i]))
    string = offset_bytes[0] + offset_bytes[1] + offset_bytes[2] + offset_bytes[3]
    offset = struct.unpack('f', string)
    #print("DAC offset = %s" %offset)
    offset = float(offset[0])
    return offset
#---------------------------------------------------------------------
# write DAC OFFSET parameter
def dac_offset_write(board, offset):
    offset = struct.pack('f', offset)
    offset_bytes = []
    for i in range(4):
        offset_bytes.append(ord(offset[i]))
    #write(board, 0x5C, offset_bytes)
    sector_write(board, 0x5C, offset_bytes)
#=====================================================================
# ADC CALIBRATION (12 bytes --> from 0x60 to 0x6B)
#=====================================================================
'''
# read ADC REFERENCE parameter
def adc_reference_read(board):
    reference = read(board, 0x60, 4)
    reference_bytes = []
    for i in range(4):
        reference_bytes.append(chr(reference[i]))
    string = reference_bytes[0] + reference_bytes[1] + reference_bytes[2] + reference_bytes[3]
    reference = struct.unpack('f', string)
    #print("ADC reference = %s" %reference)
    reference = float(reference[0])
    return reference
#---------------------------------------------------------------------
# write ADC REFERENCE parameter
def adc_reference_write(board, reference):
    reference = struct.pack('f', reference)
    reference_bytes = []
    for i in range(4):
        reference_bytes.append(ord(reference[i]))
    #write(board, 0x60, reference_bytes)
    sector_write(board, 0x60, reference_bytes)
'''
#=====================================================================
# read ADC GAIN parameter
def adc_gain_read(board):
    gain = read(board, 0x60, 4)
    gain_bytes = []
    for i in range(4):
        gain_bytes.append(chr(gain[i]))
    string = gain_bytes[0] + gain_bytes[1] + gain_bytes[2] + gain_bytes[3]
    gain = struct.unpack('f', string)
    #print("ADC gain = %s" %gain)
    gain = float(gain[0])
    return gain
#---------------------------------------------------------------------
# write ADC GAIN parameter
def adc_gain_write(board, gain):
    gain = struct.pack('f', gain)
    gain_bytes = []
    for i in range(4):
        gain_bytes.append(ord(gain[i]))
    #write(board, 0x64, gain_bytes)
    sector_write(board, 0x60, gain_bytes)
#=====================================================================
# read ADC OFFSET parameter
def adc_offset_read(board):
    offset = read(board, 0x64, 4)
    offset_bytes = []
    for i in range(4):
        offset_bytes.append(chr(offset[i]))
    string = offset_bytes[0] + offset_bytes[1] + offset_bytes[2] + offset_bytes[3]
    offset = struct.unpack('f', string)
    #print("ADC offset = %s" %offset)
    offset = float(offset[0])
    return offset
#---------------------------------------------------------------------
# write ADC OFFSET parameter
def adc_offset_write(board, offset):
    offset = struct.pack('f', offset)
    offset_bytes = []
    for i in range(4):
        offset_bytes.append(ord(offset[i]))
    #write(board, 0x68, offset_bytes)
    sector_write(board, 0x64, offset_bytes)
#=====================================================================
# READ the STATUS REGISTERS (SR1 and SR2)
#=====================================================================
def read_SR(board):
    # select device FLASH
    selection.flash(board)
    # write enable
    spi.writebytes([0x06])
    # read Status Register 1 and 2
    SR1 = spi.xfer2([0x05, 0x00])
    SR2 = spi.xfer2([0x35, 0x00])
    print("after enable")
    print("SR1 = " + str(bin(SR1[1])))
    print("SR2 = " + str(bin(SR2[1])) + "\n")
#=====================================================================
# READ SECTOR
#=====================================================================
# this function read a whole 4KB sector
def sector_read(board, address):
    # each sector correspond to 16 pages of 256 bytes
    # initial address is the beginning of the sector
    initial_address = address - (address % 4096)
    # pages is a 16 length array, where each element is another array that contains a full page (256 bytes)
    pages = [0]*16
    address = initial_address
    # reading loop for each page
    for i in range(16):
        # read a full page
        pages[i] = read(board, address, 256)
        address += 256
    return pages
# this function write in a memory position
def sector_write(board, address, value):
    # each sector correspond to 16 pages of 256 bytes
    # initial address is the beginning of the sector
    initial_address = address - (address % 4096)
    # relative address is the offset inside the sector
    relative_address = address % 256
    # page is the relative position inside the sector
    page = (address/256) % 16
    # read and store previous state of whole sector
    # backup is an array that contains 16 arrays (each corresponding to a page memory) with size 256
    backup = sector_read(board, address)
    sector = backup
    # update new values in correspondent position
    for i in range(len(value)):
        sector[page][relative_address+i] = value[i]
    # erase whole sector (smallest memory size that can be erased)
    erase_sector(board, address)
    time.sleep(0.1)
    # write sector with updated values in flash memory
    address = initial_address
    for i in range(16):
        write(board, address, sector[i])
        address += 256
    #return sector
#=====================================================================
# erase sector of FLASH memory
#=====================================================================
# SECTOR ERASE (4KB)
def erase_sector(board, address):
    # split address in 3 bytes
    address = "{:06x}".format(int(address))
    add_2 = int(address[0:2],16)
    add_1 = int(address[2:4],16)
    add_0 = int(address[4:6],16)
    # select device FLASH
    selection.flash(board)
    # write enable
    spi.writebytes([0x06])
    spi.writebytes([0x20, add_2, add_1, add_0])
#---------------------------------------------------------------------
# 32KB BLOCK ERASE
def erase_32k_block(board, address):
    # split address in 3 bytes
    address = "{:06x}".format(int(address))
    add_2 = int(address[0:2],16)
    add_1 = int(address[2:4],16)
    add_0 = int(address[4:6],16)
    # select device FLASH
    selection.flash(board)
    # write enable
    spi.writebytes([0x06])
    spi.writebytes([0x52, add_2, add_1, add_0])
#---------------------------------------------------------------------
# 64KB BLOCK ERASE
def erase_64k_block(board, address):
    # split address in 3 bytes
    address = "{:06x}".format(int(address))
    add_2 = int(address[0:2],16)
    add_1 = int(address[2:4],16)
    add_0 = int(address[4:6],16)
    # select device FLASH
    selection.flash(board)
    # write enable
    spi.writebytes([0x06])
    spi.writebytes([0xD8, add_2, add_1, add_0])
#---------------------------------------------------------------------
# CHIP ERASE
def erase_chip(board):
    # select device FLASH
    selection.flash(board)
    # write enable
    spi.writebytes([0x06])
    spi.writebytes([0x60])
#=====================================================================
#aux = spi.xfer2([0x90, 0x00, 0x00, 0x00, 0x00, 0x00])
#print("aux = " + str(aux))
#print("manufacturer ID = " + str("{:02x}".format(int(aux[4]))).upper() + "h")
#print("device ID = " + str("{:02x}".format(int(aux[5]))) + "h")
#=====================================================================
# WRITE value from flash memory
#=====================================================================
def write(board, address, value):
    # select device FLASH
    selection.flash(board)
    # write enable
    spi.writebytes([0x06])
    # split address in 3 bytes
    address = "{:06x}".format(int(address))
    add_2 = int(address[0:2],16)
    add_1 = int(address[2:4],16)
    add_0 = int(address[4:6],16)
    # prepare bytes to send
    data = []
    # append 1-byte command
    data.append(0x02)
    # append 3-bytes ADDRESS
    data.append(add_2)
    data.append(add_1)
    data.append(add_0)
    # append data to be written
    for aux in range(len(value)):
        data.append(value[aux])
    #print(data)
    #data += value
    spi.writebytes(data)
    # check BUSY bit
    BUSY = 1
    while (BUSY == 1):
        SR1 = spi.xfer2([0x05, 0x00])
        # create a mask to check just BUSY status
        BUSY = (SR1[1] & 0x01)
        # wait until BUSY = 0 again
#=====================================================================
# READ value from flash memory
#=====================================================================
def read(board, address, size):
    # select device FLASH
    selection.flash(board)
    # prepare bytes to send
    data = []
    # append 1-byte command
    data.append(0x03)
    # split address in 3 bytes
    address = "{:06x}".format(int(address))
    add_2 = int(address[0:2],16)
    add_1 = int(address[2:4],16)
    add_0 = int(address[4:6],16)
    # append 3-bytes ADDRESS
    data.append(add_2)
    data.append(add_1)
    data.append(add_0)
    # append number of data to be read
    for aux in range(size):
        data.append(0x00)
    read = spi.xfer2(data)
    #print(read[4:len(read)])
    return read[4:len(read)]
#=====================================================================
# STORE/LOAD script in memory
#=====================================================================
# read script from memory
def script_read(board, address, filename):
    counter = 0
    # read one byte
    byte = read(board, address, 1)
    # open python file to save script
    #filename = filename.replace(".py", "_python.py")
    log = open(filename, "w")
    # loop until "End of Text" (^C) is reached
    while (byte[0] != 0x03):
        log.write(chr(byte[0]))
        counter += 1
        # increment address and request one more reading
        address += 1
        byte = read(board, address, 1)
    return counter
# write script from memory
def script_write(board, address, filename):
    counter = 0
    with open(filename, "r") as f:
        erase_32k_block(board, address)
        time.sleep(1)
        byte = f.read(1)
        # while EOF is not reached
        while byte != "":
            write(board, address, [ord(byte)])
            counter += 1
            address += 1
            byte = f.read(1)
        # write "End of Text" (^C) to signal file reached the end
        write(board, address, [0x03])
    return counter
#=====================================================================
# SCRIPTS load/store (all scripts)
#=====================================================================
# store all scripts
def scripts_store(board):
    script_write(board, 0x010000, "init.py")
    script_write(board, 0x018000, "selection.py")
    script_write(board, 0x020000, "dac.py")
    script_write(board, 0x028000, "adc.py")
    script_write(board, 0x030000, "flash.py")
    script_write(board, 0x038000, "digital.py")
    script_write(board, 0x040000, "Agilent34420A.py")
    script_write(board, 0x048000, "tests.py")
    script_write(board, 0x050000, "SPIxCONV_v1_2_CPLD.bdf")
# load all scripts
def scripts_load(board):
    script_read(board, 0x010000, "init.py")
    script_read(board, 0x018000, "selection.py")
    script_read(board, 0x020000, "dac.py")
    script_read(board, 0x028000, "adc.py")
    script_read(board, 0x030000, "flash.py")
    script_read(board, 0x038000, "digital.py")
    script_read(board, 0x040000, "Agilent34420A.py")
    script_read(board, 0x048000, "tests.py")
    script_read(board, 0x050000, "SPIxCONV_v1_2_CPLD.bdf")
#=====================================================================
