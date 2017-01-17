#!/bin/bash
port=$1
# Run "script <file>" to capture terminal prior to executing this program. Killing ssh in two seconds is useful, hard to do from within.
for ip in `cat data/snooped_ping.txt`; do 
  ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no $ip & 
done
