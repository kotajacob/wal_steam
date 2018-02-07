#!/usr/bin/env python3
"""
Wal Steam

========================================
oooo    oooo               .
`888   .8P'              .o8
 888  d8'     .ooooo.  .o888oo  .oooo.
 88888[      d88' `88b   888   `P  )88b
 888`88b.    888   888   888    .oP"888
 888  `88b.  888   888   888 . d8(  888
o888o  o888o `Y8bod8P'   "888" `Y888""8o
               @nilsu.org
=== Copyright (C) 2017  Dakota Walsh ===
"""
import shutil                             # copying files
import os                                 # getting paths
import urllib.request                     # downloading the zip files
import zipfile                            # extracting the zip files
import sys
import argparse                           # argument parsing
from distutils.dir_util import copy_tree  # copytree from shutil is broken so use copy_tree

# set some variables for the file locations
HOME_DIR          = os.getenv("HOME", os.getenv("USERPROFILE")) # should be crossplatform
CACHE_DIR         = os.path.join(HOME_DIR, ".cache", "wal_steam")
CONFIG_DIR        = os.path.join(HOME_DIR, ".config", "wal_steam")
SKIN_NAME         = "Metro 4.2.4 Wal_Mod"
VERSION           = "1.2.5"
CONFIG_FILE       = "wal_steam.conf"
COLORS_FILE       = os.path.join(CACHE_DIR, "colors.styles")
CONFIG_URL        = "https://raw.githubusercontent.com/kotajacob/wal_steam_config/master/wal_steam.conf"

STEAM_DIR_OTHER   = os.path.expanduser("~/.steam/steam/skins")
STEAM_DIR_OSX     = os.path.expanduser("~/Library/Application Support/Steam/Steam.AppBundle/Steam/Contents/MacOS/skins")
STEAM_DIR_UBUNTU  = os.path.expanduser("~/.steam/skins")
STEAM_DIR_WINDOWS = "C:\Program Files (x86)\Steam\skins"
WAL_COLORS        = os.path.join(HOME_DIR, ".cache", "wal", "colors.css")
WPG_COLORS        = os.path.join(HOME_DIR, ".wallpapers", "current.css")

METRO_URL        = "http://metroforsteam.com/downloads/4.2.4.zip"
METRO_ZIP        = os.path.join(CACHE_DIR, "metroZip.zip")
METRO_DIR        = os.path.join(CACHE_DIR, "metroZip")
METRO_COPY       = os.path.join(METRO_DIR, "Metro 4.2.4")

METRO_PATCH_URL  = "https://codeload.github.com/redsigma/UPMetroSkin/zip/196feafc14deae103355b4fee1ecc4cda9288c7f" # A link to the version we've tested rather than the latest, just in case they break things upstream.
METRO_PATCH_ZIP  = os.path.join(CACHE_DIR, "metroPatchZip.zip")
METRO_PATCH_DIR  = os.path.join(CACHE_DIR, "metroPatchZip")
METRO_PATCH_COPY = os.path.join(METRO_PATCH_DIR, "UPMetroSkin-196feafc14deae103355b4fee1ecc4cda9288c7f", "Unofficial 4.2.4 Patch", "Main Files [Install First]")
METRO_PATCH_HDPI = os.path.join(METRO_PATCH_DIR, "UPMetroSkin-196feafc14deae103355b4fee1ecc4cda9288c7f", "Unofficial 4.2.4 Patch", "Extras", "High DPI", "Increased fonts", "Install")

def tupToPrint(tup):
    tmp = ' '.join(map(str, tup)) # convert the tupple (rgb color) to a string ready to print
    return tmp

def setColors(colors, variables, walColors, alpha, steam_dir):
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
    for i in variables:
        f.write('\t\t' + i + '=\"' + tupToPrint(colors[int(walColors[ii])]) + ' ' + str(alpha[ii])  +  '\"\n')
        ii = ii + 1

    # Final formatting stuff
    f.write('\t}\n')
    f.write('}\n')
    f.close()

    # now copy it to the proper place based on the os
    shutil.copy(COLORS_FILE, os.path.join(steam_dir, SKIN_NAME))

    # cleanup by removing generated color file
    os.remove(COLORS_FILE)
    print("Wal colors are now patched and ready to go")
    print("If this is your first run you may have to ")
    print("enable Metro Wal Mod skin in steam then ")
    print("simply restart steam!")

