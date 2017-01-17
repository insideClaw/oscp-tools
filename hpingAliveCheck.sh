#!/bin/bash
for serv in `cat data/iis5_vuln`; do hping3 -S -c 1 -p 80 $serv 2>&1 | grep -o -E "ip=[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"; done
