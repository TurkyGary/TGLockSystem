#!/bin/bash

# Configuration
SSID="TGLOCKSYS"
PASS="tglocksys"
CON_NAME="TGLockHotspot"
PI_IP="192.168.192.168/24"
DURATION=1200

echo "--- Configuring TGLOCKSYS (192.168.192.168) ---"

# 1. Create/Modify the profile with the specific IP
if ! nmcli con show "$CON_NAME" > /dev/null 2>&1; then
    sudo nmcli con add type wifi ifname wlan0 mode ap con-name "$CON_NAME" ssid "$SSID"
fi

sudo nmcli con modify "$CON_NAME" 802-11-wireless-security.key-mgmt wpa-psk
sudo nmcli con modify "$CON_NAME" 802-11-wireless-security.psk "$PASS"
sudo nmcli con modify "$CON_NAME" ipv4.method shared ipv4.addresses "$PI_IP"

# 2. Limit to 2 devices (Custom dnsmasq config for NetworkManager)
# This creates a rule: start at .169, end at .170 (exactly 2 IPs)
CONF_FILE="/etc/NetworkManager/dnsmasq-shared.d/limit-clients.conf"
sudo mkdir -p /etc/NetworkManager/dnsmasq-shared.d/
echo "dhcp-range=192.168.192.169,192.168.192.170,12h" | sudo tee $CONF_FILE > /dev/null

# 3. Start the Hotspot
sudo iw dev wlan0 set power_save off
sudo nmcli con up "$CON_NAME"

echo "Hotspot active at 192.168.192.168"
echo "Only 2 devices can receive IP addresses (.169 and .170)."

sleep $DURATION

# 4. Cleanup
sudo nmcli con down "$CON_NAME"
echo "Hotspot deactivated."
