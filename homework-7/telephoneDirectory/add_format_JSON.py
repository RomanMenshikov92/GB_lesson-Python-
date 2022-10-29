def creatingFormatJSON():
    file = 'telephone_directory.json'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')
