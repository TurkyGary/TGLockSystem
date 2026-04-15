#!/usr/bin/env bash
#Rescan for new wifi networks
sudo nmcli device wifi rescan

#Pause for 5 seconds
sleep 5

#Connect to hotspot
sudo nmcli device wifi connect iTAGx_MateBookPro
