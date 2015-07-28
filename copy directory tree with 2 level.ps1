# C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe
# Copy directory tree structure with security info (ACL), in TOP 2 level

# Requirement:
# Mirror the exact directory tree (with data) with security info (ACL),
# while only need empty directory tree structure (do not copy any files)
# and strict it with the TOP 2 level

# Aaron Law
# 2015-05-06

# /lev:n - top n level
# /create - copy data in 0-byte manner
# /XF - exclude files in pattern manner

robocopy "D:\PUBLIC\FILES\2_AUDIT DEPT\Yr 2015\Listed" "D:\PUBLIC\Listed-beyond-lock" /copyall /e /lev:2 /create
