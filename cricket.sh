#!/bin/bash

echo "Enter refresh time > 0:"
read time
until [[ $time -gt 0 && $((time)) == $time ]]
do 
	echo "Enter valid time > 0:"
	read time
done

echo "Enter the URL from cricbuzz website:"
read url
while [[ -z "${url// }" ]]
do 
	echo "Empty input not expected..."
	echo "Try again..."
	read url
done
watch -n $time python3 cricbuzz.py $url
