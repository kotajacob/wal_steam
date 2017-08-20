#.styles file format
They all use tabs to indent

The first line seems to define what the file relates to. An example of this can be seen in colors.styles, which is included in settings.styles, so it has "settings.styles" on the first line (this is mostly speculation, I will update it once I know for sure)

After this, any other files that are to be included are defined. This is done by entering 'include "file"' inside the first set of brackets

After that, there is a word defining what is inside the next set of brackets. From what info I have gathered, it can be either 'styles' or 'colors'. If any other words are entered here, the ui gets very messed up.

Finally, there is another set of brackets inside the first set, which houses the main part of the code.
 
