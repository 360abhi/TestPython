#!/bin/bash

count=5
while [ $count -gt 0 ]
do 
    echo "$count"
    ((count--))
done

while read line
do 
    echo "line : $line"
done < myfile.txt