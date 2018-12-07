#!/usr/bin/python

import sys

import init
import selection
import flash
import dac
import adc

board = int(sys.argv[1])

selection.flash(board)
flash.info_write(board)

dac.calibration(board)
adc.calibration(board)
