#! /bin/bash
# Print a multiplication table.

x=$1
y=$2

i=1
while [ $i -le $y ]
do
   echo "$i X $x = `expr $i \* $x`"
   i=`expr $i + 1`
done
