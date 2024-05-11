#!/usr/bin/env python3

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

# Libraries

import psutil
import subprocess
import cpuinfo
import re
import sys
import multiprocessing

# Constants

VERSION = "nicenux 1.3"

# Classes

# 0  -> 8  : style
# 30 -> 38 : fg
# 40 -> 48 : bg
class Shell:
  LOGO  = '\033[1;34;48m'
  FONT1 = '\033[1;32;48m'
  FONT2 = '\033[1;39;48m'
  FONT3 = '\033[1;33;48m'
  FONT4 = '\033[1;36;48m'
  FONT5 = '\033[1;33;48m'
  BLINK = '\033[6;37;48m'
  END   = '\033[0m'

class Floppy:
  GiB = 2 ** 30

class Machine:
  def __init__(self):
    self.disk         = psutil.disk_usage('/')
    self.memory       = psutil.virtual_memory()
    self.cpu          = cpuinfo.get_cpu_info()['brand_raw']
    self.cpu_usage    = psutil.cpu_percent(4)
    self.architecture = subprocess.check_output("uname --processor", shell = True).strip().decode()
    self.kernel       = subprocess.check_output("uname --r", shell = True).strip().decode()
    os_name           = subprocess.check_output("lsb_release -a 2>/dev/null", shell = True).strip().decode()
    self.os_name      = re.findall("Description:\s*(.*)", os_name)[0]
    self.cpu_count    = multiprocessing.cpu_count()
    self.cpu_freq     = psutil.cpu_freq().current
    # Assumes no 1000GHz CPUs, might be wrong!
    if self.cpu_freq > 1000:
      self.cpu_freq /= 1000

  def print_kernel(self):
    print("".join([
      Shell.LOGO,
      "  _      _____ _   _ _    ___   __ ",
      Shell.END,
      Shell.FONT1,
      "KERNEL: ",
      Shell.END,
      Shell.FONT2,
      self.kernel,
      Shell.END]))

  def print_os(self):
    print("".join([
      Shell.LOGO,
      " | |    |_   _| \ | | |  | \ \ / / ",
      Shell.END,
      Shell.FONT1,
      "OS:     ",
      Shell.END,
      Shell.FONT2,
      self.os_name,
      Shell.END]))

  def print_arch(self):
    print("".join([
      Shell.LOGO,
      " | |      | | |  \| | |  | |\ V / ",
      Shell.END,
      Shell.FONT1,
      " ARCH:   ",
      Shell.END,
      Shell.FONT2,
      self.architecture,
      Shell.END]))

  def print_cpu(self):
    print("".join([
      Shell.LOGO,
      " | |      | | | . ` | |  | | > < ",
      Shell.END,
      Shell.FONT1,
      "  CPU:    ",
      Shell.END,
      Shell.FONT2,
      self.cpu,
      Shell.END,
      Shell.FONT5,
      " {:.0f}@{:.2f}GHz".format(self.cpu_count, self.cpu_freq),
      Shell.END,
      Shell.FONT4,
      " ( {:.2f}% )".format(self.cpu_usage),
      Shell.END]))

  def print_ram(self):
    print("".join([
      Shell.LOGO,
      " | |____ _| |_| |\  | |__| |/ . \ ",
      Shell.END,
      Shell.FONT1,
      " RAM:    ",
      Shell.END,
      Shell.FONT2,
      "{:.2f} GiB / ".format(self.memory.total / Floppy.GiB),
      "{:.2f} GiB".format(self.memory.used / Floppy.GiB),
      Shell.END,
      Shell.FONT4,
      " ( {:.2f}% )".format(self.memory.percent),
      Shell.END]))

  def print_disk(self):
    print("".join([
      Shell.LOGO,
      " |______|_____|_| \_|\____//_/ \_\ ",
      Shell.END,
      Shell.FONT1,
      "DISK:   ",
      Shell.END,
      Shell.FONT2,
      "{:.2f} GiB".format(self.disk.total / Floppy.GiB),
      " / {:.2f} GiB".format(self.disk.used / Floppy.GiB),
      Shell.END,
      Shell.FONT4,
      " ( {:.2f}% )".format(100 * self.disk.used / max(1, self.disk.total)),
      Shell.END]))

  def print_info(self):
    self.print_kernel()
    self.print_os()
    self.print_arch()
    self.print_cpu()
    self.print_ram()
    self.print_disk()

# Functions

def print_version():
  print("".join([
    Shell.FONT2,
    VERSION,
    " ",
    Shell.END,
    Shell.BLINK,
    "by Toni Helminen",
    Shell.END]))

def print_logo():
  print("".join([
    Shell.LOGO,
    "       .__                                   \n",
    "  ____ |__| ____  ____   ____  __ _____  ___ \n",
    " /    \|  |/ ___\/ __ \ /    \|  |  \  \/  / \n",
    "|   |  \  \  \__\  ___/|   |  \  |  />    <  \n",
    "|___|  /__|\___  >___  >___|  /____//__/\_ \ \n",
    "     \/        \/    \/     \/            \/ ",
    Shell.END]))

def print_help():
  print("".join([
    Shell.FONT2,
    "nicenux. Prints nice ASCII art Linux information. Written in Python3.\n",
    Shell.END]))

  print("".join([
    Shell.FONT2,
    "Just type: ",
    Shell.END,
    Shell.FONT3,
    "> nicenux.py [opt]\n",
    Shell.END]))

  print("".join([
    Shell.FONT2,
    "Supported options:\n",
    Shell.END]))

  print("".join([
    Shell.FONT3,
    "--help    ",
    Shell.END,
    Shell.FONT2,
    " This help",
    Shell.END]))

  print("".join([
    Shell.FONT3,
    "--logo    ",
    Shell.END,
    Shell.FONT2,
    " Print nicenux ASCII art logo",
    Shell.END]))

  print("".join([
    Shell.FONT3,
    "--version ",
    Shell.FONT2,
    " Show version",
    Shell.END]))

def print_error():
  print("".join([
    Shell.FONT1,
    "Bad args: ",
    Shell.END,
    Shell.FONT2,
    "'",
    " ".join(sys.argv[1:]),
    "'\n",
    Shell.END]))

  print("".join([
    Shell.FONT1,
    "See:",
    Shell.END]))

  print("".join([
    Shell.FONT2,
    "> nicenux.py --help",
    Shell.END]))

def print_info():
  machine = Machine()
  machine.print_info()

def main():
  if len(sys.argv) == 2 and sys.argv[1] == "--version":
    print_version()
  elif len(sys.argv) == 2 and sys.argv[1] == "--help":
    print_help()
  elif len(sys.argv) == 2 and sys.argv[1] == "--logo":
    print_logo()
  elif len(sys.argv) != 1:
    print_error()
  else:
    print_info()

# Init

if __name__ == "__main__":
  main()
