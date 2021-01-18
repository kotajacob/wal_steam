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
=== Copyright (C) 2019  Dakota Walsh ===
"""
import shutil                             # copying files
import os                                 # getting paths
import urllib.request                     # downloading the zip files
import zipfile                            # extracting the zip files
import sys
import argparse                           # argument parsing
import textwrap
import time
import re
from distutils.dir_util import copy_tree  # copytree from shutil is broken so use copy_tree
from argparse import RawTextHelpFormatter

# set some variables for the file locations
HOME_DIR          = os.getenv("HOME", os.getenv("USERPROFILE")) # should be crossplatform
CACHE_DIR         = os.path.join(HOME_DIR, ".cache", "wal_steam")
CONFIG_DIR        = os.path.join(HOME_DIR, ".config", "wal_steam")
SKIN_VERSION      = "4.4"
SKIN_NAME         = "Metro %s Wal_Mod" % SKIN_VERSION
VERSION           = "1.4"
CONFIG_FILE       = "wal_steam.conf"
COLORS_FILE       = os.path.join(CACHE_DIR, "custom.styles")
CONFIG_URL        = "https://raw.githubusercontent.com/kotajacob/wal_steam_config/master/wal_steam.conf"

STEAM_DIR_OTHER   = os.path.expanduser("~/.steam/steam/skins")
STEAM_DIR_OSX     = os.path.expanduser("~/Library/Application Support/Steam/Steam.AppBundle/Steam/Contents/MacOS/skins")
STEAM_DIR_UBUNTU  = os.path.expanduser("~/.steam/skins")
STEAM_DIR_WINDOWS = "C:\Program Files (x86)\Steam\skins"
WAL_COLORS        = os.path.join(HOME_DIR, ".cache", "wal", "colors.css")
WPG_COLORS        = os.path.join(HOME_DIR, ".config", "wpg", "formats", "colors.css")

METRO_URL                 = "https://github.com/minischetti/metro-for-steam/archive/v%s.zip" % SKIN_VERSION
METRO_ZIP                 = os.path.join(CACHE_DIR, "metroZip.zip")
METRO_DIR                 = os.path.join(CACHE_DIR, "metro-for-steam-%s" % SKIN_VERSION)
METRO_COLORS_FILE         = os.path.join(METRO_DIR, "custom.styles")

METRO_PATCH_URL  = "https://github.com/redsigma/UPMetroSkin/archive/9.1.12.zip" # A link to the version we've tested rather than the latest, just in case they break things upstream.
METRO_PATCH_ZIP  = os.path.join(CACHE_DIR, "metroPatchZip.zip")
METRO_PATCH_DIR  = os.path.join(CACHE_DIR, "metroPatchZip")
METRO_PATCH_COPY = os.path.join(METRO_PATCH_DIR, "UPMetroSkin-9.1.12", "Unofficial 4.x Patch", "Main Files [Install First]")
METRO_PATCH_HDPI = os.path.join(METRO_PATCH_DIR, "UPMetroSkin-9.1.12", "Unofficial 4.x Patch", "Extras", "High DPI", "Increased fonts", "Install")
MAX_PATCH_DL_ATTEMPTS = 5

# CLI colour and style sequences
CLI_RED    = "\033[91m"
CLI_YELLOW = "\033[93m"
CLI_BOLD   = "\033[1m"
CLI_END    = "\033[0m"

def tupToPrint(tup):
    tmp = ' '.join(map(str, tup)) # convert the tupple (rgb color) to a string ready to print
    return tmp

def setCustomStyles(colors, variables, walColors, alpha, steam_dir, fonts = []):
    print ("Patching new colors")

    # delete the old colors file if present in cache
    try:
        os.remove(COLORS_FILE) # just in case it was already there for some reason
    except FileNotFoundError:
        print("No file to remove")

    with open(METRO_COLORS_FILE) as f:
        custom_styles = f.read()

    patches = []
    ii = 0
    for ii, i in enumerate(variables):
        patches.append(
            '{}="{} {}"'.format(i, tupToPrint(colors[int(walColors[ii])]), alpha[ii])
        )

    wal_styles = "\n".join(patches)
    custom_styles = custom_styles.replace(
        "}\n\nstyles{", wal_styles + "}\n\nstyles{")

    if fonts:
        custom_styles = replaceFonts(custom_styles, fonts)

    with open(COLORS_FILE, "w") as f:
        f.write(custom_styles)

    # now copy it to the proper place based on the os
    shutil.copy(COLORS_FILE, os.path.join(steam_dir, SKIN_NAME))

    # cleanup by removing generated color files
    os.remove(COLORS_FILE)
    print(
        "Wal colors are now patched and ready to go\n"
        "If this is your first run you may have to\n"
        "enable Metro Wal Mod skin in steam then\n"
        "simply restart steam!"
    )


def replaceFonts(styles, fonts):
    print("Patching custom fonts")

    # attempt to replace font styles with regular expressions
    matches = {
        "^basefont=\"(.+?)\"": "basefont=\"" + fonts[0] + "\"",
        "^semibold=\"(.+?)\"": "semibold=\"" + fonts[1] + "\"",
        "^semilight=\"(.+?)\"": "semilight=\"" + fonts[2] + "\"",
        "^light=\"(.+?)\"": "light=\"" + fonts[3] + "\"",
    }

    for pattern, replacement in matches.items():
        styles = re.sub(pattern, replacement, styles, 0, re.M)

    return styles

###################
# color functions #
###################
def getConfigAlpha():
    # read the config file and return a dictionary of the variables and color variables
    with open(os.path.join(CONFIG_DIR, CONFIG_FILE)) as f:
        # save the lines of the config file to rawFile
        rawFile = f.readlines()

    # loop through rawFile
    result = []
    for line in rawFile:
        tmpResult = line[line.find(",")+1:line.find("\n")]
        result.append(tmpResult)
    return result

def getConfigColor():
    # read the config file and return a dictionary of the variables and color variables
    with open(os.path.join(CONFIG_DIR, CONFIG_FILE)) as f:
        # save the lines of the config file to rawFile
        rawFile = f.readlines()

    # loop through rawFile
    result = []
    for line in rawFile:
        tmpResult = line[line.find("=")+1:line.find(",")]
        result.append(tmpResult)
    return result

def getConfigVar():
    # read the config file and return a dictionary of the variables and color variables
    with open(os.path.join(CONFIG_DIR, CONFIG_FILE)) as f:
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
        with open(colorsFile) as f:
            rawFile = f.readlines()  # save the lines to rawFile
    except:
        print("Error: Colors file missing. Make sure you've run pywal/wpg before wal_steam")
        sys.exit(1)

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

    return colors

##########################
# checkInstall functions #
##########################

def checkSkin(steam_dir, dpi):
    # check for skin and patch in cache
    if not (os.path.isdir(METRO_DIR) and os.path.isdir(METRO_PATCH_COPY)):
        # metro skin and patch not found in cache, download and make
        makeSkin()
    # check for patched skin in steam skin directory
    if not os.path.isdir(os.path.join(steam_dir, SKIN_NAME)):
        # patched skin not found in steam, copy it over
        print("Installing skin")
        copy_tree(METRO_DIR, os.path.join(steam_dir, SKIN_NAME))
    else:
        print("Wal Steam skin found")
        if (dpi==1):
            # skin was not found, copy it over
            print("Forcing skin install for High DPI patches")
            copy_tree(METRO_DIR, os.path.join(steam_dir, SKIN_NAME))

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

    with zipfile.ZipFile(METRO_ZIP, 'r') as z:
        z.extractall(CACHE_DIR)

    # download metro for steam patch and extract
    print("Attempting to download Metro patch")
    patch_dl_attempts = 0
    patch_dld = False
    while (patch_dl_attempts < MAX_PATCH_DL_ATTEMPTS) and not patch_dld:
        try:
            opener = urllib.request.build_opener()
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(METRO_PATCH_URL, METRO_PATCH_ZIP)
            patch_dld = True
        except:
            patch_dl_attempts += 1
            print("Error: download attempt " + str(patch_dl_attempts) + " failed.")
            if patch_dl_attempts < MAX_PATCH_DL_ATTEMPTS:
                time.sleep(5)

    if not patch_dld:
        print("Error: patch download attempts failed, exiting...")
        sys.exit(1)
    else:
        print("Patch downloaded, proceeding...")

    with zipfile.ZipFile(METRO_PATCH_ZIP, 'r') as z:
        z.extractall(METRO_PATCH_DIR)

    # finally apply the patch
    copy_tree(METRO_PATCH_COPY, METRO_DIR) # use copy_tree not copytree, shutil copytree is broken

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
    copy_tree(METRO_PATCH_HDPI, METRO_DIR)

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

def parseFontArgs(rawArgs):
    splitArgs = [arg.strip() for arg in rawArgs.split(",")]

    if len(splitArgs) != 4:
        print("Error: You must specify all four custom font styles.")
        sys.exit(1)

    return splitArgs

def getArgs():
    # get the arguments with argparse
    description = "Wal Steam"
    arg = argparse.ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)

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
        help=f"Force update cache, skin, and config file. {CLI_RED}WARNING:{CLI_END} WILL OVERWRITE config.json")

    arg.add_argument("-f", "--fonts", nargs='+',
        help=textwrap.dedent(f'''
            Specify custom fonts. Enter font styles separated by comma.
            {CLI_BOLD}Available styles:{CLI_END} basefont, semibold, semilight, light.
            {CLI_YELLOW}Example:{CLI_END} 'Open Sans, Open Sans Semibold, Open Sans Semilight, Open Sans Light'
            {CLI_RED}WARNING:{CLI_END} Fonts must already be installed on your system.'''))

    arg.add_argument("-a", "--attempts", help="Set the number of patch download attempts (DEFAULT=5)")

    return arg.parse_known_args()

def main():
    # set default mode to wal
    # 0 = wal
    # 1 = wpgtk
    mode = 0

    # parse the arguments
    arguments, unknown = getArgs()
    
    if len(unknown) != 0:
        print("Unknown arguments: {}".format(' '.join(unknown)))
    
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
        print("Using custom skin path: {}".format(arguments.s))
    else:
        # check where the os installed steam
        # ~/.steam/steam/skins               - common linux install location
        # ~/.steam/skins                     - used on ubuntu and its derivatives
        # C:\Program Files (x86)\Steam\skins - used on windows
        oSys = getOs()

    # allow the user to enter custom font styles
    if arguments.fonts:
        fonts = parseFontArgs(' '.join(arguments.fonts))
        print("Using custom font styles: {}".format(', '.join(fonts)))
    else:
        fonts = ""

    # update the cache and config then exit
    if arguments.u:
        print("Force updating cache and config")
        # first remove the cache and config
        forceUpdate(oSys, dpi)
        print("Cache and config updated")
        print("Run with -w or -g to apply and re-enable wal_steam")
        sys.exit()

    if arguments.attempts:
        try:
            attempts_bound = int(arguments.attempts)
            MAX_PATCH_DL_ATTEMPTS = attempts_bound
        except:
            print("Error setting maximum patch download attempts, using default (5).")

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
    setCustomStyles(colors, variables, walColors, alpha, oSys, fonts)

if __name__ == '__main__':
    main()
