#!/usr/bin/python
# -*- coding: utf-8 -*-

from include import *
from timecat import locate_next_line

dataset_index = 0
def judge(f, st, ed):
    global dataset_index
    dataset_index += 1
    print("\ndataset[{}]".format(dataset_index))
    locate_next_line(f, st, ed)
    print(f.readline())
    
if __name__ == "__main__":
    testlog = "test.log"
    with open(testlog, "r") as f:
        #1 打印第1行
        f.seek(0)
        st = f.tell()
        f.seek(0, os.SEEK_END) 
        ed = f.tell()
        judge(f, st, ed)

        #2 打印第2行
        f.seek(0)
        f.read(5)
        st = f.tell()
        f.seek(0, os.SEEK_END) 
        ed = f.tell()
        judge(f, st, ed)

        #3 打印第一行最后3个字符
        f.seek(0)
        f.read(5)
        st = f.tell()
        f.readline()
        f.seek(-3, os.SEEK_CUR)
        ed = f.tell()
        judge(f, st, ed)

        #4 打印最后一行的倒数5个字符，eof
        f.seek(-5, os.SEEK_END)
        st = f.tell()
        ed = f.tell()
        judge(f, st, ed)
    
