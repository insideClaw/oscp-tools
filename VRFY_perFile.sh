#!/bin/bash
file=$1

for user in $(cat $file)
do
	echo VRFY $user | nc -nv -w 1 192.168.35.55 25 2>/dev/null | grep ^"252"
done
