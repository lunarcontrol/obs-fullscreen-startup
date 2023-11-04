@echo off

taskkill.exe /F -IM obs64.exe

c:
cd \Program Files\obs-studio\bin\64bit
start "OBSSTUDIO" "C:\Program Files\obs-studio\bin\64bit\obs64.exe"
