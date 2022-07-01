#!/bin/bash  

let a=879
echo -n "The value of \"a\" is now: "
echo $a

let a=a+15
echo "The value of \"a\" is now: $a"

echo -n "The values of \"a\" in the loop are: "
for a in 7 8 9 11
do  
    if test $a -eq 11
    then   
        echo "$a END"
        break
    elif test $a -lt 8
    then
        echo "BEGIN $a, "
    else
        echo -n "$a, "
    fi
done
