#!/bin/bash
if [ $# -eq 0 ]
then
  file="data/http_servers_cleaned"
  echo "Default filepath $file assumed."
else
  file=$!
fi

#for item in `grep report $file | cut -d ' ' -f5`
for item in `cat $file`
do 
  echo "Opening $item"
  firefox --new-tab $item  
done
