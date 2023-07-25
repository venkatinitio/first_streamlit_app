import streamlit
import pandas

streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 and Blueberry Oat Meal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build your own smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick Some Fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# convert the json structure into a normalized table like structure with index and column names (rows and columns)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# convert the table into a dataframe
streamlit.dataframe(fruityvice_normalized)
