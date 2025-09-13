#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

# Python 2/3 compatibility
try:
    xrange
except NameError:
    # Python 3
    xrange = range
# -*- coding: utf-8 -*-

from include import *
from timecat import at_line_head

dataset_index = 0
def judge(f):
    global dataset_index
    dataset_index += 1
    print("\ndataset[{}]".format(dataset_index))
    print(repr(at_line_head(f)))

if __name__ == "__main__":
    testlog = "test.log"

    with open(testlog, "r") as f:
        #1 返回true
        judge(f)

        #2 返回false
        f.read(3)
        judge(f)

        #3 返回true
        f.readline()
        judge(f)

        #4 返回true
        f.seek(0, os.SEEK_END)
        judge(f)
        
        #5 返回true
        f.seek(500)
        f.readline()
        line = f.readline()
        f.seek(f.tell() - len(line))
        judge(f)
