#!/usr/bin/env bash
#Rescan for new wifi networks
sudo nmcli device wifi rescan

#Connect to hotspot
sudo nmcli device wifi connect iTAGx_MateBookPro
