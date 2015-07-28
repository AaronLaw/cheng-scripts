2015-03-20:
List rubbish files (temporary file) with a directory and its sub-directories:
# Thumbs.db, ~*.RTF, ~*.tmp, *.part, *.crdownload, *.lck, *.lock, *.temp
# Google: temp file types on Windows -> http://www.file-extensions.org/filetype/extension/name/temporary-files
#-force - force to show hiddle files
Get-ChildItem -recurse -force *.tmp, *.db, ~*

Remove rubbish files with a directory and its sub-directories:
# Thumbs.db, ~*.RTF, ~*.tmp
#-force - (in Get-ChildItem)force to show hiddle files
#-force - (in Remove-Item)force to delete file/folder whenever permission-denied
Get-ChildItem -recurse -force *.tmp, *.db, ~* | Remove-Item -force

2015-06-16:
Just because I got a "Long file name" error with the Powershell commandlet, I shall try another way to do so. [不是清走"我裡面的垃圾"，而是把"我裡面"的垃圾搬到出面]
As I know `robocopy` bypasses this error, I shall try:
Robocopy . "F:\test\rubbish" *.tmp *.db ~* /move /s
this command moves out the temp and rubbish files in the file structure

Before remove temp files in a directory, it is better that we make a backup copy of that files with same folder structure (And then we do the remove). Therefore, we use Robocopy to do it:
# Google: how to use robocopy to copy a certain type of files
Robocopy . "F:\test\" *.tmp,*.db,~* /S

Show all GPO in a domain:
Get-GPO -all