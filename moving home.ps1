# C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe
# I move data from D:\ to F:\ for saving space puprose, as the D:\ is almost full

# Aaron Law
#2015-05-01


# /MIR - to mirror the source (excat copy of the source. Delete anything that is not exist in the source)
# /COPY:DATSUO - copy all meta-info
# /DCOPY:T - copy the timestamp of directory
robocopy "D:\HOME\" "F:\test\HOME\"  /mir /dcopy:t /copyall