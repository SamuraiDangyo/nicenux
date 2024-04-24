#!/bin/sh

# nicenux. Shows ASCII art Linux information. Written in Python3.
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

# Actions

echo "${FONT1}Installing ...${END}"

pip install py-cpuinfo
pip install psutil

chmod 555 nicenux.py
sudo cp nicenux.py /usr/bin

echo "${FONT2}... and done !${END}"
echo "${FONT3}> nicenux.py${END}"
