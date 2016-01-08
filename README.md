# timecat
强大的日志搜索辅助工具 - A powerful tool for search in log files.    
环境要求/requirements：Python    

<pre>
usage: timecat [-h] -s START [-e END] [-d DATE] [-r REGEX_FORMAT] [-v]
               [--color]
               file [file ...]

timecat command line tool uses binary search on seekable log files to directly
locate positions between start and end datetime, saving huge amounts of disk
I/Os, with high fault tolerance.Usage: timecat -s '2016-01-02 20:13:14' -e
'2016-01-02 20:14:13' LOGFILE1.log LOGFILE2.log ...

positional arguments:
  file                  files to be timecat.

optional arguments:
  -h, --help            show this help message and exit
  -s START, --start-datetime START
                        Which datetime to start(includsive). e.g. "-s
                        '2016-01-02 20:13:14'", "-s '2016/01/02 20:13:14'",
                        "-s '2016-01-02T12:13:14'", "-s
                        '2016-01-02T12:13:14.000'", "-s
                        '02/Jan/2016:20:13:14'", "-s '02-Jan-2016 20:13:14'",
                        "-s '02 Jan 2016 20:13:14'", "-s 'Jan 2 20:13:14'",
                        "-s '20160102201315'", "-s '1451736794'", "-s
                        '20:13'", etc. We will exhaust our effort to cover
                        regular datetime formats.
  -e END, --end-datetime END
                        Stop after reaching this datetime(excludsive). Same
                        format as "-s". If not set, means output till the end
                        of file.
  -d DATE, --date DATE  This is an optional argument. With "-d", the following
                        two statements are essentially the same: "timecat -s
                        '2016-01-02 20:13:14' -e '2016-01-02 20:14:13' ..."
                        and "timecat -d '2016-01-02' -s '20:13:14' -e
                        '20:14:13' ...".
  -r REGEX_FORMAT, --regex-format REGEX_FORMAT
                        If timecat failes to detect datetime format in your
                        log file, you can specify the regex pattern that can
                        find your datetime within each log line. e.g. I have
                        format "2016:01:01-20-13-14", and timecat does not
                        recognize this datetime format, then I can specify "-r
                        '\d{4}:\d{2}:\d{2}-\d{2}-\d{2}-\d{2}'".
  -v, --verbose         print additional information
  --color               Whether to enable colorized output
</pre>
