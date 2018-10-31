@echo off
cd /d "%~f1"
dir *.netsim /b>filetext.txt
python Output_Script.py "%~f1"  "%~2"


