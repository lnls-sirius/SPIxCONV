#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e
#-------------------------------------------------
# check if script is running as root
#-------------------------------------------------
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit 1
fi
#-------------------------------------------------
# copy image to the default icons folder
#-------------------------------------------------
if [ -d /usr/share/icons ]
then
  if [ ! -e /usr/share/icons/septum.png ]
  then
    echo "Copying icon to /usr/share/icons"
    cp septum.png /usr/share/icons
  else
    echo "Icon already exist in /usr/share/icons"
  fi
else
  echo "/usr/share/icon folder does not exist"
  exit 1
fi
#-------------------------------------------------
# copy shortcut (.desktop file) to the Desktop folder
#-------------------------------------------------
# check user who invoked sudo
HOME="/home/$SUDO_USER"
if [ -d $HOME/Desktop ]
then
  if [ ! -e $HOME/Desktop/epp_display.desktop ]
  then
    echo "Copying desktop file to $HOME/Desktop"
    cp epp_display.desktop $HOME/Desktop
    # change user and group
    chown $SUDO_USER $HOME/Desktop/epp_display.desktop
    chgrp $SUDO_USER $HOME/Desktop/epp_display.desktop
  else
    echo "File already exist in $HOME/Desktop"
  fi
else
  echo "Desktop folder does not exist"
  exit 1
fi
#-------------------------------------------------
exit 0
