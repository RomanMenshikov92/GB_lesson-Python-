from user_input import information as info
import os.path

record = info()


def writing_scv():
    directory = '../Семинары/homework-7/telephoneDirectory'
    filename = 'telephone_directory.csv'
    file = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{record[0]};{record[1]};{record[2]};{record[3]}\n')


def writing_json():
    directory = '../Семинары/homework-7/telephoneDirectory'
    filename = 'telephone_directory.json'
    file = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{record[0]};{record[1]};{record[2]};{record[3]}\n')


def writing_txt():
    directory = '../Семинары/homework-7/telephoneDirectory'
    filename = 'telephone_directory.txt'
    file = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Фамилия: {record[0]}\nИмя: {record[1]}\nТелефон: {record[2]}\nОписание: {record[3]}\n\n')
