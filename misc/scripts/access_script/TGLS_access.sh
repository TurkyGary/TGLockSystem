#!/usr/bin/env bash

# This script is temporary solution to generate granted access files to the TGLockSystem

# 'dlist.csv' file is the formated original data to use for this script.
# it follows this format "{User_Number},{User_Name},{First_Number},{Second_Number},{Third_Number}"

#echo $line;
touch ./TGLSraw_$(date +%d%b%Y_%H%M).tmp
touch ./TGLScred_$(date +%d%b%Y_%H%M).access
echo "NOTE: The following lines should be copied to thier cossesponding files..." >> TGLScred_$(date +%d%b%Y_%H%M).access
echo "(access_list.csv) file:" > al.tmp
echo "(granted.csv) file:" > g.tmp
echo "(.bkp.log) file:" > bkp.tmp

while read line; do

#echo $line
IFS=',' read -r userID NAME VN FN CN <<< "$line"

#echo -e "$userID,\c"
#echo -e "$NAME,\c"
#echo -e "$FN,\c"
#echo -e "$VN,\c"
#echo -e "$CN"

# ======START====== Calculating Card Raw ID ======START====== #
# --- Input Variables ---
#VN: Version (Hex)
#FN: Facility (Hex)
#CN: Card Number (Decimal)

# 1. Convert inputs to integers for calculation
v_int=$((16#$VN))
f_int=$((16#$FN))
c_int=$CN

# 2. Split Card Number into MSB and LSB
c_msb=$(( (c_int >> 8) & 0xFF ))
c_lsb=$(( c_int & 0xFF ))

# 3. Calculate Checksum
# (0xF0 + Facility + Version + CardMSB + CardLSB) mod 256, then XOR with 0xFF
sum=$(( 0xF0 + f_int + v_int + c_msb + c_lsb ))
chk_sum_byte=$(( sum & 0xFF ))
checksum=$(( 0xFF ^ chk_sum_byte ))

# 4. Helper function to convert Int to 8-bit Binary string
to_bin() {
    local val=$1
    local bin=""
    for ((i=7; i>=0; i--)); do
        bin+=$(( (val >> i) & 1 ))
    done
    echo "$bin"
}

# 5. Build the 64-bit Binary Stream with IoProx delimiters (Stop Bits)
# Pattern: [8-bits data] + [Stop Bit]
bits=""
bits+="$(to_bin 0)0"           # Preamble (0x00) + 0
bits+="$(to_bin 240)1"         # Static Sync (0xF0) + 1
bits+="$(to_bin $f_int)1"      # Facility + 1
bits+="$(to_bin $v_int)1"      # Version + 1
bits+="$(to_bin $c_msb)1"      # Card MSB + 1
bits+="$(to_bin $c_lsb)1"      # Card LSB + 1
bits+="$(to_bin $checksum)11"  # Checksum + 11 (Tail)

# 6. Convert the 64-bit Binary String to Hexadecimal
raw_hex=$(printf '%016X' "$((2#$bits))")

# 7. Convert raw_hex to small letters
raw_hex="${raw_hex,,}"

# --- Output Results ---
echo "------------------------------------------" >> TGLSraw_$(date +%d%b%Y_%H%M).tmp
echo "$NAME ($userID):" >> TGLSraw_$(date +%d%b%Y_%H%M).tmp
echo "IoProx Parameters:" >> TGLSraw_$(date +%d%b%Y_%H%M).tmp
echo "  Version (VN):  $VN" >> TGLSraw_$(date +%d%b%Y_%H%M).tmp
echo "  Facility (FN): $FN" >> TGLSraw_$(date +%d%b%Y_%H%M).tmp
echo "  Card (CN):     $CN" >> TGLSraw_$(date +%d%b%Y_%H%M).tmp
echo "Calculated Raw ID: $raw_hex" >> TGLSraw_$(date +%d%b%Y_%H%M).tmp
echo "------------------------------------------" >> TGLSraw_$(date +%d%b%Y_%H%M).tmp
echo "" >> TGLSraw_$(date +%d%b%Y_%H%M).tmp
# ======END====== Calculating Card Raw ID ======END====== #

# ======START====== Generate Access Credentials ======START====== #
echo "$userID,$raw_hex" >> al.tmp
echo "$userID" >> g.tmp
echo "[$(date +%Y%b%d_%H%M%S)]IOProx,XSF($VN)$FN:$CN,Raw:$raw_hex(ok),$userID,$NAME" >> bkp.tmp
# ======END====== Generate Access Credentials ======END====== #

done < dlist.csv

(cat al.tmp; echo ""; cat g.tmp; echo ""; cat bkp.tmp;) >> ./TGLScred_$(date +%d%b%Y_%H%M).access
rm -f al.tmp g.tmp bkp.tmp

