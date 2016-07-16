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
import os, shutil, glob

source = "C:/Users/aaron.law/Sites/cheng-scripts/attandance_server"
dist = "C:/Users/aaron.law/Sites/cheng-scripts/attandance_server/result"
filetype = ("txt", "ps1")

# Reference:
# Stackoverflow.com: python move file ->  http://stackoverflow.com/questions/38061344/python-how-to-recursively-move-files-that-are-inside-folders
folder = os.scandir(source)
for files in folder:
    if files.name.endswith((filetype)):
        print("Moving {0}".format(files.name))
        shutil.move(os.path.join(source, files.name), os.path.join(dist, files.name))