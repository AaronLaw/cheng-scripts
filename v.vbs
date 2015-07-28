Set oShell = CreateObject("Shell.Application")
oShell.NameSpace("H:\").Self.Name = "Public"

Set oShell = CreateObject("Shell.Application")
oShell.NameSpace("X:\").Self.Name = "My Private Storage"

Set oShell = CreateObject("Shell.Application")
oShell.NameSpace("Z:\").Self.Name = "Share"

Set oShell = CreateObject("Shell.Application")
oShell.NameSpace("I:\").Self.Name = "Home"