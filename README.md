# `wal_steam`

A little program that themes the colors for Metro for steam from `wal`or `wpg`. Now with windows support!

![1](https://ptpb.pw/l9Rw.png)

## About

`wal_steam` is a tiny program that is meant to work with either `wal` or `wpgtk`, by reading the colors they generate and making a color theme for a slightly tweaked version of Metro for Steam.

[Wal](https://github.com/dylanaraps/pywal) is a little program for linux that creates a terminal color scheme based on your wallpaper (in addition to being able to set the wallpaper and a few other 
interesting features).

[Wpgtk](https://github.com/deviantfero/wpgtk) is based on wal, but with the added feature of being able to generate gtk themes with the colors and bring a nice simple ui to wal.

[Metro for steam](http://metroforsteam.com/) is a very nice looking skin for steam. We also add the [community patch](https://steamcommunity.com/groups/metroforsteam/discussions/0/527273789693410879/) which makes the skin render well on linux.

## Install

### Packages

**Arch Linux AUR:** `python-wal-steam-git`

### Manual

**Pre-install:** Make sure [Wal](https://github.com/dylanaraps/pywal) or [Wpgtk](https://github.com/deviantfero/wpgtk) is installed and working.

**Install:** `git clone https://github.com/kotajacob/wal_steam.git`

**Post-install:** See the "Using" section of this readme.

## Using

**Make sure you've run wal or wpgk at least once to generate the colors and set the wallpaper.**

**Note:** On some distros, notably **Ubuntu** you'll have to run the command python3 instead of python or you'll have an error about failing to import urllib.request.

If you cloned the repo all you need to do is run the script with python 3 from wherever you downloaded it.

Example:

`python wal_steam.py -w`

```
Usage:
  wal_steam.py (-w | -g)
  wal_steam.py ( -s ) ["/home/kota/bin/custom_steam_install/skins/"]
  wal_steam.py (-h | --help)
  wal_steam.py (-v | --version)

Options:
  -h --help            show this help message and exit
  -v --version         show version and exit
  -w                   use wal for colors
  -g                   use wpg for colors
  -u                   force update cache and config file
  -s "/steam/skins"    specify a custom steam skins folder to use
```

## Screenshots

![2](https://ptpb.pw/kw6D.png)

![3](https://ptpb.pw/zhFg.png)

![4](https://ptpb.pw/xOo1.png)

![5](https://ptpb.pw/43pZ.png)

![6](https://ptpb.pw/JRcw.png)

![7](https://ptpb.pw/z4Kr.png)
