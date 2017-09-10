# `wal_steam`

A little program that themes the colors for Metro for steam from `wal`or `wpg`. Now with HiDPI support!

![1](https://ptpb.pw/l9Rw.png)

## About

`wal_steam` is a tiny program that is meant to work with either `wal` or `wpgtk`, by reading the colors they generate and making a color theme for a slightly tweaked version of Metro for Steam.

[Wal](https://github.com/dylanaraps/pywal) is a little program for linux that creates a terminal color scheme based on your wallpaper (in addition to being able to set the wallpaper and a few other 
interesting features).

[Wpgtk](https://github.com/deviantfero/wpgtk) is based on wal, but with the added feature of being able to generate gtk themes with the colors and bring a nice simple ui to wal.

[Metro for steam](http://metroforsteam.com/) is a very nice looking skin for steam. We also add the [community patch](https://steamcommunity.com/groups/metroforsteam/discussions/0/527273789693410879/) which makes the skin render well on linux.

## Install

**Note for Windows users:** You're going to need to install [python 3](https://www.python.org/) then [imagemagick](https://www.imagemagick.org/script/download.php) first. Then search for command prompt, right click it and open as administrator, then run the pip command below but without the sudo part.

### Packages

**Python PIP:** `sudo pip3 install wal-steam`

**Arch Linux AUR:** `pacaur -S python-wal-steam-git`

### Manual

**Pre-install:** Make sure [Wal](https://github.com/dylanaraps/pywal) or [Wpgtk](https://github.com/deviantfero/wpgtk) is installed and working.

**Install:** `git clone https://github.com/kotajacob/wal_steam.git`

**Post-install:** See the "Using" section of this readme.

## Using

**Make sure you've run wal or wpgk at least once to generate the colors and set the wallpaper.**

**Note:** On some distros, notably **Ubuntu** you'll have to run the command python3 instead of python or you'll have an error about failing to import urllib.request. Additionally, OSx users may   need to use the system certificate store (outlined [here](https://stackoverflow.com/questions/41691327/ssl-sslerror-ssl-certificate-verify-failed-certificate-verify-failed-ssl-c)).

If you cloned the repo all you need to do is run the script with python 3 from wherever you downloaded it.

Example:

`wal-steam -w`

```
Usage:
  wal_steam.py (-w | -g | -u) [-d]
  wal_steam.py ( -s ) ["/home/kota/bin/custom_steam_install/skins/"]
  wal_steam.py (-h | --help)
  wal_steam.py (-v | --version)

Options:
  -h --help            show this help message and exit
  -v --version         show version and exit
  -w                   use wal for colors
  -g                   use wpg for colors
  -u                   force update cache and config file
  -d                   apply HiDPI community patch
  -s "/steam/skins"    specify a custom steam skins folder to use
```

## Screenshots

![2](https://ptpb.pw/kw6D.png)

![3](https://ptpb.pw/zhFg.png)

![4](https://ptpb.pw/xOo1.png)
