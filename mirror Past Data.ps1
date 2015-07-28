# C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe
# We have weekly full backup of Past Data though,
# I mirror Past Data to another drive for archive purpose
# Decide to run this script monthly

# Aaron Law
#2015-03-07


# /MIR - to mirror the source (excat copy of the source. Delete anything that is not exist in the source)
# /COPY:DATSUO - copy all meta-info
# /DCOPY:T - copy the timestamp of directory
robocopy "D:\Past Data\Audit" "Z:\Past Data\Audit" /MIR /COPY:DATSUO /DCOPY:T