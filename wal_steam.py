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
from distutils.dir_util import copy_tree  # copytree from shutil is FUCKING GARBAGE for no reason so we use this instead
from lib.docopt import docopt             # argument parsing

# set some variables for the file locations
ROOT_DIR = os.path.expanduser("~/.cache/wal_steam/")

metroUrl           = "http://metroforsteam.com/downloads/4.2.4.zip"
metroPatchUrl      = "http://github.com/redsigma/UPMetroSkin/archive/master.zip"

metroZip           = os.path.join(ROOT_DIR, "metroZip.zip")
metroPatchZip      = os.path.join(ROOT_DIR, "metroPatchZip.zip")
metroResource      = os.path.join(ROOT_DIR, "metroZip/")
metroPatchResource = os.path.join(ROOT_DIR, "metroPatchZip/")
metroPatchCopy     = os.path.join(ROOT_DIR, "metroPatchZip/UPMetroSkin-master/Unofficial 4.2.4 Patch/Main Files [Install First]/")
metroCopy          = os.path.join(ROOT_DIR, "metroZip/Metro 4.2.4/")

metroInstallOther  = os.path.expanduser("~/.steam/steam/skins/Metro 4.2.4 Wal_Mod/")
metroInstallUbuntu = os.path.expanduser("~/.steam/skins/Metro 4.2.4 Wal_Mod/")
steamSkins         = os.path.expanduser("~/.steam/steam/skins/")
steamSkinsUbuntu   = os.path.expanduser("~/.steam/skins/")

newColors          = os.path.join(ROOT_DIR, "colors.styles")
wpgConfig          = os.path.expanduser("~/.wallpapers/current.css")
walConfig          = os.path.expanduser("~/.cache/wal/colors.css")

# Set metro install
if os.path.isdir(steamSkins):
    # use "other" path
    metroInstall = metroInstallOther
elif os.path.isdir(steamSkinsUbuntu):
    # use "ubuntu" path
    metroInstall = metroInstallUbuntu
else:
    # no steam found
    sys.exit("Error: Steam not found!")


def tupToPrint(tup):
    tmp = ' '.join(map(str, tup)) # convert the tupple (rgb color) to a string ready to print
    return tmp

def checkDir(dirName):
    # check if wal_steam has been run before
    if os.path.isdir(dirName):
        return True
    else:
        return False

