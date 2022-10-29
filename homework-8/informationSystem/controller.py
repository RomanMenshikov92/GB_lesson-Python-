from sort import sort,get_list
from user_view import operation,data
from file_write import writing_scv
from file_read import read_scv
from main import sort_data

def button():
    return sort_data(operation, read_scv, writing_scv, sort, get_list, data)