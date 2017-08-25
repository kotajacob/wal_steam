#!/usr/bin/env python3

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
import shutil                             # copying files
import os                                 # getting paths
import urllib.request                     # downloading the zip files
import zipfile                            # extracting the zip files
import sys
import argparse                           # argument parsing
import json                               # writing and reading the config file
from distutils.dir_util import copy_tree  # copytree from shutil is broken so use copy_tree

# set some variables for the file locations
ROOT_DIR         = os.path.expanduser("~/.cache/wal_steam/")
CONFIG_DIR       = os.path.expanduser("~/.config/wal_steam/")
SKIN_NAME        = "Metro 4.2.4 Wal_Mod"
VERSION          = "Wal Steam 1.2.0"
CONFIG_FILE      = "config.json"
COLORS_FILE      = os.path.join(ROOT_DIR, "colors.styles")

STEAM_DIR_OTHER  = os.path.expanduser("~/.steam/steam/skins")
STEAM_DIR_UBUNTU = os.path.expanduser("~/.steam/skins")
WAL_COLORS       = os.path.expanduser("~/.cache/wal/colors.css")
WPG_COLORS       = os.path.expanduser("~/.wallpapers/current.css")

METRO_URL        = "http://metroforsteam.com/downloads/4.2.4.zip"
METRO_ZIP        = os.path.join(ROOT_DIR, "metroZip.zip")
METRO_DIR        = os.path.join(ROOT_DIR, "metroZip")
METRO_COPY       = os.path.join(METRO_DIR, "Metro 4.2.4")

METRO_PATCH_URL  = "https://github.com/redsigma/UPMetroSkin/archive/196feafc14deae103355b4fee1ecc4cda9288c7f.zip" # A link to the version we've tested rather than the latest, just in case they break things upstream.
METRO_PATCH_ZIP  = os.path.join(ROOT_DIR, "metroPatchZip.zip")
METRO_PATCH_DIR  = os.path.join(ROOT_DIR, "metroPatchZip")
METRO_PATCH_COPY = os.path.join(METRO_PATCH_DIR, "UPMetroSkin-196feafc14deae103355b4fee1ecc4cda9288c7f/Unofficial 4.2.4 Patch/Main Files [Install First]")

def tupToPrint(tup):
    tmp = ' '.join(map(str, tup)) # convert the tupple (rgb color) to a string ready to print
    return tmp

def setColors(colors, config, oSys):
    print ("Patching new colors")

    # delete the old colors file if present in cache
    try:
        os.remove(COLORS_FILE) # just in case it was already there for some reason
    except FileNotFoundError:
        print("No file to remove")

    f = open(COLORS_FILE, 'w')

    # First write the variables we aren't changing
    f.write('\"settings.styles\"\n')
    f.write('{\n')
    f.write('\tcolors\n')
    f.write('\t{\n')
    f.write('\t\tnone=\"0 0 0 0\"\n')
    f.write('\t\tFocus_T=\"0 114 198 30.6\"\n')
    f.write('\t\twhite03=\"255 255 255 7.65\"\n')
    f.write('\t\twhite08=\"255 255 255 20.4\"\n')
    f.write('\t\twhite05=\"255 255 255 12.75\"\n')
    f.write('\t\twhite10=\"255 255 255 25.5\"\n')
    f.write('\t\twhite12=\"255 255 255 30.6\"\n')
    # f.write('\t\twhite15=\"255 255 255 \"\n') this was commented in the file...
    f.write('\t\twhite20=\"255 255 255 51\"\n')
    f.write('\t\twhite24=\"255 255 255 61.2\"\n')
    f.write('\t\twhite25=\"255 255 255 63.75\"\n')
    f.write('\t\twhite35=\"255 255 255 89.25\"\n')
    f.write('\t\twhite45=\"255 255 255 114.75\"\n')
    f.write('\t\twhite50=\"255 255 255 127.5\"\n')
    f.write('\t\twhite75=\"255 255 255 191.25\"\n')
    f.write('\t\twhite=\"255 255 255 255\"\n')
    f.write('\t\tblack03=\"0 0 0 7.65\"\n')
    f.write('\t\tblack08=\"0 0 0 20.4\"\n')
    f.write('\t\tblack05=\"0 0 0 12.75\"\n')
    f.write('\t\tblack10=\"0 0 0 25.5\"\n')
    f.write('\t\tblack12=\"0 0 0 30.6\"\n')
    # f.write('\t\tblack15=\"0 0 0 38.25\"\n') this was commented in the file too...
    f.write('\t\tblack20=\"0 0 0 51\"\n')
    f.write('\t\tblack24=\"0 0 0 61.2\"\n')
    f.write('\t\tblack35=\"0 0 0 106\"\n')
    f.write('\t\tblack25=\"0 0 0 63.75\"\n')
    f.write('\t\tblack75=\"0 0 0 191.25\"\n')
    f.write('\t\tBlack=\"0 0 0 255\"\n')
    f.write('\t\tScroll_blu=\"88 168 242 165\"\n')
    f.write('\t\tScroll_blu_s=\"103 193 245 175\"\n')
    f.write('\t\tDetailsBackground=\"Black45\"\n')
    f.write('\t\tDetailPanels=\"black45\"\n')
    f.write('\t\tOverlaySidePanels=\"255 255 255 144.75\"\n')
    f.write('\t\tOverlayHover05=\"255 255 255 12.75\"\n')
    f.write('\t\ttransparent_notification=\"5 5 5 229.5\"\n')
    f.write('\t\tchatframe=\"White50\"\n')
    f.write('\t\tScrollBar=\"86 86 86 255\"\n')
    f.write('\t\tScrollBarH=\"110 110 110 255\"\n')
    f.write('\t\tGrey1=\"40 40 40 255\"\n')
    f.write('\t\tGrey2=\"48 48 48 255\"\n')
    f.write('\t\tGrey3=\"75 75 75 255\"\n')
    f.write('\t\tClientBGTransparent=\"43 43 43 191.25\"\n')
    f.write('\t\tRed=\"255 0 0 255\"\n')
    f.write('\t\tW10close_Red_h=\"232 18 35 255\"\n')
    f.write('\t\tW10close_Red_p=\"241 112 121 255\"\n')

    # Now write the variables we will be changing
    ii = 0
    for i in config:
        # basically we need to write the steam variable and the color from the config dict
        if (ii % 2 == 0):
            alpha = "alpha_" + i
            f.write('\t\t' + i + '=\"' + tupToPrint(colors[config[i]]) + ' ' + str(config[alpha])  +  '\"\n')
        ii = ii + 1

    # Final formatting stuff
    f.write('\t}\n')
    f.write('}\n')
    f.close()

    # now copy it to the proper place based on the os
    if (oSys == 0):
        # linux other
        shutil.copy(COLORS_FILE, os.path.join(STEAM_DIR_OTHER, SKIN_NAME))
    else:
        # linux ubuntu
        shutil.copy(COLORS_FILE, os.path.join(STEAM_DIR_UBUNTU, SKIN_NAME))

    # cleanup by removing generated color file
    os.remove(COLORS_FILE)
    print("Wal colors are now patched and ready to go")
    print("If this is your first run you may have to ")
    print("enable Metro Wal Mod skin in steam then ")
    print("simply restart steam!")
    
