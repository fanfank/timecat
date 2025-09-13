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
from timecat import binary_seek_pos
from timecat import detect_datetime_format
from timecat import detect_file_format

dataset_index = 0
def do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern):
    global dataset_index
    dataset_index += 1

    regex_format_info = detect_datetime_format(cmp_pattern, None)
    file_order_info   = detect_file_format(f, cmp_pattern, None, 
            regex_format_info)

    print("\ndataset[{}]".format(dataset_index))
    print("st={}, ed={}".format(st, ed))
    pos = binary_seek_pos(f, st, ed, cmp_pattern, regex_format_info, 
            file_order_info)
    if pos is None:
        print("binary search return None")
    else:
        print("pos=%d" % pos)
        f.seek(pos)
        print(f.readline())
    
def do_readline(f, readline_num):
    while readline_num > 0:
        readline_num -= 1
        f.readline()

if __name__ == "__main__":
    testbinarylog = "testbinary.log"
    regex_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

    with open(testbinarylog, "r") as f:

        # st合法，ed合法，中间包含/不包含非法字段
        #1 打印第3行
        cmp_pattern = "2015-12-13 13:13:20"
        f.seek(0)
        do_readline(f, 2)
        st = f.tell()
        do_readline(f, 4)
        f.read(30)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #2 打印第3行
        cmp_pattern = "2015-12-13 13:13:20"
        f.seek(0)
        do_readline(f, 1)
        f.read(3)
        st = f.tell()
        do_readline(f, 6)
        f.read(30)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #3 打印第1行
        cmp_pattern = "2015-12-13 12:13:20"
        f.seek(0)
        st = f.tell()
        do_readline(f, 2)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #4 打印第3行
        cmp_pattern = "2015-12-13 13:13:20"
        f.seek(0)
        st = f.tell()
        do_readline(f, 2)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)
        
        #5 打印第8行
        cmp_pattern = "2015-12-13 13:14:20"
        f.seek(0)
        do_readline(f, 6)
        st = f.tell()
        do_readline(f, 2)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        # st合法，ed非法，中间包含/不包含非法字段
        #6 打印第3行
        cmp_pattern = "2015-12-13 13:13:20"
        f.seek(0)
        st = f.tell()
        do_readline(f, 4)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #7 打印第3行
        cmp_pattern = "2015-12-13 13:13:20"
        f.seek(0)
        st = f.tell()
        do_readline(f, 28)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #8 打印第12行
        cmp_pattern = "2015-12-13 15:13:29"
        f.seek(0)
        st = f.tell()
        do_readline(f, 28)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        # st非法，ed合法，中间包含/不包含非法字段
        #9 打印第7行
        cmp_pattern = "2015-12-13 13:12:00"
        f.seek(0)
        do_readline(f, 4)
        f.read(30)
        st = f.tell()
        do_readline(f, 38)
        f.read(28)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #10 打印第10行
        cmp_pattern = "2015-12-13 14:30:00"
        f.seek(0)
        do_readline(f, 4)
        st = f.tell()
        do_readline(f, 38)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #11 打印第12行
        cmp_pattern = "2015-12-13 15:13:30"
        f.seek(0)
        do_readline(f, 4)
        st = f.tell()
        do_readline(f, 38)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #12 打印最后一行(43行)
        cmp_pattern = "2015-12-13 15:13:30"
        f.seek(0)
        do_readline(f, 12)
        st = f.tell()
        do_readline(f, 30)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        # st非法，ed合法，中间包含/不包含非法字段
        #13 返回None
        cmp_pattern = "2015-12-13 00:13:30"
        f.seek(0)
        do_readline(f, 14)
        st = f.tell()
        do_readline(f, 10)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #14 打印第7行
        cmp_pattern = "2015-12-13 13:13:20"
        f.seek(0)
        do_readline(f, 3)
        st = f.tell()
        do_readline(f, 15)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #15 打印第12行
        cmp_pattern = "2015-12-13 15:14:00"
        f.seek(0)
        do_readline(f, 3)
        st = f.tell()
        do_readline(f, 15)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #16 打印第10行
        cmp_pattern = "2015-12-13 15:13:00"
        f.seek(0)
        do_readline(f, 3)
        st = f.tell()
        do_readline(f, 15)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        # 边缘case，分别测指定pattern不在范围内的输入
        #17 打印第1行
        cmp_pattern = "2015-12-12 15:13:00"
        f.seek(0)
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #18 返回None或打印空行
        cmp_pattern = "2015-12-14 15:13:00"
        f.seek(0)
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #19 返回None或打印空行
        cmp_pattern = "2015-12-13 15:13:00"
        f.seek(0)
        do_readline(f, 20)
        st = f.tell()
        do_readline(f, 10)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)
