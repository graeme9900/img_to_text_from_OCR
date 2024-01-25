@echo off


:: 將 cmd 最小化執行
if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dpnx0"
goto :EOF
:minimized

::用系統管理員執行
@REM runas /user:administrator "%~dp0run.bat"


:: 建立捷徑
@REM mklink "%~dp0run_link.bat" "%~dp0run.bat"
@REM echo %~dp0

:: 建立 save 資料夾
set current_dir=%~dp0
mkdir "%current_dir%\save"

cd %current_dir%

python img_to_text.py