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

#streamlit.dataframe(my_fruit_list)
# Let's Create Some User Interaction
# We'll add a user interactive widget called a Multi-select that will allow users to pick the fruits they want in their smoothies.

# Let's put a pick list here so they can pick the fruit they want to include 

# The picker works, but the numbers don't make any sense! We want the customer to be able to choose the fruits by name!!
#  Choose the Fruit Name Column as the Index

my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
