#!/usr/bin/env python

import datetime
import sys
import argparse


def parseArgs():
    parser = argparse.ArgumentParser(
        description="This is a tool to handle varous data strings into unix time and to compare data strings. If one date is given then output is its unix seconds. If two dates are given then the result is {-1,0,1} depending on d1>d2 resolution. Warning: it is awfully slow. Warning: it seems like '%m 2 3' breaks the system already. Nobody's perfect!")
    parser.add_argument(
        "format", help="format of the first date. According to datetime.datetime.strptime method documentation")
    parser.add_argument("date1", help="the first date to be parsed")
    parser.add_argument(
        "date2", help="the second date to be parsed", nargs="?")
    parser.add_argument("format2", help="format of the second date", nargs="?")
    parser.add_argument(
        "-v", "--verbose", help="show debug. Will break scripts", action="store_true")
    return parser.parse_args()


arrrgs = parseArgs()
if arrrgs.verbose:
    print("Arguments are: ", arrrgs)

form = arrrgs.format
first = arrrgs.date1
second = arrrgs.date2
sform = arrrgs.format2

try:
    ftime = datetime.datetime.strptime(first, form)
except ValueError:
    print("Bad first format I guess")
    sys.exit(2)

if not second:
    print(ftime.strftime("%s"))
    sys.exit(0)

if not sform:
    sform = form

try:
    stime = datetime.datetime.strptime(second, sform)
except ValueError:
    print("Bad second format I guess")
    sys.exit(2)

fsecs = ftime.strftime("%s")
ssecs = stime.strftime("%s")


if arrrgs.verbose:
    print(form, '\t', sform)
    print(ftime, '\t', stime)
    print(fsecs, '\t', ssecs)

# Code will bug without this conversion:
# ( like /timecomp.py "%Y-%m-%d_%H-%M-%S" 1970-01-01_03-00-05 1970-01-01_03-04-05 )
fsecs = int(fsecs)
ssecs = int(ssecs)

if fsecs < ssecs:
    res = -1
elif fsecs > ssecs:
    res = 1
elif fsecs == ssecs:
    res = 0

print(res)
sys.exit(0)
