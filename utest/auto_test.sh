#!/bin/bash
PY_FILES=`find . -name '*.py'`

for i in ${PY_FILES[@]}
do
    name=${i:2:-3}
    ans_name="$name".ans
    if [ -f $ans_name ]; then
        echo "----- Job: $name -----"
        python $i > ./.utest.tmp.out
        diff ./.utest.tmp.out ./$ans_name
        rm -f ./.utest.tmp.out
    fi
done
