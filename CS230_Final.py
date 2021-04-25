"""
Name:       George Sekas
CS230:      Section SN1
Data:       "Used cars for sale on Craigslist"
Video:      Link to your presentation video
Summary:

This program is comprised for three different sections.

The first section is composed of a pie chart set up.
The pie chart allows the user to see what percentage of used cars have a specific quality.
The three qualities available to break down the data are drivetrain, car size, and transmission type.
The data is graphed using the value count method.
Additionally, the user can spin the pie chart.

The second section breaks down more data through a bar chart.
The user is able to graph four separate queries including: "Top 10 Most Expensive Cars", "Top 10 Least Expensive Cars",
"Top 10 Cars with The Most Mileage", "Top 10 Cars with The Least Mileage".
This data is obtained through using the sort method.
The user is also able to select the color of the graph and the color of the text.

The third and final section of this code is a word cloud displaying car manufacturers.
A list is created using the manufacturers column and a frequency function gets the dictionary needed to make the cloud.
Depending on what manufacturers are most prominent, determines the size of their name in the word cloud.
The word cloud has set formatting values to align with the pages color scheme and format.
To display the cloud, the user must press a button.


"""

import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
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


# Pie Chart Set Up

def pie(values, labels, angle, title, pie_colors):
    plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=angle, colors=pie_colors)
    plt.title(title)
    plt.legend(loc="best", labels=labels)
    return plt


# Bar Chart Set Up

# Selection of Valid Data
validPrice = df[df["price"] > 1]
validMile = df[df["odometer"] > 1]

# top 10 most expensive cars
top_10_price = validPrice.sort_values(by='price', ascending=False)[:10]

# bottom 10 least expensive cars
bottom_10_price = validPrice.sort_values(by='price', ascending=True)[:10]
# print(bottom_10_price[["model", "price"]])

# top 10 most miles on car
top_10_miles = validMile.sort_values(by='odometer', ascending=False)[:10]

# bottom 10 miles on car
bottom_10_miles = validMile.sort_values(by='odometer', ascending=True)[:10]


def bar_top_price(chart_color):
    plt.clf()  # clears plt to prevent pie chart overlap
    x = []
    for cars in top_10_price["model"].values:
        x.append(cars)
    plt.bar(top_10_price["model"], top_10_price["price"], align="center", alpha=0.5, color=chart_color)
    plt.title("Top 10 Most Expensive Cars")
    plt.xlabel("Models", color=chart_color)
    plt.ylabel("Prices ($)", color=chart_color)
    plt.xticks(x, rotation=65)
    plt.tight_layout()
    return plt


def bar_bottom_price(chart_color):
    plt.clf() # clears plt to prevent pie chart overlap
    x = []
    x_values = bottom_10_price["model"].astype(str)
    for cars in x_values:
        x.append(cars)
    # y = []
    # y_values = bottom_10_price["price"].astype(str)
    # for prices in y_values:
    #     y.append(prices)
    plt.bar(x, bottom_10_price["price"], align="center", alpha=0.5, color=chart_color)
    plt.title("Top 10 Least Expensive Cars")
    plt.xlabel("Models", color=chart_color)
    plt.ylabel("Prices ($)", color=chart_color)
    plt.xticks(x, rotation=65)
    plt.tight_layout()
    return plt


def bar_top_mile(chart_color):
    plt.clf() # clears plt to prevent pie chart overlap
    x = []
    for cars in top_10_miles["model"].values:
        x.append(cars)
    # y = []
    # for miles in top_10_miles["odometer"].values:
    #     y.append(miles)
    plt.bar(top_10_miles["model"], top_10_miles["odometer"], align="center", alpha=0.5, color=chart_color)
    plt.title("Top 10 Cars with The Most Mileage")
    plt.xlabel("Models", color=chart_color)
    plt.ylabel("Mileage (Millions)", color=chart_color)
    plt.xticks(x, rotation=65)
    plt.tight_layout()
    return plt


def bar_bottom_mile(chart_color):
    plt.clf() # clears plt to prevent pie chart overlap
    x = []
    x_values = bottom_10_miles["model"].astype(str)
    for cars in x_values:
        x.append(cars)
    plt.bar(x, bottom_10_miles["odometer"], align="center", alpha=0.5, color=chart_color)
    plt.title("Top 10 Cars with The Least Mileage")
    plt.xlabel("Models", color=chart_color)
    plt.ylabel("Mileage", color=chart_color)
    plt.xticks(x, rotation=65)
    plt.tight_layout()
    return plt


