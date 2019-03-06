#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import path
from pydm import Display
import sys
import json

class DeviceMenu(Display):
    def __init__(self, parent=None, args=[], macros=None):
        super(DeviceMenu, self).__init__(parent=parent, args=args, macros=macros)

        # defining macros for PyDMShellCommand
        #self.***object_name***.macros = json.dumps({"pv_prefix":"TB-04:PU-InjSept"})
        #self.***object_name***.macros = json.dumps({"pv_prefix":"BO-01D:PU-InjKckr"})

    def ui_filename(self):
        return '../ui/main_window.ui'

    def ui_filepath(self):
        return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())
