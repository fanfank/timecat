#!/usr/bin/python
# -*- coding: utf-8 -*-

from include import *
from timecat import forward_match

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
    match, line, res_pos = forward_match(f, st, ed, regprog)
    print_match_result(match, line)

def do_readline(f, readline_num):
    while readline_num > 0:
        readline_num -= 1
        f.readline()

if __name__ == "__main__":
    testlog = "test.log"
    regprog = re.compile("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    #1 匹配 第4行
    with open(testlog, "r") as f:
        f.seek(-5, os.SEEK_END)
        ed = f.tell()
        f.seek(0)
        st = f.tell()
        do_match(f, st, ed, regprog)

    #2 匹配 第4行
    with open(testlog, "r") as f:
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        f.seek(0)
        do_readline(f, 3)
        st = f.tell()
        do_match(f, st, ed, regprog)

    #3 不匹配 空
    with open(testlog, "r") as f:
        do_readline(f, 3)
        ed = f.tell()
        st = f.tell()
        do_match(f, st, ed, regprog)
        
    #4 匹配 第4行，从字母N开始
    with open(testlog, "r") as f:
        do_readline(f, 3)
        f.read(1)
        st = f.tell()
        f.readline()
        ed = f.tell()
        f.seek(st)
        do_match(f, st, ed, regprog)

    #5 不匹配 第4行,从字母t开始
    with open(testlog, "r") as f:
        do_readline(f, 3)
        f.read(30)
        st = f.tell()
        f.readline()
        ed = f.tell()
        f.seek(st)
        do_match(f, st, ed, regprog)

    #6 不匹配 第38行
    with open(testlog, "r") as f:
        do_readline(f, 9)
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        f.seek(st)
        do_match(f, st, ed, regprog)
