@echo off
SET  NETSIM_PATH="C:\\Program Files\\NetSim Standard\\bin"
FOR /d /r %%i IN (*) DO (
   pushd "%%i"
   call Identify_Config.bat  "%%~i" %NETSIM_PATH%
   popd
)

pause