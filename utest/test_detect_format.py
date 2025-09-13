#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

# Python 2/3 compatibility
try:
    xrange
except NameError:
    # Python 3
    xrange = range

from include import *
from timecat import detect_datetime_format

case_num = 0
def sorted_dict_repr(d):
    """返回字典的排序后的字符串表示，确保输出一致"""
    if d is None:
        return 'None'
    if isinstance(d, dict):
        items = sorted(d.items())
        return '{' + ', '.join("'{}': {}".format(k, repr(v)) for k, v in items) + '}'
    return repr(d)

def check(st, regex_format = None):
    global case_num
    case_num += 1
    print("case num:{}".format(case_num))
    regex_format_info = detect_datetime_format(st, regex_format)
    if regex_format_info:
        regex_format_info["parser"] = "parser obj" # always change, it's an obj
    print(sorted_dict_repr(regex_format_info))
    print("")

if __name__ == "__main__":
    # case 1~3
    check("2016-01-02 20:13:14.666")
    check("2016-01-02 20:13:14")
    check("2016-01-02 20:13")

    # case 4~6
    check("Jan  2 20:13:14") 
    check("Aug 12 20:13:14") 
    check("Oct 09 20:13:14") 

    # case 7~9
    check("2016-01-02T12:13:14.666")
    check("2016/01/02 20:13:14")
    check("2016-01-02 20:13:14")

    # case 10~12
    check("02/Oct/2016:20:13:14.666")
    check("02-Jan-2016 20:13:14")
    check("02 Feb 2016 20:13:14")

    # case 13~14
    check("17769394")
    check("20160102201315")

    # case 15
    check("1451736794666")

    # case 16
    check("1451736794")

    # case 17~18
    check("20:13:14")
    check("20013014")

    # case 19~21
    check("20:13")
    check("20013")
    check("13:14")
    check("13014")
