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

def parseCss():
    print("Parsing CSS ")

def getWpg():
    print("Getting WPG")
    f_name = open('test.css', 'r')
    parseCss()
    f_name.close()

def getWal():
    print("Getting WAL")
    f_name = open('test.css', 'r')
    parseCss()
    f_name.close()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Wal Steam 0.1.0') # create the flags from the comment

    if (arguments['--help']==False and arguments['--version']==False): # determine which option was selected
        if (arguments['-g']==True):
            print("OPTION G WOO!")
            getWpg()
        else:
            print("OPTION W WOO!") 
            getWal()
