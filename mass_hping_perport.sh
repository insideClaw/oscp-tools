#!/bin/bash
#file=data/snooped_ping
#file="data/ssh_responded_fast_IPs_clean"
port=$1
for ip in `seq 1 254`; do 
#  echo "Pinging 10.11.1.$ip"
  hping3 -S -c 1 -p $port 10.11.1.$ip 2>/dev/null | grep flags=SA | egrep -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' &
done
