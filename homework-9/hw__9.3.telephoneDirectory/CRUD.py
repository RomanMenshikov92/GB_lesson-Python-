import csv
import os.path
import log as lg


db_file_name = ''
db = []
global_id = 0


def init_data_base(file_name):
    global global_id
    global db
    global db_file_name

    directory = '../Семинары/homework-9/hw__9.3.telephoneDirectory'
    filename = 'db_telDir.csv'
    file_name = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)

    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if (row[0] != 'ID'):
                    db.append(row)
                    if (int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='', encoding='utf-8').close()


def create(name='', surname='', number='', description=''):
    global global_id
    global db
    global db_file_name
    if (name == ''):
        print("Безымянно и некорректно!")
        return
    if (surname == ''):
        print("Безымянно и некорректно!")
        return
    if (number == ''):
        print("Безымянно и некорректно!")
        return
    if (description == ''):
        print("Безымянно и некорректно!")
        return

    for row in db:
        if (row[1] == name.title() and row[2] == surname.title() and row[3] == number and row[4] == description.lower()):
            print("Уже есть")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
               surname.title(), number, description.lower()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


def retrive(id='', name='', surname='', number='', description=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if (name != '' and row[1] != name.title()):
            continue
        if (surname != '' and row[2] != surname.title()):
            continue
        if (number != '' and row[3] != number):
            continue
        if (description != '' and row[3] != description.lower()):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result


def update(id='', new_name='', new_surname='', new_number='', new_email=''):
    global global_id
    global db
    global db_file_name
    if (id == ''):
        print('Укажите идентификатор для обновления')
        return
    with open(db_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if (row[0] == id):
                if (new_name != ''):
                    row[1] = new_name.title()

                if (new_surname != ''):
                    row[2] = new_surname.title()

                if (new_number != ''):
                    row[3] = new_number

                if (new_email != ''):
                    row[3] = new_email.lower()

            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if (id == ''):
        print('укажите идентификатор для удаления')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)
