# -*- coding:utf8 -*-
"""
@author xuruiqi
@date   20151124
"""
from __future__ import division

# Python 2/3 compatibility
try:
    xrange
except NameError:
    # Python 3
    xrange = range

from datetime import datetime
import json
import logging
import os
from pprint import pprint as ppt 
import random
import re
import signal
import subprocess
import sys 
import time
#reload(sys)
#sys.setdefaultencoding('utf-8')
