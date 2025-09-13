"""timecat pip setup file
@author xuruiqi(fanfank@github.com)
@site   https://github.com/fanfank/timecat
@date   20160108
"""

from codecs import open
from os import path
from setuptools import setup, find_packages

CUR_DIR = path.abspath(path.dirname(__file__))

#with open(path.join(CUR_DIR, "README.rst"), encoding = "utf-8") as f:
#    long_description = f.read()
long_description = \
        "Usage: timecat -s '2016-01-02 20:13:14' -e '2016-01-02 20:14:13', " \
        "or: timecat -d '2016-01-02' -s '20:13:14' -e '20:14:13'. timecat " \
        "output contents within the specified [start, end) range, saving " \
        "huge amounts of disk I/Os. " \
        "Timecat supports popular datetime formats say syslog, apache, " \
        "nginx, timestamp, etc."

setup(
    name         = "timecat",        
    version      = "2.1.0",
    description  = "a powerful tool for searching log files " \
            "with binary search algorithm",
    long_description = long_description,
    url          = "https://github.com/fanfank/timecat",
    author       = "xuruiqi",
    author_email = "reetsee.xu@gmail.com",
    license      = "MIT",
    classifiers  = [
        "Development Status :: 5 - Production/Stable",

        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",

        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",

        "Topic :: Utilities",
        "Topic :: System :: Systems Administration",
        "Topic :: Text Processing :: Filters",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],

    scripts = ["timecat"],

    keywords = "log binary search tool",

    packages = [],

    install_requires = [],

    extras_require = {},

    data_files = [],

    entry_points = {}
)
