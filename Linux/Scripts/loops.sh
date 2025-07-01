#!/bin/bash

for color in red blue green
do
    echo "Color is $color"
done

for i in {1..5}
do
    echo "$i"
done

for ((i=1;i<=5;i++))
do
    echo "$i"
done

for file in *.txt
do
    echo "$file"
done