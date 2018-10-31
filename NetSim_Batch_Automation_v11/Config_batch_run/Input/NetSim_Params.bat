@echo off
SET DIR="%2"
SET NETSIM_PATH="%1"

CD %2

%1\NetSimCore.exe -apppath %1 -iopath  %2 -license 5053@192.168.0.192
exit
