Set oShell = CreateObject("Shell.Application")
oShell.NameSpace("H:\").Self.Name = "Public"

Set oShell = CreateObject("Shell.Application")
oShell.NameSpace("I:\").Self.Name = "Home"

Set oShell = CreateObject("Shell.Application")
oShell.NameSpace("O:\").Self.Name = "Past Data"

Set oShell = CreateObject("Shell.Application")
oShell.NameSpace("M:\").Self.Name = "Past Data 2"


rem 2015-07-31:
rem no need to set the X: drive here, as it has already been mounted automatically, in AD
rem //
rem Set oShell = CreateObject("Shell.Application")
rem oShell.NameSpace("X:\").Self.Name = "My Network Storage"