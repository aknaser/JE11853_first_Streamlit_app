import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
#Dont run anytin past ere while we trouble shoot
#streamlit.stop()
#import snowflake.connector

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
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Lets Choose a Few Fruits to Set a Good Example
#We want to filter the table data based on the fruits a customer will choose, so we'll pre-populate the list to set an example for the customer. 

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# Display the table on the page.
#streamlit.dataframe(my_fruit_list)

#Now we just have to make the table below the picker a bit smarter so it's doesn't load all the fruits, just the ones shown in the pick list. 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display te Table on the page
streamlit.dataframe(fruits_to_show)

#12/01/2022: Bring in and import another Python package library. This one is called "requests"

#New section to display fruityvice api response

#create repeatable code block (called a function)
def get_fryuityvice_data(this_fruit_choice):  
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)

# Convert Unstructured data into normalized structured form 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header('Fryuityvice Fruit Advice!')

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        #streamlit.write('The user entered ', fruit_choice)
#-add_my_fruit = streamlit.text_input('What fruit would you like to Add?','jackfruit')
#-streamlit.write('The user entered ', add_my_fruit)
        #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        back_from_function = get_fryuityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
# Convert Unstructured data into normalized structured form 
        #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Normalize output data and display in tabular form
        #streamlit.dataframe(fruityvice_normalized)

except URLerror as e:
    streamlit.error()

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The Fruit Load List Contains:")
#streamlit.dataframe(my_data_rows)

#Move the Fruit Load List Query and Load into a Button Action
#streamlit.header("The Fruit Load List Contains:")
streamlit.header("View our Fruit List - Add your Favorites!")
#snowflake_related_functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()
#Add a button to load the fruit
if streamlit.button('Get Fruit List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

####
#add_my_fruit = streamlit.text_input('What fruit would you like to Add?','jackfruit')
#streamlit.write('Thanks for adding ', add_my_fruit)
#ruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
#-streamlit.text("Thanks for adding, JacKfruit")
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

#Let's Use a Function and Button to Add the Fruit Name Submissions
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('" + new_fruit +"')")
        return "Thanks for adding, " + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to Add?')
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_function)