# Word Cloud Set-Up

# create a list of car manufacturers
def manufacturer_list():
    manufacturers = []
    for make in df["manufacturer"].values:
        manufacturers.append(make)
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
    font_fname = path.join(DIR, "HighlandGothicFLF.ttf")
    mask_fname = np.array(Image.open(path.join(DIR, "star.png")))

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
    st.title("CS 230 Final Project")
    st.header("By George Sekas")
    st.subheader("Dataset Used - Used Cars on Craigslist")

    # First Image Display
    img1 = Image.open("img1.jpg")
    st.image(img1, width=750)
    st.text("Image from Slashgear.com")
    # image citation:
    # https://www.slashgear.com/lamborghini-aventador-svj-roadster-first-drive-review-770hp-convertible-beast-01604760/

    # Pie Chart - with options
    st.header("Pie Chart")
    st.subheader("Total Car Analysis on: Drivetrain | Transmission | Car Size")

    # Graphing Selection for Pie Chart
    st.subheader("What Do You Want To Graph?")
    pie_chart_selection = st.selectbox("Pie Chart Options", ("drive",
                                                             "transmission",
                                                             "size"))

    # Start Angle Set with Slider for Pie Chart
    st.subheader("Spin The Chart")
    angle = st.slider("Spin!", 45, 90, 180)

    # Data Set Up
    column = df[pie_chart_selection].value_counts()
    labels = []
    for i in column.index:
        labels.append(i)
    values = []
    for i in column.values:
        values.append(i)

    # Colors for Pie Chart which vary between Data
    drive_color = ["springgreen", "darkolivegreen", "yellow"]  # 3 colors
    transmission_color = ["lightcoral", "orangered", "saddlebrown"]  # 3 colors
    size_color = ["midnightblue", "aqua", "blueviolet", "dodgerblue"]  # 4 colors

    # Display Pie Chart
    if pie_chart_selection == "drive":
        st.pyplot(pie(values, labels, angle, title="Drivetrain", pie_colors=drive_color))
    elif pie_chart_selection == "transmission":
        st.pyplot(pie(values, labels, angle, title="Transmission", pie_colors=transmission_color))
    elif pie_chart_selection == "size":
        st.pyplot(pie(values, labels, angle, title="Car Size", pie_colors=size_color))

    # Bar Chart - with options
    st.header("Bar Chart - Pricing/Mileage")

    # Graphing Selection for Bar Chart
    st.subheader("What Do You Want To Graph?")
    bar_chart_selection = st.selectbox("Bar Chart Options", ("Top 10 Most Expensive Cars",
                                                             "Top 10 Least Expensive Cars",
                                                             "Top 10 Cars with The Most Mileage",
                                                             "Top 10 Cars with The Least Mileage"))

    # Color Selection for Bar Chart
    colors = {"Orange Red": "orangered", "Lime": "lime", "Dark Orange": "darkorange",
              "Deep Sky Blue": "deepskyblue", "Dark Violet": "darkviolet"}
    color_names = list(colors.keys())
    st.subheader("Pick a Color")
    chart_color = st.radio('Color:', color_names)

    # Display Bar Chart
    if bar_chart_selection == "Top 10 Most Expensive Cars":
        st.pyplot(bar_top_price(colors[chart_color]))
    elif bar_chart_selection == "Top 10 Least Expensive Cars":
        st.pyplot(bar_bottom_price(colors[chart_color]))
    elif bar_chart_selection == "Top 10 Cars with The Most Mileage":
        st.pyplot(bar_top_mile(colors[chart_color]))
    elif bar_chart_selection == "Top 10 Cars with The Least Mileage":
        st.pyplot(bar_bottom_mile(colors[chart_color]))

    # Word Cloud

    # Create Word Cloud
    wc = create_cloud()

    # Button to Display Word Cloud
    if st.button("Click for something cool."):
        st.image(wc.to_array())

    # Second Image Display
    img2 = Image.open("img2.jpg")
    st.image(img2, width=750)
    st.text("Image from Slashgear.com")
    # image citation:
    # https://www.slashgear.com/lamborghini-aventador-svj-roadster-first-drive-review-770hp-convertible-beast-01604760/


main()
