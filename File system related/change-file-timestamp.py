#!/usr/bin/env python3
# Problem:
# need to change modification time ( timestamp) on folders

# Usage:
#
# ref:
# Google: python 3 change file timestamp -> http://www.dreamincode.net/forums/topic/307923-change-timestamp-on-file-to-current-time/


# Author: AaronLaw
# Last Update: 2017-04-13
import os, time
from stat import *

# returns a list of all files on the current directory
os.chdir('.')
files = os.scandir('.')
print(files)

for f in files:
    print("Affected with timestamp: {} ".format(f) )
    if f.is_dir():
        st = os.stat(f)
        atime = st[ST_ATIME] #access time
        mtime = st[ST_MTIME] #modification time
		
        new_mtime = mtime+(4*3600)
		
        #modify the file timestamp
        os.utime(f, (atime, new_mtime))