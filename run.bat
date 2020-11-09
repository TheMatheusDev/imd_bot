@echo off
setlocal enabledelayedexpansion

if not exist python\python.exe (
	echo Python portavel nao foi encontrado; nos iremos baixar e instalar para voce.
	PowerShell -ExecutionPolicy Unrestricted -File "downloadpython.ps1"
)

title IMD BOT
mode con:cols=50 lines=30
python\python.exe BOT.py
