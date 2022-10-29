def information():
    record = []
    last_name = input('Фамилия: ')
    record.append(last_name)
    first_name = input('Имя: ')
    record.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Телефон: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    record.append(phone_number)
    description = input('Описание: ')
    record.append(description)
    return record
