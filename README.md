# wal_steam

A little script that themes the colors for Metro for steam from wal or wpg.

## About

Wal Steam is a tiny program that is meant to work with either wal or wpgtk, by reading the colors they generate and making a color theme for a slightly tweaked version of Metro for Steam.

[Wal](https://github.com/dylanaraps/pywal) is a little program for linux that creates a terminal color scheme based on your wallpaper (in addition to being able to set the wallpaper and a few other 
interesting features).

[Wpgtk](https://github.com/deviantfero/wpgtk) is based on wal, but with the added feature of being able to generate gtk themes with the colors and bring a nice simple ui to wal.

[Metro for steam](http://metroforsteam.com/) is a very nice looking skin for steam. We also add the [community patch](https://steamcommunity.com/groups/metroforsteam/discussions/0/527273789693410879/) which makes the skin render well on linux.

## Install

The install is very simple and if you run into any problems just submit an issue and we should be able to resolve it fairly quickly.

First install and run wal or wpgtk to set your wallpaper and color scheme.

Then install steam using your distros package manager. (On ubuntu you need to enable the multiverse and fedora you'll want to get rpm fusion)

Next simply clone the repo to a memorable location like documents.

`git clone https://github.com/kotajacob/wal_steam.git ~/Documents`

Now go in that directory and run wal_steam once so it can get the colors and theme steam.

`python wal_steam.py -w` or if you used wpgtk instead of wal `python wal_steam.py -g`

That's it, the first time you run wal steam it will download all the needed skins and patches. Then you just need to open steam, select the metro for steam wal_mod skin and restart steam to apply the theme.

**Packages:** We have an aur package [python-wal-steam-git](https://aur.archlinux.org/packages/python-wal-steam-git) Thanks to [/u/_tague on reddit.](https://www.reddit.com/user/_tague)

## Using

**Make sure you've run wal or wpgk at least once to generate the colors and set the wallpaper.**

**Note:** On some distros, notably **Ubuntu** you'll have to run the command python3 instead of python or you'll have an error about failing to import urllib.request.

Just run the script with python. Use -g for wpg or -w for wal.

Example:

`python wal_steam.py -w`

```
Usage:
  wal_steam.py (-w | -g)
  wal_steam.py (-h | --help)
  wal_steam.py (-v | --version)

Options:
  -w                   use wal for colors
  -g                   use wpg for colors
  -h --help            show this help message and exit
  -v --version         show version and exit
```

## Screenshots

![1](https://ptpb.pw/kw6D.png)

![2](https://ptpb.pw/zhFg.png)

![3](https://ptpb.pw/l9Rw.png)

![4](https://ptpb.pw/xOo1.png)

![5](https://ptpb.pw/n8jd.png)
