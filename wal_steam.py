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
wpgConfig     = os.path.expanduser("~/.wallpapers/current.css")
walConfig     = os.path.expanduser("~/.cache/wal/colors.css")
metroSettings = os.path.expanduser("~/.steam/steam/skins/Fake\ Skin/settings.styles") # REPLACE AFTER TESTS
metroColors   = os.path.expanduser("~/.steam/steam/skins/Fake\ Skin/wal_colors.styles") # REPLACE AFTER TESTS

def makeStyle(colors):
    # create and write the wal_colors.styles file
    print("Makeing color styles")
    print(colors)

def replaceSettings():
    # replace the settings.styles file with one tweaked to load our colors :)
    # first make a backup of their settings.styles file
    print("Replacing settings")

def hexToRgb(hexColors):
    # convert hex colors to rgb colors (takes a list)
    tmpColors = []
    rgbColors = []
    for color in hexColors: # loop through the hex colors
        # remove the optothorpe
        # use tuple and a loop to convert them to rgb
        # append new colors to our rgb list
        tmp = color.lstrip('#')
        tmpColors.append(tuple(int(tmp[i:i+2], 16) for i in (0, 2 ,4)))
    # put the colors in the correct format
    for color in tmpColors: # loop through the new RGB colors
        # remove parentheses
        tmp = color
        rgbColors.append(tmp)

    return rgbColors

def parseCss(config):
    # parse colors file and return colors in list
    f_name = open(config, 'r')
    raw_file = f_name.readlines() # save lines into raw_file
    del raw_file[0:11] # delete elements up to the colors
    del raw_file[16]   # also that last line is just a } (16 now because we removed some already)

    colors = []
    for line in raw_file: # loop through raw_file
        tmp = line[line.find("#"):] # remove everything before the octothorpe
        tmp = tmp[:7] # remove everything after the color

        colors.append(tmp) # add tmp to the new list

    f_name.close()
    return colors

def main(arguments):
    if (arguments['--help'] == False and arguments['--version'] == False): # determine the mode
        if (arguments['-g'] == True):
            colors = parseCss(wpgConfig) # they picked g so parse wpg
            colors = hexToRgb(colors)
            makeStyle(colors)
            replaceSettings()
        else:
            colors = parseCss(walConfig) # they picked w so parse wal
            colors = hexToRgb(colors)
            makeStyle(colors)
            replaceSettings()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Wal Steam 0.1.0') # create the flags from the comment
    main(arguments)
