from sort import sort, get_dat
from view import get_action, get_data
from write_read_db import read_file, write_file
from main import sort_data

def button():
    return sort_data(get_action, read_file, write_file, sort, get_dat, get_data)
