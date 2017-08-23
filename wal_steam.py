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
from lib.docopt import docopt             # argument parsing
from shutil import move                   # moveing files
from shutil import copy                   # copying files
import os                                 # getting paths
import urllib.request                     # downloading the zip files
import zipfile                            # extracting the zip files
from distutils.dir_util import copy_tree  # copytree from shutil is FUCKING GARBAGE for no reason so we use this instead
import json                               # writing and reading the config file

# set some variables for the file locations
ROOT_DIR = os.path.expanduser("~/.cache/wal_steam/")
SKIN_NAME = "Metro 4.2.4"
CONFIG_FILE = "config.json"

STEAM_DIR_OTHER = os.path.expanduser("~/.steam/steam/skins")
STEAM_DIR_UBUNTU = os.path.expanduser("~/.steam/skins")
WAL_COLORS = os.path.expanduser("~/.cache/wal/colors.css")
WPG_COLORS = os.path.expanduser("~/.wallpapers/current.css")

METRO_URL = "http://metroforsteam.com/downloads/4.2.4.zip"
METRO_ZIP = os.path.join(ROOT_DIR, "metroZip.zip")
METRO_DIR = os.path.join(ROOT_DIR, "metroZip")
METRO_COPY = os.path.join(METRO_DIR, "Metro 4.2.4")

METRO_PATCH_URL = "http://github.com/redsigma/UPMetroSkin/archive/master.zip"
METRO_PATCH_ZIP = os.path.join(ROOT_DIR, "metroPatchZip.zip")
METRO_PATCH_DIR = os.path.join(ROOT_DIR, "metroPatchZip")
METRO_PATCH_COPY = os.path.join(METRO_PATCH_DIR, "UPMetroSkin-master/Unofficial 4.2.4 Patch/Main Files [Install First]")

def setColors(colors, config):
    print (colors)
    print (config)

def getConfig():
    # read the config file and return a dictionary of the variables and color variables
    f = open(os.path.join(ROOT_DIR, CONFIG_FILE), 'r')
    result = json.load(f)
    f.close()
    return result

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
    return tmpColors

def getColors(mode):
    if (mode == 0):
        # using colors from wal
        colorsFile = WAL_COLORS
    else:
        # using colors from wpg
        colorsFile = WPG_COLORS
    # parse the file
    print("Reading colors")
    f = open(colorsFile, 'r')
    rawFile = f.readlines() # save the lines to rawFile
    # delete the lines not involving the colors
    del rawFile[0:11]
    del rawFile[16]

    # loop through rawFile and store colors in a list
    colors = []
    for line in rawFile:
        # delete everything but the hex code
        tmp = line[line.find("#"):]
        tmp = tmp[:7]

        # append the hex code to the colors list
        colors.append(tmp)

    f.close()
    return colors

def getMode(arguments):
    if (arguments['-w'] == True):
        return 0
    if (arguments['-g'] == True):
        return 1

##########################
#                        #
# checkInstall functions #
#                        #
##########################

def checkSkin(oSys):
    # check if the skin is in the skin folder
    if (oSys == 0):
        # path is os other
        if not os.path.isdir(os.path.join(STEAM_DIR_OTHER, SKIN_NAME)):
            # skin was not found, copy it over
            print("Installing skin")
            copy_tree(METRO_PATCH_COPY, os.path.join(STEAM_DIR_OTHER, SKIN_NAME))
        else:
            print("Wal Steam skin found")
    else:
        # path is os ubuntu
        if not os.path.isdir(os.path.join(STEAM_DIR_UBUNTU, SKIN_NAME)):
            # skin was not found, copy it over
            print("Installing skin")
            copy_tree(METRO_PATCH_COPY, os.path.join(STEAM_DIR_UBUNTU, SKIN_NAME))
        else:
            print("Wal Steam skin found")

def checkOs():
    # check if ~/.steam/steam/skins exists
    if os.path.isdir(STEAM_DIR_OTHER):
        return 0
    # check if ~/.steam/skins exists
    elif os.path.isdir(STEAM_DIR_UBUNTU):
        return 1
    # close with error message otherwise
    else:
        sys.exit("Error: Steam install not found!")

def makeSkin():
    # download metro for steam and extract
    print("Downloading Metro for steam")
    urllib.request.urlretrieve(METRO_URL, METRO_ZIP)
    z = zipfile.ZipFile(METRO_ZIP, 'r')
    z.extractall(METRO_DIR)
    z.close()

    # download metro for steam patch and extract
    print("Downloading Metro patch")
    urllib.request.urlretrieve(METRO_PATCH_URL, METRO_PATCH_ZIP)
    z = zipfile.ZipFile(METRO_PATCH_ZIP, 'r')
    z.extractall(METRO_PATCH_DIR)
    z.close()

    # finally apply the patch
    copy_tree(METRO_PATCH_COPY, METRO_COPY) # use copy_tree not copytree, shutil copytree is broken

def makeConfig():
    # generate the config if it's missing
    # obviously this is a huge block of code
    f = open(os.path.join(ROOT_DIR, CONFIG_FILE), 'w')
    config = dict(black45=0, Focus=4, Friends_InGame=1, Friends_Online=2, FrameBorder=0, GameList=0, Dividers=15, Seperator=15, OverlayBackground=0, OverlayPanels=0, OverlayClock=15, OverlaySideButtons=1, OverlaySideButtons_h=4, TextEntry=0, Header_Dark=0, ClientBG=0)
    # write to json config
    json.dump(config, f)
    f.close()

def checkCache():
    # check for the cache
    if not os.path.isdir(ROOT_DIR):
        # make the config directory
        os.mkdir(ROOT_DIR)

        # make the config file
        makeConfig()

        # download, extract, and patch metro for steam
        makeSkin()
    else:
        # cache folder exists
        print("Wal Steam cache found")

def checkInstall():
    # check if the cache exists, make it if not
    checkCache()

    # check where the os installed steam
    # 0 = ~/.steam/steam/skins - more common
    # 1 = ~/.steam/skins       - used on ubuntu and its derivatives
    oSys = checkOs()

    # check if the skin is installed, install it if not
    checkSkin(oSys)

def main(arguments):
    # check for the cache, the skin, and get them if needed
    checkInstall()

    # use the arguments to set a mode variable
    # 0 = wal
    # 1 = wpgtk
    mode = getMode(arguments)

    # get a list from either wal or wpg based on the mode
    colors = getColors(mode)

    # convert our list of colors from hex to rgb
    colors = hexToRgb(colors)

    # get a dictionary of the config settings from the config file
    config = getConfig()

    # finally create a temp colors.styles and copy it in updating the skin
    setColors(colors, config)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Wal Steam 1.2.0') # create the flags from the comment
    main(arguments)
