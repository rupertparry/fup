#!/bin/bash
pyinstaller --onefile fup.py
cp -i dist/fup /usr/local/bin