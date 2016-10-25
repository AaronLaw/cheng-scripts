rem this script is stored in a GPO named 'Domain Policy', and then later be linked to cheng.local/
net use h: \\cc-server01\public
net use i: \\cc-server01\home
rem net use o: \\cc-server01\past_data$
net use o: \\cc-server01\past_data_2$
net use /delete z:

v.vbs


rem set default printer to Global Printer
RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "\\CCPRINT02\GlobalPrinter"