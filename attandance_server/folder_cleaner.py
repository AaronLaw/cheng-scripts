#!/usr/bin/env python3
# Problem: 
# The 701 Server program generates 2 new files every day, and so the "701 Server folder" becomes full a year later.
#
# Requirement:
# This script intend to clean up "the 701 server folder" by moving some old data (non-current *.msg & *.dut) to another folder.
#
# Usage:
# Install Python 3 and put this script into scheduler.
#
# Author: AaronLaw
# Last Update: 2017-07-17
import os, shutil, glob, datetime

source = "C:/Users/aaron.law/Sites/cheng-scripts/attandance_server"
dist = "C:/Users/aaron.law/Sites/cheng-scripts/attandance_server/result"
filetype = ("txt", "ps1")
day_keep = datetime.timedelta(days=7) # days of files that should be kept (not be moved)
# ref: Stackoverflow.com: python datetime -> http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
# ref: Stackoverflow.com: python datetime -> http://stackoverflow.com/questions/5476065/truncate-python-datetime -> https://docs.python.org/3/library/datetime.html#module-datetime
# ref: Stackoverflow.com: python datetime timedelta -> http://stackoverflow.com/questions/20631855/get-the-difference-between-two-datetime-objects-in-minutes-in-python
curr_date = datetime.date.today().isoformat()


# ref: Stackoverflow.com: python move file ->  http://stackoverflow.com/questions/38061344/python-how-to-recursively-move-files-that-are-inside-folders
folder = os.scandir(source) # return a list of DirEntry object
for files in folder:
    if files.name.endswith(filetype):
        mtime = os.stat(files.name).st_mtime # return a timestamp in float
        mtime_in_date = datetime.date.fromtimestamp(mtime) # making a date object from float
        print("Moving {0}, with modified date {1}".format(files.name, mtime_in_date))
        print(day_keep)
        #shutil.move(os.path.join(source, files.name), os.path.join(dist, files.name))