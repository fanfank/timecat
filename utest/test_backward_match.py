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
from timecat import backward_match

def print_match_result(match, line):
    if not match:
        print("no match")
    else:
        print("match:[{}]".format(match.group(0)))
    print("last line:[{}]".format(line))

dataset_index = 0
def do_match(f, st, ed, regprog):
    global dataset_index
    dataset_index += 1
    print("\ndataset[{}]".format(dataset_index))
    print("st={}, ed={}".format(st, ed))
    #match, line = backward_match(f, ed, st, regprog)
    match, line, res_pos = backward_match(f, ed, st, regprog, 2)
    print_match_result(match, line)

def do_readline(f, readline_num):
    while readline_num > 0:
        readline_num -= 1
        f.readline()

if __name__ == "__main__":
    testlog = "test.log"
    regprog = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    #1 返回第8行
    with open(testlog, "r") as f:
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        do_match(f, st, ed, regprog)

    #2 返回空
    with open(testlog, "r") as f:
        do_readline(f, 3)
        ed = f.tell()
        st = f.tell()
        do_match(f, st, ed, regprog)

    #3 返回第7行
    with open(testlog, "r") as f: 
        do_readline(f, 3)
        st = f.tell()
        do_readline(f, 4)
        ed = f.tell()
        do_match(f, st, ed, regprog)

    #4 返回第8行,从字母O开始
    with open(testlog, "r") as f:
        do_readline(f, 7)
        f.read(3)
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        do_match(f, st, ed, regprog)

    #5 返回空
    with open(testlog, "r") as f:
        do_readline(f, 7)
        f.read(30)
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        do_match(f, st, ed, regprog)

    #6 返回第4行
    with open(testlog, "r") as f:
        do_readline(f, 3)
        st = f.tell()
        do_readline(f, 1)
        ed = f.tell()
        do_match(f, st, ed, regprog)

    #7 返回空
    with open(testlog, "r") as f:
        do_readline(f, 3)
        f.read(30)
        st = f.tell()
        do_readline(f, 1)
        ed = f.tell()
        do_match(f, st, ed, regprog)

    #8 返回第8行
    with open(testlog, "r") as f:
        do_readline(f, 7)
        st = f.tell()
        do_readline(f, 1)
        f.read(30)
        ed = f.tell()
        do_match(f, st, ed, regprog)

    #9 返回空
    with open(testlog, "r") as f:
        do_readline(f, 7)
        f.read(30)
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        do_match(f, st, ed, regprog)