def makeStyle(colors):
    # create and write the colors.styles file
    print("Patching new colors")

    try:
        os.remove(newColors) # just in case it was already there for some reason
    except FileNotFoundError:
        print("No file to remove")
    f_name = open(newColors, 'w')

    # First write the variables we aren't changing
    f_name.write('\"settings.styles\"\n')
    f_name.write('{\n')
    f_name.write('\tcolors\n')
    f_name.write('\t{\n')
    f_name.write('\t\tnone=\"0 0 0 0\"\n')
    f_name.write('\t\tFocus_T=\"0 114 198 30.6\"\n')
    f_name.write('\t\twhite03=\"255 255 255 7.65\"\n')
    f_name.write('\t\twhite08=\"255 255 255 20.4\"\n')
    f_name.write('\t\twhite05=\"255 255 255 12.75\"\n')
    f_name.write('\t\twhite10=\"255 255 255 25.5\"\n')
    f_name.write('\t\twhite12=\"255 255 255 30.6\"\n')
    # f.write('\t\twhite15=\"255 255 255 \"\n') this was commented in the file...
    f_name.write('\t\twhite20=\"255 255 255 51\"\n')
    f_name.write('\t\twhite24=\"255 255 255 61.2\"\n')
    f_name.write('\t\twhite25=\"255 255 255 63.75\"\n')
    f_name.write('\t\twhite35=\"255 255 255 89.25\"\n')
    f_name.write('\t\twhite45=\"255 255 255 114.75\"\n')
    f_name.write('\t\twhite50=\"255 255 255 127.5\"\n')
    f_name.write('\t\twhite75=\"255 255 255 191.25\"\n')
    f_name.write('\t\twhite=\"255 255 255 255\"\n')
    f_name.write('\t\tblack03=\"0 0 0 7.65\"\n')
    f_name.write('\t\tblack08=\"0 0 0 20.4\"\n')
    f_name.write('\t\tblack05=\"0 0 0 12.75\"\n')
    f_name.write('\t\tblack10=\"0 0 0 25.5\"\n')
    f_name.write('\t\tblack12=\"0 0 0 30.6\"\n')
    # f.write('\t\tblack15=\"0 0 0 38.25\"\n') this was commented in the file too...
    f_name.write('\t\tblack20=\"0 0 0 51\"\n')
    f_name.write('\t\tblack24=\"0 0 0 61.2\"\n')
    f_name.write('\t\tblack35=\"0 0 0 106\"\n')
    f_name.write('\t\tblack25=\"0 0 0 63.75\"\n')
    f_name.write('\t\tblack75=\"0 0 0 191.25\"\n')
    f_name.write('\t\tBlack=\"0 0 0 255\"\n')
    f_name.write('\t\tScroll_blu=\"88 168 242 165\"\n')
    f_name.write('\t\tScroll_blu_s=\"103 193 245 175\"\n')
    f_name.write('\t\tDetailsBackground=\"Black45\"\n')
    f_name.write('\t\tDetailPanels=\"black45\"\n')
    f_name.write('\t\tOverlaySidePanels=\"255 255 255 144.75\"\n')
    f_name.write('\t\tOverlayHover05=\"255 255 255 12.75\"\n')
    f_name.write('\t\ttransparent_notification=\"5 5 5 229.5\"\n')
    f_name.write('\t\tchatframe=\"White50\"\n')
    f_name.write('\t\tScrollBar=\"86 86 86 255\"\n')
    f_name.write('\t\tScrollBarH=\"110 110 110 255\"\n')
    f_name.write('\t\tGrey1=\"40 40 40 255\"\n')
    f_name.write('\t\tGrey2=\"48 48 48 255\"\n')
    f_name.write('\t\tGrey3=\"75 75 75 255\"\n')
    f_name.write('\t\tClientBGTransparent=\"43 43 43 191.25\"\n')
    f_name.write('\t\tRed=\"255 0 0 255\"\n')
    f_name.write('\t\tW10close_Red_h=\"232 18 35 255\"\n')
    f_name.write('\t\tW10close_Red_p=\"241 112 121 255\"\n')

    # Now for some variables we are changing
    f_name.write('\t\tblack45=\"' + tupToPrint(colors[0]) + ' 120' + '\"\n')
    f_name.write('\t\tFocus=\"' + tupToPrint(colors[4]) + ' 255' + '\"\n')
    f_name.write('\t\tFriends_InGame=\"' + tupToPrint(colors[1]) + ' 255' + '\"\n')
    f_name.write('\t\tFriends_Online=\"' + tupToPrint(colors[2]) + ' 255' + '\"\n')
    f_name.write('\t\tFrameBorder=\"' + tupToPrint(colors[0]) + ' 255' + '\"\n')
    f_name.write('\t\tGameList=\"' + tupToPrint(colors[0]) + ' 255' + '\"\n')
    f_name.write('\t\tDividers=\"' + tupToPrint(colors[15]) + ' 255' + '\"\n')
    f_name.write('\t\tSeperator=\"' + tupToPrint(colors[15]) + ' 255' + '\"\n')
    f_name.write('\t\tOverlayBackground=\"' + tupToPrint(colors[0]) + ' 80' + '\"\n')
    f_name.write('\t\tOverlayPanels=\"' + tupToPrint(colors[0]) + ' 120' + '\"\n')
    f_name.write('\t\tOverlayClock=\"' + tupToPrint(colors[15]) + ' 120' + '\"\n')
    f_name.write('\t\tOverlaySideButtons=\"' + tupToPrint(colors[1]) + ' 120' + '\"\n')
    f_name.write('\t\tOverlaySideButtons_h=\"' + tupToPrint(colors[4]) + ' 120' + '\"\n')
    f_name.write('\t\tTextEntry=\"' + tupToPrint(colors[0]) + ' 255' + '\"\n')
    f_name.write('\t\tHeader_Dark=\"' + tupToPrint(colors[0]) + ' 255' + '\"\n')
    f_name.write('\t\tClientBG=\"' + tupToPrint(colors[0]) + ' 255' + '\"\n')

    # Final formatting stuff
    f_name.write('\t}\n')
    f_name.write('}\n')

    f_name.close()
    shutil.copy(newColors, metroInstall)
    # cleanup by removing generated color file
    os.remove(newColors)
    print("Wal colors are now patched and ready to go")
    print("If this is your first run you may have to ")
    print("enable Metro Wal Mod skin in steam then ")
    print("simply restart steam!")

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

def parseCss(config):
    # parse colors file and return colors in list
    print("Reading colors")
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

##################
# For installing #
#   Wal Steam    #
##################

def makeCache():
    os.mkdir(ROOT_DIR)

def downloadMetro():
    # download metro for steam
    # download metro for steam patch
    print("Downloading Metro for steam")
    urllib.request.urlretrieve(metroUrl, metroZip)
    z = zipfile.ZipFile(metroZip, 'r')
    z.extractall(metroResource)
    z.close()
    print("Downloading Metro patch")
    urllib.request.urlretrieve(metroPatchUrl, metroPatchZip)
    z = zipfile.ZipFile(metroPatchZip, 'r')
    z.extractall(metroPatchResource)
    z.close()

def installMetro():
    print("Installing Metro Wal")
    copy_tree(metroPatchCopy, metroCopy) # use copy_tree not copytree, shutil copytree is broken
    copy_tree(metroCopy, metroInstall)
    print("Metro Wal is now installed")

def checkInstall():
    if not checkDir(ROOT_DIR):
        # wal_steam cache missing
        # redownload and patch
        makeCache()
        downloadMetro()
        installMetro()
    else:
        # cache was found
        # check for skin
        if not checkDir(metroInstall):
            # metro install missing
            downloadMetro()
            installMetro()
        else:
            # metro install found
            print("Metro install found")

def main(arguments):
    checkInstall()

    if (arguments['--help'] == False and arguments['--version'] == False): # determine the mode
        if (arguments['-g'] == True):
            colors = parseCss(wpgConfig) # they picked g so parse wpg
            colors = hexToRgb(colors)
            makeStyle(colors)
        else:
            colors = parseCss(walConfig) # they picked w so parse wal
            colors = hexToRgb(colors)
            makeStyle(colors)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Wal Steam 1.1.0') # create the flags from the comment
    main(arguments)
