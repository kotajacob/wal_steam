# Colors.styles descriptions
For wal_steam, colors.styles is one of the most important files, it stores all the color variables that are used elsewhere in steam, and also controls the colors of the majority of the steam client and the ingame overlay.

## Variables
In the main part of the code, there are a bunch of variables that appear to not be used anywhere in the metro for steam directory. At this point it is unknown if these are being used anywhere, so we aren't going to touch them

## Items
This is the section that the first couple versions of wal_steam will be focusing on changing. It is located after the variables. It contains items and their color values, stored in an rgba format.

In the unnoficial patch for metro for steam, there are some 'extras' that are included. Some of these extras must be installed for some items to be colored. For instance, to have the scrollbars be a different color, you will need to install the 'accent scrollbars' extra.

# Item descriptions
Friends_InGame: The text color of a friends name while they are in a game

Friends_Online: The text color of a friends name while they are online

FrameBorder: The color of the borders at the edge of each window, also serperates the header from the rest of a window

GameList: background color of the game list on the left side of the library

Dividers: color of dividers in dropdown menus

Seperators: color of column seperators in places like the dlc information panel in the details of a game

OverlayBackground: color of the background of the in game overlay

Overlay Panels: Overlay item backgrounds (friends, guides, etc...)

OverlayClock: color of clock in the overlay

OverlaySideButtons: Color of buttons on the right side of the overlay (web browser, music, settings)

OverlaysideButtons_h: Color of buttons described above when you hover the mouse over them

TextEntry: Background color of any text box in the steam client (filter games, search friends, chat windoww)

Scrollbar: Scrollbar color (only works if you have 'accent scrollbar' extra installed

Header_Dark: Color of window header

ClientBG: Main background color of the client, it also controlls the background color of any categories in the game list
