#!/bin/bash
if [ $# -ne 2 ]; then 
  echo "USAGE: $0 <command> <file_of_IPs>"
  exit 1
fi

cmd="$1"
IPs=$(cat $2)

for ip in $IPs; do
  $cmd $ip > "data/autocmd/$cmd.$ip" &
done
