#!/usr/bin/python
# -*- coding: utf-8 -*-

from include import *
from timecat import detect_file_order
from timecat import detect_format

case_num = 0
def dofo(f, start, end, regex_format_info):
    global case_num
    case_num += 1
    print("case {}".format(case_num))
    print(repr(detect_file_order(f, start, end, regex_format_info)))
    print("")

if __name__ == "__main__":
    # 1. ascending
    regex_format_info = detect_format("02/Oct/2016:20:13:14.666", None, None)
    dofo(None, "02/Oct/2016:20:13:14.666", "02/Dec/2017:20:13:14.666", 
            regex_format_info)

    # 2. descending
    regex_format_info = detect_format("02/Oct/2016:20:13:14.666", None, None)
    dofo(None, "02/Oct/2016:20:13:14.666", "05/Aug/2016:20:13:14.666", 
            regex_format_info)

    ascending_log = "testbinary.log"
    with open(ascending_log) as f:
        regex_format_info = detect_format("2015-12-13 12:13:20", None, None)

        # 3. ascending
        dofo(f, "2015-12-13 12:13:20", None, regex_format_info)

        # 4. descending
        dofo(f, "2015-12-13 12:13:20", "2015-12-13 11:10:20", regex_format_info)

    descending_log = "testbinary.log.reverse"
    with open(descending_log) as f:
        regex_format_info = detect_format("2015-12-13 11:10:20", None, None)

        # 5. descending
        dofo(f, "2015-12-13 12:13:20", None, regex_format_info)

        # 6. ascending
        dofo(f, "2015-12-13 12:13:20", "2016-12-13 12:13:20", regex_format_info)
