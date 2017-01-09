REM this script is stored in a GPO named 'Domain Policy', and then later be linked to cheng.local/
REM 2017-01-09: This script is no longer in use. We set drive mapping in 'Domain Policy -> User Configuration -> Preferences -> Windows Settings -> Drive Maps' in GPO instead.
net use h: \\cc-server01\public
net use i: \\cc-server01\home
net use /delete o:
net use o: \\cc-server01\past_data_2$
net use /delete z:

v.vbs


REM set default printer to Global Printer
REM RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "\\CCPRINT02\GlobalPrinter"
