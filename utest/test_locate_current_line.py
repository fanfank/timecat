#!/usr/bin/python
# -*- coding: utf-8 -*-

from include import *
from timecat import locate_current_line

dataset_index = 0
def judge(f, st, ed):
    global dataset_index
    dataset_index += 1
    print("\ndataset[{}]".format(dataset_index))
    #locate_current_line(f, ed, st)
    locate_current_line(f, ed, st, 2)
    print(f.readline())

def do_readline(f, readline_num):
    while readline_num > 0:
        readline_num -= 1
        f.readline()

if __name__ == "__main__":
    testlog = "test.log"
    with open(testlog, "r") as f:
        #1 打印空行
        f.seek(0)
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        judge(f, st, ed)

        #2 打印最后1行
        f.seek(0)
        st = f.tell()
        f.seek(-5, os.SEEK_END)
        ed = f.tell()
        judge(f, st, ed)

        #3 打印第4行，从第4个字符开始打印
        f.seek(0)
        do_readline(f, 3)
        f.read(3)
        st = f.tell()
        f.readline()
        f.seek(-5, os.SEEK_CUR)
        ed = f.tell()
        judge(f, st, ed)

        #4 打印第2行
        f.seek(30)
        st = f.tell()
        f.readline()
        ed = f.tell()
        judge(f, st, ed)