###################
# color functions #
###################
def getConfigAlpha():
    # read the config file and return a dictionary of the variables and color variables
    f = open(os.path.join(CONFIG_DIR, CONFIG_FILE), 'r')

    # save the lines of the config file to rawFile
    rawFile = f.readlines()

    # loop through rawFile
    result = []
    for line in rawFile:
        tmpResult = line[line.find(",")+1:line.find("\n")]
        result.append(tmpResult)
    f.close()
    return result

def getConfigColor():
    # read the config file and return a dictionary of the variables and color variables
    f = open(os.path.join(CONFIG_DIR, CONFIG_FILE), 'r')

    # save the lines of the config file to rawFile
    rawFile = f.readlines()

    # loop through rawFile
    result = []
    for line in rawFile:
        tmpResult = line[line.find("=")+1:line.find(",")]
        result.append(tmpResult)
    f.close()
    return result

def getConfigVar():
    # read the config file and return a dictionary of the variables and color variables
    f = open(os.path.join(CONFIG_DIR, CONFIG_FILE), 'r')

    # save the lines of the config file to rawFile
    rawFile = f.readlines()

    # loop through rawFile
    result = []
    for line in rawFile:
        tmpResult = line[:line.find("=")]
        result.append(tmpResult)
    f.close()
    return result

def hexToRgb(hexColors):
    """Convert hex colors to rgb colors (takes a list)."""
    return [tuple(bytes.fromhex(color.strip("#"))) for color in hexColors]

def getColors(mode):
    if (mode == 0):
        # using colors from wal
        colorsFile = WAL_COLORS
    else:
        # using colors from wpg
        colorsFile = WPG_COLORS
    # parse the file
    print("Reading colors")
    try:
        f = open(colorsFile, 'r')
    except:
        print("Error: Colors file missing. Make sure you've run pywal/wpg before wal_steam")
        sys.exit(1)

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

def checkSkin(steam_dir, dpi):
    # check for skin and patch in cache
    if not (os.path.isdir(METRO_COPY) and os.path.isdir(METRO_PATCH_COPY)):
        # metro skin and patch not found in cache, download and make
        makeSkin()
    # check for patched skin in steam skin directory
    if not os.path.isdir(os.path.join(steam_dir, SKIN_NAME)):
        # patched skin not found in steam, copy it over
        print("Installing skin")
        copy_tree(METRO_COPY, os.path.join(steam_dir, SKIN_NAME))
    else:
        print("Wal Steam skin found")
        if (dpi==1):
            # skin was not found, copy it over
            print("Forcing skin install for High DPI patches")
            copy_tree(METRO_COPY, os.path.join(steam_dir, SKIN_NAME))

def makeSkin():
    # download metro for steam and extract
    print("Downloading Metro for steam")
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [{'User-Agent', 'Mozilla/5.0'}]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(METRO_URL, METRO_ZIP)
    except:
        print("Error: downloading needed skin file. Check your connection and try again.")
        sys.exit(1)

    z = zipfile.ZipFile(METRO_ZIP, 'r')
    z.extractall(METRO_DIR)
    z.close()

    # download metro for steam patch and extract
    print("Downloading Metro patch")
    try:
        urllib.request.urlretrieve(METRO_PATCH_URL, METRO_PATCH_ZIP)
    except:
        print("Error: downloading needed patch file. Check your connection and try again.")
        sys.exit(1)

    z = zipfile.ZipFile(METRO_PATCH_ZIP, 'r')
    z.extractall(METRO_PATCH_DIR)
    z.close()

    # finally apply the patch
    copy_tree(METRO_PATCH_COPY, METRO_COPY) # use copy_tree not copytree, shutil copytree is broken

def makeConfig():
    # download the config for wal_steam
    print ("Downloading config file")
    try:
        urllib.request.urlretrieve(CONFIG_URL, os.path.join(CONFIG_DIR, CONFIG_FILE))
    except:
        # problem with download
        # generate the config instead
        print("Error: downloading needed config file.")
        sys.exit(1)

def makeDpi():
    # apply the high dpi
    print ("Applying the high dpi patches")
    copy_tree(METRO_PATCH_HDPI, METRO_COPY)

def delConfig():
    # delete the config
    if os.path.isdir(CONFIG_DIR):
        shutil.rmtree(CONFIG_DIR)

def delCache():
    # delete the cache
    if os.path.isdir(CACHE_DIR):
        shutil.rmtree(CACHE_DIR)

