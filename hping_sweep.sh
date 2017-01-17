#!/bin/bash
# -1 allows ICMP sweet instead of port
for ip in $(seq 1 254);do
  hping3 -c 1 -S -p 80 192.168.0.$ip 2>&1 | grep flags &
done
