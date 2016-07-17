#!/usr/bin/env python3
# Problem: 
# The 701 Server program generates 2 new files every day, and so the "701 Server folder" becomes full a year later.
#
# Requirement:
# This script intend to clean up "the 701 server folder" by moving some old data (non-current *.msg & *.dut) to another folder.
#    1. The day/time calculated is not required to be accuracy.
#    2. The current day's file must not be moved around. 
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
day_keep = datetime.timedelta(days=2) # days of files that should be kept (not to be moved)
# ref: Stackoverflow.com: python datetime -> http://stackoverflow.com/questions/5476065/truncate-python-datetime -> https://docs.python.org/3/library/datetime.html#module-datetime
# ref: Stackoverflow.com: python datetime timedelta -> http://stackoverflow.com/questions/20631855/get-the-difference-between-two-datetime-objects-in-minutes-in-python

curr_date = datetime.date.today() # ref: Stackoverflow.com: python datetime -> http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python

# MOVE files if match file extension AND m_date < a certain date
# ref: Stackoverflow.com: python move file ->  http://stackoverflow.com/questions/38061344/python-how-to-recursively-move-files-that-are-inside-folders
folder = os.scandir(source) # return a list of DirEntry object
for files in folder:
    m_time = os.stat(files.name).st_mtime # return a timestamp in float
    m_date = datetime.date.fromtimestamp(m_time) # making a date object from float
 
    if files.name.endswith(filetype) and (m_date < (curr_date - day_keep)):
        print("Moving {0}, with modified date {1}".format(files.name, m_date))
        try:
            shutil.move(os.path.join(source, files.name), os.path.join(dist, files.name))
        except Exception as why:
            print(why)
            os.makedirs(dist) # create a leaf directory and all intermediate one (recursive) if the dist does not exist
