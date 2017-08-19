#!/usr/bin/env python

#----------------------------------#
# ,--. ,--.         ,--.           #
# |  .'   / ,---. ,-'  '-. ,--,--. #
# |  .   ' | .-. |'-.  .-'' ,-.  | #
# |  |\   \' '-' '  |  |  \ '-'  | #
# `--' '--' `---'   `--'   `--`--' #
#            kotajacob.tk          #
# Copyright (C) 2017  Dakota Walsh #
#----------------------------------#

"""
Wal Steam

Usage:
  wal_steam.py (-w | -g)
  wal_steam.py (-h | --help)
  wal_steam.py (-v | --version)

Options:
  -w                   use wal for colors
  -g                   use wpg for colors
  -h --help            show this help message and exit
  -v --version         show version and exit
"""
from lib.docopt import docopt
import os

# set some variables for the file locations
wpgConfig = os.path.expanduser("~/.wallpapers/current.css")
walConfig = os.path.expanduser("~/.cache/wal/colors.css")

def parseCss(option):
    if option == 0:
        # parse wpg config
        f_name = open(wpgConfig, 'r')
        raw_file = f_name.readlines() # save lines into raw_file
        del raw_file[0:11] # delete elements up to the colors
        del raw_file[16]   # also that last line is just a } (16 now because we removed some already)

        colors = []
        for line in raw_file: # loop through raw_file
            tmp = line[line.find("#"):] # remove everything before the octothorpe
            tmp = tmp[:7] # remove everything after the color

            colors.append(tmp) # add tmp to the new list

        print(colors)
        f_name.close()
    else:
        # parse wal config
        f_name = open(walConfig, 'r')
        raw_file = f_name.readlines() # save lines into raw_file
        del raw_file[0:11] # delete elements up to the colors
        del raw_file[16]   # also that last line is just a } (16 now because we removed some already)

        colors = []
        for line in raw_file: # loop through raw_file
            tmp = line[line.find("#"):] # remove everything before the octothorpe
            tmp = tmp[:7] # remove everything after the color

            colors.append(tmp) # add tmp to the new list

        print(colors)
        f_name.close()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Wal Steam 0.1.0') # create the flags from the comment

    if (arguments['--help']==False and arguments['--version']==False): # determine which option was selected
        if (arguments['-g']==True):
            parseCss(0)
        else:
            parseCss(1)
