@echo off
color c
cls

Scripts\python -V
echo.

GOTO HELP

:UNINSTALL_MODULE
echo Enter module's name!
set /P module_name=module: 

if %module_name% == ex GOTO EXIT_MODULE_UNINSTALLER

if %module_name% == h GOTO HELP
if %module_name% == help GOTO HELP

Scripts\python -m pip uninstall %module_name%
pause

GOTO UNINSTALL_MODULE

:HELP
echo ScorpionIPX Python module uninstaller v 1.0
echo.
echo HELP MENU
echo commands set
echo h , help - Promts ScorpionIPX Python module uninstaller HELP MENU
echo ex - Quits ScorpionIPX Python module uninstaller
echo.
GOTO UNINSTALL_MODULE

:EXIT_MODULE_UNINSTALLER
echo.
echo Thank you for using ScorpionIPX Python module uninstaller v 1.0
pause