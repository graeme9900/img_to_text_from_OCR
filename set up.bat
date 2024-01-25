@echo off

powershell Start-Process cmd -Verb RunAs

set current_dir=%~dp0
mkdir "%current_dir%\save"