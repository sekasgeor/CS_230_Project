"""
Name:       George Sekas
CS230:      Section SN1
Data:       "Used cars for sale on Craigslist"
Video:      Link to your presentation video
Summary:

This program queries the data to .... (a few sentences about your program)

"""

import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import pandas as pd
import pydeck as pdk
from os import path
from PIL import Image
import numpy as np
import os
from wordcloud import WordCloud


# data file setup
# read in datafile
datafile = "usedcardata.csv"
df = pd.read_csv(datafile)

# drop columns used drop method
df.drop(['Unnamed: 0', 'id', 'url', 'region_url', 'image_url'], inplace=True, axis=1)
# print(df.dtypes)
# print(df)


# word cloud set up

# create a list of car manufacturers

def manufacturer_list():
    manufacturers = []
    for make in df["manufacturer"].values:
        manufacturers.append(make)
    print(manufacturers)
    return manufacturers


def get_freq():
    # Call list of manufacturers
    manufacturers = manufacturer_list()

    # Creates a dictionary dict_freq containing each unique word and the number of times it appears in the file
    dict_freq = {}
    unique_words = []
    for make in manufacturers:
        # Uses helper.clean() to remove any punctuation found in each word
        if make not in unique_words:
            unique_words.append(make)
    for unique_word in unique_words:
        freq = 0
        for make in manufacturers:
            if unique_word == make:
                freq += 1
        dict_freq[unique_word] = freq

    # Returns dict_freq
    return dict_freq


def create_cloud():

    # Sets up variables containing the file names (with paths) for the font, text file, and mask
    DIR = os.getcwd()
    font_fname = path.join(DIR, "fonts", "HighlandGothicFLF.ttf")
    mask_fname = np.array(Image.open(path.join(DIR, "masks", "star.png")))

    wc = WordCloud(background_color="black",
                   font_path=font_fname,
                   mask=mask_fname,
                   colormap="viridis",
                   contour_width=5,
                   contour_color='lime')

    # Calls get_freq()to get a dictionary of words and their frequencies
    dict_of_manufacturers = get_freq()

    # calls WordCloud() and wc.generate_from_frequencies() (from the WordCloud
    # module you imported) to generate the word cloud
    wc = wc.generate_from_frequencies(dict_of_manufacturers)

    return wc



def main():

    img = Image.open("img1.jpg")

    st.image(img, width=300)
    st.title("Craigslist Car Marketplace Analysis")

    st.header("Chart 1")

    wc = create_cloud()
    #
    # if st.button("Click for something cool."):
    #     st.image(wc.to_array())

    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()


main()
