import os
import os.path
from add_format_CSV import creatingFormatCSV
from add_format_JSON import creatingFormatJSON
from file_writing import writing_scv
from file_writing import writing_json
from file_writing import writing_txt


def clear(): return os.system('cls||clear')

directory = '../Семинары/homework-7/telephoneDirectory'
filename = 'telephone_directory.csv'
file = os.path.join(directory, filename)
if not os.path.isdir(directory):
    os.mkdir(directory)
    creatingFormatCSV()
    creatingFormatJSON()

writing_scv()
writing_json()
writing_txt()


