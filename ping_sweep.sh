#!/bin/bash
#echo "Enter subnet then delete meeee" && exit 1

for ip in $(seq 1 254);do
  ping -c 1 192.168.0.$ip | grep from | cut -d" " -f4 | cut -d ":" -f1 &
done
