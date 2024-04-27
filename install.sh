#!/bin/sh

# nicenux. Prints nice ASCII art Linux information. Written in Python3.
# Copyright (C) 2024 Toni Helminen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Constants

FONT1="\033[1;34;48m"
FONT2="\033[1;35;48m"
FONT3="\033[2;37;48m"
END="\033[0m"
BIN="/usr/bin"

# Actions

echo "${FONT1}Installing nicenux ...${END}"
echo ""

pip install py-cpuinfo
pip install psutil

sudo cp nicenux.py $BIN
sudo chmod 555 $BIN/nicenux.py

echo ""
echo "${FONT2}... And done !${END}"
echo ""
echo "${FONT1}To use nicenux, just type:${END}"
echo ""
echo "${FONT3}> nicenux.py${END}"
