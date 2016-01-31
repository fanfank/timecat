#!/usr/bin/python
# -*- coding: utf-8 -*-

from include import *
from timecat import detect_file_format
from timecat import detect_datetime_format

case_num = 0
def dofo(f, start, end, regex_format_info):
    global case_num
    case_num += 1
    print("case {}".format(case_num))
    res = detect_file_format(f, start, end, regex_format_info)
    if res is not None:
        res = {
            "order": res["order"]
        }
    print(repr(res))
    print("")

if __name__ == "__main__":
    ascending_log = "testbinary.log"
    with open(ascending_log) as f:
        # 1. ascending
        regex_format_info = detect_datetime_format("02/Oct/2016:20:13:14.666", None)
        dofo(f, "02/Oct/2016:20:13:14.666", "02/Dec/2017:20:13:14.666", 
                regex_format_info)

    descending_log = "testbinary.log.reverse"
    with open(descending_log) as f:
        # 2. descending
        regex_format_info = detect_datetime_format("02/Oct/2016:20:13:14.666", None)
        dofo(f, "02/Oct/2016:20:13:14.666", "05/Aug/2016:20:13:14.666", 
                regex_format_info)

    ascending_log = "testbinary.log"
    with open(ascending_log) as f:
        regex_format_info = detect_datetime_format("2015-12-13 12:13:20", None)

        # 3. ascending
        dofo(f, "2015-12-13 12:13:20", None, regex_format_info)

        # 4. descending
        dofo(f, "2015-12-13 12:13:20", "2015-12-13 11:10:20", regex_format_info)

    descending_log = "testbinary.log.reverse"
    with open(descending_log) as f:
        regex_format_info = detect_datetime_format("2015-12-13 11:10:20", None)

        # 5. descending
        dofo(f, "2015-12-13 12:13:20", None, regex_format_info)

        # 6. ascending
        dofo(f, "2015-12-13 12:13:20", "2016-12-13 12:13:20", regex_format_info)
