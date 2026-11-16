#!/bin/sh
set -e

if command -v python3 >/dev/null 2>&1; then
    PY=python3
elif command -v python >/dev/null 2>&1; then
    PY=python
else
    if command -v apt-get >/dev/null 2>&1; then
        INSTALL="sudo apt-get install -y"
    elif command -v dnf >/dev/null 2>&1; then
        INSTALL="sudo dnf install -y"
    elif command -v pacman >/dev/null 2>&1; then
        INSTALL="sudo pacman -S --noconfirm"
    elif command -v apk >/dev/null 2>&1; then
        INSTALL="sudo apk add"
    elif command -v brew >/dev/null 2>&1; then
        INSTALL="brew install"
    else
        echo "Error: no package manager found" >&2
        exit 1
    fi

    $INSTALL python
    PY=python
fi
ABSPATH=$(cd "$(dirname "$0")" && pwd)
clear && printf '\033[32mDone\033[0m! Welcome to Barkell preview. \033[34mv: 0.1.0\033[0m\ntype \033[33m"help"\033[0m to see available commands. Type \033[32m"barkell"\033[0m in your terminal to start the shell everytime. \033[33mNote\033[0m: Customize your shell typing \033[32m"setcolors"\033[0m, \033[34m"settings"\033[0m or \033[35m"setmode"\033[0m\n.'
exec "$PY" "$ABSPATH/barkell.py"
