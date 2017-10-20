@echo off
color b
cls

Scripts\python -V
echo.

GOTO HELP

:INSTALL_MODULE
echo Enter module's name!
set /P module_name=module: 

if %module_name% == ex GOTO EXIT_MODULE_INSTALLER

if %module_name% == h GOTO HELP
if %module_name% == help GOTO HELP

Scripts\python -m pip install %module_name%
pause

GOTO INSTALL_MODULE

:HELP
echo ScorpionIPX Python module installer v 1.0
echo.
echo HELP MENU
echo commands set
echo h , help - Promts ScorpionIPX Python module installer HELP MENU
echo ex - Quits ScorpionIPX Python module installer
echo.
GOTO INSTALL_MODULE

:EXIT_MODULE_INSTALLER
echo.
echo Thank you for using ScorpionIPX Python module installer v 1.0
pause