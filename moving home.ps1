# C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe
# We have weekly full backup of Past Data though,
# I move data from D:\ to F:\ for saving space puprose, as the D:\ is almost full
# Decide to run this script when need

# Requirement:
# Mirror the exact directory tree (with data) with security info (ACL),
# while do not copy the rubbish data (~$, tmp, thumb.db)
# and when there was an invalid file, the program skips it/restart again, and run the copy process continues

# Aaron Law
#2015-05-01


# /MIR - to mirror the source (excat copy of the source. Delete anything that is not exist in the source)
# /COPY:DATSUO - copy all meta-info
# /DCOPY:T - copy the timestamp of directory
robocopy "D:\HOME\" "F:\test\HOME\"  /mir /dcopy:t /copyall /XF ~$* tmp* thumb* /ZB