import csv
import _tkinter


def __init__(file1, file2):
    #file names
    change_sea= file1
    change_temp= file2

def get_year_sea():
    with open( "Mean_change_sea_levels.csv", 'r') as sea_file:
        sea_reader = csv.reader(sea_file)
        next(sea_reader)  # Skip header
        sea_data = {rows[0]: float(rows[12]) for rows in sea_reader}
    return sea_data

def get_year_temp():
    with open(change_temp, 'r') as temp_file:
        temp_reader = csv.reader(temp_file)
        next(temp_reader)  # Skip header
        temp_data = {rows[0]: float(rows[1]) for rows in temp_reader}
    return temp_data 


def get_country():
    with open(change_sea, 'r') as sea_file:
        sea_reader = csv.reader(sea_file)
        next(sea_reader)  # Skip header
        countries = [rows[0] for rows in sea_reader]
    return countries


def get_increase_temp():
    with open(change_sea, 'r') as sea_file:
        sea_reader = csv.reader(sea_file)
        next(sea_reader)  # Skip header
        sea_data = {rows[0]: float(rows[1]) for rows in sea_reader}
    return sea_data


def get_increase_sea():

    with open(change_temp, 'r') as temp_file:
        temp_reader = csv.reader(temp_file)
        next(temp_reader)  # Skip header
        temp_data = {rows[0]: float(rows[1]) for rows in temp_reader}
    return temp_data

# call functions
__init__('sea_level_change.csv', 'temperature_change.csv')

get_year_sea()