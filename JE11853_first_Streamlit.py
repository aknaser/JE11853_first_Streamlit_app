import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner!')

streamlit.header('Breakfast Menu')
streamlit.subheader('Breakfast Favorites:')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

## We want pandas to read our CSV file from that S3 bucket so we use a pandas function called read_csv  to pull the data into a dataframe we'll call my_fruit_list. 
# Remember the S3 Bucket from DWW? 
# We're going to use a CSV file from that bucket in our app. 
# The file is here: https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
