#!/usr/bin/python
# -*- coding: utf-8 -*-

from include import *
from timecat import detect_datetime_format
from timecat import dtcmp

case_num = 0
def docmp(lhs, rhs, regex_format_info, cmp_op):
    global case_num
    case_num += 1
    print("case {}:".format(case_num))
    print(repr(dtcmp(lhs, rhs, regex_format_info, cmp_op)))
    print("")

if __name__ == "__main__":
    regex_format_info = detect_datetime_format("Oct 09 20:13:14", None)
    # 1. False
    docmp("Oct 09 20:13:14", "Nov 08 19:12:13", regex_format_info, ">")
    # 2. True
    docmp("Oct 09 20:13:14", "Nov 08 19:12:13", regex_format_info, "<")
    # 3. False
    docmp("Oct 09 20:13:14", "Nov 08 19:12:13", regex_format_info, "=")
    # 4. False
    docmp("Oct 09 20:13:14", "Nov 08 19:12:13", regex_format_info, "==")
    # 5. True
    docmp("Oct 09 20:13:14", "Nov 08 19:12:13", regex_format_info, "!=")
    # 6. True
    docmp("Oct 09 20:13:14", "Nov 08 19:12:13", regex_format_info, "<=")
    # 7. False
    docmp("Oct 09 20:13:14", "Nov 08 19:12:13", regex_format_info, ">=")

    regex_format_info = detect_datetime_format("02/Oct/2016:20:13:14.666", None)
    # 8. True
    docmp("02/Oct/2016:20:13:14.666", "02/Sep/2016:20:13:14.666", regex_format_info, ">")
    # 9. True
    docmp("02/Oct/2016:20:13:14.666", "02/Oct/2016:20:13:14.666", regex_format_info, "=")
    # 10. True
    docmp("02/Oct/2016:20:13:14.666", "02/Oct/2016:20:13:14.666", regex_format_info, ">=")
    # 11. True
    docmp("02/Oct/2016:20:13:14.666", "02/Oct/2016:20:13:14.666", regex_format_info, "<=")
    # 12. True
    docmp("01/Oct/2016:20:13:14.666", "02/Oct/2016:20:13:14.666", regex_format_info, "<=")
    # 13. True
    docmp("09/Oct/2016:20:13:14.666", "01/Oct/2017:20:13:14.666", regex_format_info, "<=")
    # 14. False
    docmp("01/Oct/2017:20:13:14.666", "09/Oct/2016:20:13:14.666", regex_format_info, "<=")
    # 15. True
    docmp("09/Oct/2016:20:13:14.667", "09/Oct/2016:20:13:14.666", regex_format_info, ">")
