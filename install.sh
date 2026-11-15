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
clear && echo "\033[32mDone\033[0m! Welcome to Barkell preview. \033[34mv: 0.1.0\033[0m\ntype \033[33m'help'\033[0m to see available commands."
exec "$PY" ~/BarkellPreview/barkell.py
