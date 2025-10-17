#!/bin/bash

rm -rfv build
rm -rfv dist

pyinstaller Arcanum.spec

# Create spec file:
# pyinstaller --windowed --icon assets/app-icon.icns --name Arcanum src/main.py

cd dist
open .
