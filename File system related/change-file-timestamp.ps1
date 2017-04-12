# C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe
# We are going to change modified time of files & folder on a windows system

# Requirement:
# Equivalent of touch on unix system

# Aaron Law
#2017-04-12

# Google: set file timestamp on windows   -> https://superuser.com/questions/292630/how-can-i-change-the-timestamp-on-a-file
# .CreationTime=
# .LastAccessTime=
# .LastWriteTime=
$(get-item filename).lastwritetime=$(get-date "2015-06-08 06:00am")

# Google: set file timestamp on windows   -> https://superuser.com/questions/292630/how-can-i-change-the-timestamp-on-a-file -> https://superuser.com/questions/10426/windows-equivalent-of-the-linux-command-touch
# a recursive version
Get-ChildItem . * -recurse | ForEach-Object{$_.LastWriteTime=$(get-date)}