"""
Helping Functions
"""

from PIL import Image, ImageColor

FONTS = {"highland": "HighlandGothicFLF.ttf",
         "alpaca": "Alpaca Solidify.ttf",
         "bebas": "BebasNeue-Regular.ttf",
         "crayons": "Colored Crayons.ttf",
         "junegull" : "JuneGull.ttf",
         "prata" : "Prata-Regular.ttf"
      }

MASKS = {"square": "square.png",
         "fish": "fish.png",
         "snowman": "snowman.png",
         "star": "star.png",
         "clover" : "clover.png"
      }

#  **************************************************************
#   Selection Functions with Data Validation
#  **************************************************************
def default_input(prompt, default_value):
    """
    If the user presses Enter, use the default value
    """
    item = input(prompt + "[Enter for " + default_value + "]: ").lower()
    if item == "":
        item = default_value
    return item



def font_select():

    print("Available Fonts:")
    print(*FONTS.keys())

    font = default_input("Select a font. ","highland")

    while font not in FONTS.keys():
        font = default_input("Error. Select a font. ","highland")

    return font

def mask_select():

    print("Available masks:")
    print(*MASKS.keys())
    mask = default_input("Select a mask: ", "square")

    while mask not in MASKS.keys():
        mask = default_input("Error. Select a mask: ", "square")
    return mask

def bg_color_select():
    color = default_input("Enter a web color name for the background.",
                          "white")
    while color not in ImageColor.colormap.keys():
        color = default_input("Error. Enter a web color name for the background.",
                          "white")
    return color

def color_map_select():
    # choose several color maps from https://matplotlib.org/stable/tutorials/colors/colormaps.html

    COLOR_MAPS= ['autumn', 'cool', 'copper', 'flag', 'hot','inferno', 'ocean', 'prism',
                 'rainbow','spring', 'summer',  'twilight', 'winter']
    print ("Select a color scheme for the text: ")
    print (*COLOR_MAPS)
    color_map = default_input("Enter a color map for the text. ", "prism")

    while color_map not in COLOR_MAPS:
        color_map = default_input("Error. Enter a color map for the text. ", "prism")
    return color_map

# *********************************************************************
#  remove special characters from a word
# *********************************************************************

def clean(w):
    """
    remove special characters
    """
    PUNC = ".,:;!?"
    SYMBOLS = "-()\/[]<>{}!@#_$%^&*\'\""
    for sym in SYMBOLS:
       w = w.replace(sym,"")

    if w != "":
        if w[-1] in PUNC:
            w = w[:-1]
    return w
