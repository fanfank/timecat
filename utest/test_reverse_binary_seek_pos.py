#!/usr/bin/python
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
    testbinarylog = "testbinary.log.reverse"
    regex_pattern = "\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

    with open(testbinarylog, "r") as f:

        # st合法，ed合法，中间包含/不包含非法字段
        #1 打印第33行
        cmp_pattern = "2015-12-13 15:13:20"
        f.seek(0)
        do_readline(f, 31)
        st = f.tell()
        do_readline(f, 3)
        f.read(30)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #2 打印第32行
        cmp_pattern = "2015-12-13 15:14:20"
        f.seek(0)
        do_readline(f, 31)
        f.read(3)
        st = f.tell()
        do_readline(f, 1)
        f.read(30)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #3 打印第33行
        cmp_pattern = "2015-12-13 15:13:20"
        f.seek(0)
        do_readline(f, 31)
        st = f.tell()
        do_readline(f, 2)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #4 打印第42行
        cmp_pattern = "2015-12-13 13:13:10"
        f.seek(0)
        do_readline(f, 40)
        st = f.tell()
        do_readline(f, 2)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)
        
        #5 打印第35行
        cmp_pattern = "2015-12-13 14:13:20"
        f.seek(0)
        do_readline(f, 34)
        st = f.tell()
        do_readline(f, 1)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        # st合法，ed非法，中间包含/不包含非法字段
        #6 打印第1行
        cmp_pattern = "2015-12-13 16:13:20"
        f.seek(0)
        st = f.tell()
        do_readline(f, 4)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #7 打印空或31行
        cmp_pattern = "2015-12-13 15:14:21"
        f.seek(0)
        st = f.tell()
        do_readline(f, 30)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #8 打印第33行
        cmp_pattern = "2015-12-13 15:13:20"
        f.seek(0)
        st = f.tell()
        do_readline(f, 38)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        # st非法，ed合法，中间包含/不包含非法字段
        #9 打印第35行
        cmp_pattern = "2015-12-13 14:13:20"
        f.seek(0)
        do_readline(f, 14)
        f.read(30)
        st = f.tell()
        do_readline(f, 20)
        f.read(28)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #10 打印第35行
        cmp_pattern = "2015-12-13 14:30:00"
        f.seek(0)
        do_readline(f, 14)
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #11 打印第42行
        cmp_pattern = "2015-12-13 12:13:20"
        f.seek(0)
        do_readline(f, 38)
        st = f.tell()
        do_readline(f, 3)
        f.read(30)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #12 打印最后一行(32行)
        cmp_pattern = "2015-12-13 15:14:21"
        f.seek(0)
        do_readline(f, 12)
        st = f.tell()
        do_readline(f, 20)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        # st非法，ed非法，中间包含/不包含非法字段
        #13 返回None
        cmp_pattern = "2015-12-13 00:13:30"
        f.seek(0)
        do_readline(f, 14)
        st = f.tell()
        do_readline(f, 10)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #14 打印第33行
        cmp_pattern = "2015-12-13 15:13:20"
        f.seek(0)
        do_readline(f, 5)
        st = f.tell()
        do_readline(f, 34)
        f.read(3)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #15 打印None或39行
        cmp_pattern = "2015-12-13 12:13:20"
        f.seek(0)
        do_readline(f, 10)
        st = f.tell()
        do_readline(f, 28)
        f.read(10)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #16 打印32行
        cmp_pattern = "2015-12-13 15:14:20"
        f.seek(0)
        do_readline(f, 1)
        st = f.tell()
        do_readline(f, 30)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        # 边缘case，分别测指定pattern不在范围内的输入
        #17 打印第1行
        cmp_pattern = "2015-12-14 15:13:00"
        f.seek(0)
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #18 返回None或打印EOF
        cmp_pattern = "2015-12-12 15:13:00"
        f.seek(0)
        st = f.tell()
        f.seek(0, os.SEEK_END)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)

        #19 打印33行
        cmp_pattern = "2015-12-13 15:13:20"
        f.seek(0)
        do_readline(f, 32)
        st = f.tell()
        do_readline(f, 2)
        ed = f.tell()
        do_binary_seek_pos(f, st, ed, cmp_pattern, regex_pattern)