###################
# color functions #
###################

def getConfig():
    # read the config file and return a dictionary of the variables and color variables
    f = open(os.path.join(CONFIG_DIR, CONFIG_FILE), 'r')
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

##########################
# checkInstall functions #
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
    print("Generating config")
    # obviously this is a huge block of code
    f = open(os.path.join(CONFIG_DIR, CONFIG_FILE), 'w')
    config = dict(black45=0, alpha_black45=120, Focus=4, alpha_Focus=255, Friends_InGame=1, alpha_Friends_InGame=255, Friends_Online=2, alpha_Friends_Online=255, FrameBorder=0, alpha_FrameBorder=255, GameList=0, alpha_GameList=255, Dividers=15, alpha_Dividers=255, Seperator=15, alpha_Seperator=255, OverlayBackground=0, alpha_OverlayBackground=80, OverlayPanels=0, alpha_OverlayPanels=120, OverlayClock=15, alpha_OverlayClock=120, OverlaySideButtons=1, alpha_OverlaySideButtons=120, OverlaySideButtons_h=4, alpha_OverlaySideButtons_h=120, TextEntry=0, alpha_TextEntry=255, Header_Dark=0, alpha_Header_Dark=255, ClientBG=0, alpha_ClientBG=255)
    # write to json config
    json.dump(config, f)
    f.close()

def checkConfig():
    # check for the config
    if not os.path.isdir(CONFIG_DIR):
        # make the config directory
        os.mkdir(CONFIG_DIR)

        # download or make config file
        makeConfig()
    elif not os.path.isfile(os.path.join(CONFIG_DIR, CONFIG_FILE)):
        # download or make the config file
        makeConfig()
    else:
        # config file found!
        print("Wal Steam config found")

def checkCache():
    # check for the cache
    if not os.path.isdir(ROOT_DIR):
        # make the cache directory
        os.mkdir(ROOT_DIR)

        # download, extract, and patch metro for steam
        makeSkin()
    else:
        # cache folder exists
        print("Wal Steam cache found")

def checkInstall(oSys):
    # check if the cache exists, make it if not
    checkCache()

    # check if the config file exists
    checkConfig()

    # check if the skin is installed, install it if not
    checkSkin(oSys)

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

def getArgs():
    # get the arguments with argparse
    description = "Wal Steam"
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("-v", "--version", action="store_true",
            help="Print wal_steam version.")

    arg.add_argument("-w", action="store_true",
            help="Get colors from wal.")

    arg.add_argument("-g", action="store_true",
            help="Get colors from wpg.")

    return arg.parse_args()

def main():
    # set default mode to wal
    # 0 = wal
    # 1 = wpgtk
    mode = 0

    # parse the arguments
    arguments = getArgs()
    if arguments.version:
        print(VERSION)
        sys.exit()

    # make sure they didn't select both wal and wpg
    if arguments.w and arguments.g:
        sys.exit("Error: You must select wpg or wal")

    # set the mode for either wal or wpg
    if arguments.w:
        mode = 0
    if arguments.g:
        mode = 1

    # check where the os installed steam
    # 0 = ~/.steam/steam/skins - more common
    # 1 = ~/.steam/skins       - used on ubuntu and its derivatives
    oSys = checkOs()

    # check for the cache, the skin, and get them if needed
    checkInstall(oSys)

    # get a list from either wal or wpg based on the mode
    colors = getColors(mode)

    # convert our list of colors from hex to rgb
    colors = hexToRgb(colors)

    # get a dictionary of the config settings from the config file
    config = getConfig()

    # finally create a temp colors.styles and copy it in updating the skin
    setColors(colors, config, oSys)

if __name__ == '__main__':
    main()
