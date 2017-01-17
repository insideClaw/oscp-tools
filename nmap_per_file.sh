#!/bin/bash
if [ $# -ne 2 ]; then 
  echo "USAGE: $0 <file_of_IPs> <ports>"
  exit 1
fi

#ports="80,445"
IPs=$(cat $1)
ports=$2

# Remove the -oX if outputting in XML format for MagicTree not desired
for ip in $IPs; do
# nmap -Pn -A -p $ports $ip -oX data/xml/$(echo $ip).xml &
  nmap --script=smb-brute $ip -p $ports > data/$(echo $ip)_bruteforce.txt &
done