def delSkin(steam_dir):
    # delete the skin
    if os.path.isdir(os.path.join(steam_dir, SKIN_NAME)):
        shutil.rmtree(os.path.join(steam_dir, SKIN_NAME))

def checkConfig():
    # check for the config
    if not os.path.isdir(os.path.join(HOME_DIR, ".config")):
        # make the .config folder
        os.mkdir(os.path.join(HOME_DIR, ".config"))
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

def checkCache(dpi):
    # check for the cache
    if not os.path.isdir(os.path.join(HOME_DIR, ".cache")):
        # make the .cache folder
        os.mkdir(os.path.join(HOME_DIR, ".cache"))
    if not os.path.isdir(CACHE_DIR):
        # make the cache directory
        os.mkdir(CACHE_DIR)

        # download, extract, and patch metro for steam
        makeSkin()

        # apply the dpi patches
        if (dpi==1):
            makeDpi()
    else:
        # cache folder exists
        print("Wal Steam cache found")

        # apply the dpi patches
        if (dpi==1):
            makeDpi()

def checkInstall(oSys, dpi):
    # check if the cache exists, make it if not
    checkCache(dpi)

    # check if the config file exists
    checkConfig()

    # check if the skin is installed, install it if not
    checkSkin(oSys, dpi)

def forceUpdate(oSys, dpi):
    # force update the cache and config files
    delConfig()
    delCache()
    delSkin(oSys)
    checkCache(dpi)
    checkConfig()

def getOs():
    # check if ~/.steam/steam/skins exists
    if os.path.isdir(STEAM_DIR_OTHER):
        return STEAM_DIR_OTHER
    # check if ~/.steam/skins exists
    elif os.path.isdir(STEAM_DIR_UBUNTU):
        return STEAM_DIR_UBUNTU
    # check if C:\Program Files (x86)\Steam\skins exists
    elif os.path.isdir(STEAM_DIR_WINDOWS):
        return STEAM_DIR_WINDOWS
    elif os.path.isdir(STEAM_DIR_OSX):
        return STEAM_DIR_OSX
    # close with error message otherwise
    else:
        print("Error: Steam install not found!")
        sys.exit(1)

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

    arg.add_argument("-s",
            help="Enter a custom steam skin directory.")

    arg.add_argument("-d", action="store_true",
            help="Apply high dpi patches.")

    arg.add_argument("-u", action="store_true",
            help="Force update cache, skin, and config file, WARNING WILL OVERWRITE config.json")

    return arg.parse_args()

def main():
    # set default mode to wal
    # 0 = wal
    # 1 = wpgtk
    mode = 0

    # parse the arguments
    arguments = getArgs()
    if arguments.version:
        print("Wal Steam", VERSION)
        sys.exit()

    # make sure they didn't select both wal and wpg
    if arguments.w and arguments.g:
        print("Error: You must select wpg or wal")
        sys.exit(1)

    # set the mode for either wal or wpg
    if arguments.w:
        mode = 0
    if arguments.g:
        mode = 1

    # check if user wants high-dpi support
    if arguments.d:
        dpi = 1
    if not arguments.d:
        dpi = 0

    # allow the user to enter a custom steam install location
    if arguments.s:
        oSys = arguments.s
        print("Using custom skin path: " + arguments.s)
    else:
        # check where the os installed steam
        # ~/.steam/steam/skins               - common linux install location
        # ~/.steam/skins                     - used on ubuntu and its derivatives
        # C:\Program Files (x86)\Steam\skins - used on windows
        oSys = getOs()

    # update the cache and config then exit
    if arguments.u:
        print("Force updating cache and config")
        # first remove the cache and config
        forceUpdate(oSys, dpi)
        print("Cache and config updated")
        print("Run with -w or -g to apply and re-enable wal_steam")
        sys.exit()

    # check for the cache, the skin, and get them if needed
    checkInstall(oSys, dpi)

    # get a list from either wal or wpg based on the mode
    colors = getColors(mode)

    # convert our list of colors from hex to rgb
    colors = hexToRgb(colors)

    # get a dictionary of the config settings from the config file
    variables = getConfigVar()
    walColors = getConfigColor()
    alpha = getConfigAlpha()

    # finally create a temp colors.styles and copy it in updating the skin
    setColors(colors, variables, walColors, alpha, oSys)

if __name__ == '__main__':
    main()
