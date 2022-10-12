import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

theme = 'DarkTeal10'

# Set the theme for the application 
sg.theme(theme)

# Some test data 
# TODO Replace this data with data from the CSV
test_years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
test_prices = [15, 17, 19, 20, 16, 19, 22, 40, 45]

# Set some initial conditions  
graph_flag = 0
window_flag = 0
district_name = 'Kyiv'

# Read the data from the CSV folder of "Ukrainian_food" and store in a variable that will not be altered 
food_data_frame = pd.read_csv('Ukrainian_food.csv', low_memory=False, skiprows=[2])