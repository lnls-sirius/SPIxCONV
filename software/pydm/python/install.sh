#!/bin/bash
set -e
set -x

DESKTOP=/home/$(whoami)/Desktop
if [ -d $DESKTOP ]; then
    echo 'ok'
else
    echo 'Desktop folder not found!'
    exit 1
fi
cat lnls-con-epp.desktop.template | S_DIR=$(pwd) envsubst > $DESKTOP/lnls-con-epp.desktop
