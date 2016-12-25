#!/usr/bin/env python3
# Problem: 
# The 701 Server program generates 2 new files every day, and so the "701 Server folder" becomes full a year later.
#
# Requirement:
# This script intend to clean up "the 701 server folder" by moving some old data (non-current *.msg & *.dut) to an archive folder.
#    1. The day/time calculated is not required to be accuracy.
#    2. The files of the current day must becomes kept in the  currect dorectory. 
#
# Usage:
# Install Python 3 and put this script into scheduler.
#
# Author: AaronLaw
# Last Update: 2016-12-24
import os, shutil, glob, datetime

source = "C:/Users/aaron.law/Sites/test_data"
dist = "C:/Users/aaron.law/Sites/test_data/result"
filetype = ("txt", "ps1")
day_keep = datetime.timedelta(days=2) # days of files that should be kept (not to be moved)
# ref: Stackoverflow.com: python datetime -> http://stackoverflow.com/questions/5476065/truncate-python-datetime -> https://docs.python.org/3/library/datetime.html#module-datetime
# ref: Stackoverflow.com: python datetime timedelta -> http://stackoverflow.com/questions/20631855/get-the-difference-between-two-datetime-objects-in-minutes-in-python

curr_date = datetime.date.today() # ref: Stackoverflow.com: python datetime -> http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python

# MOVE files if match file extension AND m_date < a certain date
# ref: Stackoverflow.com: python move file ->  http://stackoverflow.com/questions/38061344/python-how-to-recursively-move-files-that-are-inside-folders
files = os.scandir(source) # return a list of DirEntry object
os.chdir(source) # FIX: the files cannot be moved if they are not in the same directory with this script. Need to change cwd for shutil functions.
errors = []
for file in files:
    m_time = os.stat(file.name).st_mtime # return a timestamp in float
    m_date = datetime.date.fromtimestamp(m_time) # making a date object from float
 
    if file.name.endswith(filetype) and (m_date < (curr_date - day_keep)):
        print("Moving {0}, with modified date {1}".format(file.name, m_date))
        try:
            print("Jointed source: " + os.path.join(source, file.name))
            print("Jointed dist  : " + os.path.join(dist, file.name))
            shutil.move(os.path.join(source, file.name), os.path.join(dist, file.name))
        except Exception as why: # mostly shutil.move() throw an exception when the folder of dist does not exist
            errors.append(str(why))
            os.makedirs(dist) # create a leaf directory and all intermediate one (recursive) if the dist does not exist. ref: https://docs.python.org/3/library/shutil.html#shutil.copy2 -> 11.10.1.1. copytree example

if errors:
    print(errors)