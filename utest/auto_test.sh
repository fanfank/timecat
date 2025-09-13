#!/bin/bash

find . -name '*.py' | while read i
do
    name="${i:2}"
    name="${name%.py}"
    ans_name="$name".ans
    if [ -f $ans_name ]; then
        echo "----- Job: $name -----"
        python $i > ./.utest.tmp.out
        diff ./.utest.tmp.out ./$ans_name
        rm -f ./.utest.tmp.out
    fi
done
