import telebot

import CRUD as cr
import log as lg

bot = telebot.TeleBot('5471399302:AAEWyQQTPKqPEpxhTqGVOukmOGzfiMAwic4')


@bot.message_handler(content_types=['sticker', 'pinned_message', 'photo', 'audio', 'video'])
def warning(message):
    bot.send_message(
        message.chat.id, f'Некорректно. Обратитесь: /help.')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'Привет, *{message.from_user.first_name} {message.from_user.last_name}!*\nГлавное меню: /main\nПомощь: /help\n')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, f'Начать сначала: /start\nГлавное меню: /main\nПомощь: /help')


name_it = ''
surname_it = ''
number_it = ''
description = ''
user_id_it = ''
new_number_it = ''


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == '/main':
        bot.send_message(message.chat.id, f'Ваш пункт в меню: \n/1 - Полная информация в записи.\n/2 - Нахождение номера по фамилии.\n/3 - Нахождение номера по имени.\n/4 - Поиск по номеру телефона.\n/5 - Добавление новой записи.\n/6 - Изменение имеющей записи.\n/7 - Удаление записи.\n/8 - Выход.')
        cr.init_data_base('telephoneDirectory.csv')

    elif message.text == '/1':
        lg.logging.info('The user has selected item number 1')
        bot.send_message(message.chat.id, f'{cr.retrive()}')

    elif message.text == '/2':
        lg.logging.info('The user has selected item number 2')
        bot.send_message(message.chat.id, f'Ввод фамилии')
        bot.register_next_step_handler(message, find_surname)

    elif message.text == '/3':
        lg.logging.info('The user has selected item number 3')
        bot.send_message(message.chat.id, f'Ввод имени')
        bot.register_next_step_handler(message, find_name)

    elif message.text == '/4':
        lg.logging.info('The user has selected item number 4')
        bot.send_message(message.chat.id, f'Ввод номера телефона')
        bot.register_next_step_handler(message, find_number)

    elif message.text == '/5':
        lg.logging.info('The user has selected item number 5')
        bot.send_message(message.chat.id, f'Ввод имени')
        bot.register_next_step_handler(message, get_name)

    elif message.text == '/6':
        lg.logging.info('The user has selected item number 6')
        bot.send_message(
            message.chat.id, f'Какой контакт хотите изменить?\nУкажите по:\n/61 - Фамилии\n/62 - Имени\n/63 - Номеру телефона')
        bot.register_next_step_handler(message, edit_entry)

    elif message.text == '/7':
        lg.logging.info('The user has selected item number 7')
        bot.send_message(
            message.chat.id, f'Выберите контакт, который хотите удалить?\nВыберите по:\n/71 - Фамилии\n/72 - Имени\n/73 - Номеру телефона')
        bot.register_next_step_handler(message, delete_contact)
    elif message.text == '/8':
        lg.logging.info('The user has selected item number 8')
        bot.send_message(
            message.chat.id, f'До свидания')
        bot.register_next_step_handler(message, exit())

    else:
        bot.send_message(
            message.chat.id, f'Некорректно. Обратитесь: /help.')


def find_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(surname=surname_it)}')


def find_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(name=name_it)}')


def find_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(number=number_it)}')


def get_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'Ввод фамилии')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'Ввод номера телефона')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'Ввод описания')
    bot.register_next_step_handler(message, get_email)


def get_email(message):
    global description
    description = message.text
    lg.logging.info('User entered: {description}')
    cr.create(name_it, surname_it, number_it, description)
    bot.send_message(message.chat.id, f'Добавлен новый контакт')


def edit_entry(message):
    if message.text == '/61':
        lg.logging.info('The user has selected item number 6.1')
        bot.send_message(message.chat.id, f'Ввод фамилии')
        bot.register_next_step_handler(message, change_surname)

    elif message.text == '/62':
        lg.logging.info('The user has selected item number 6.2')
        bot.send_message(message.chat.id, f'Ввод имени')
        bot.register_next_step_handler(message, change_name)

    elif message.text == '/63':
        lg.logging.info('The user has selected item number 6.3')
        bot.send_message(message.chat.id, f'Ввод номера телефона')
        bot.register_next_step_handler(message, change_num)

    else:
        bot.send_message(
            message.chat.id, f'Некорректно. Обратитесь: /help.')


def change_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(name=name_it)}')
    bot.send_message(
        message.chat.id, f'Ввод № записи для изменения')
    bot.register_next_step_handler(message, change_number)


def change_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(surname=surname_it)}')
    bot.send_message(
        message.chat.id, f'Ввод № записи для изменения')
    bot.register_next_step_handler(message, change_number)


def change_num(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(number=number_it)}')
    bot.send_message(
        message.chat.id, f'Ввод № записи для изменения')
    bot.register_next_step_handler(message, change_number)


def change_number(message):
    global user_id_it
    user_id_it = message.text
    lg.logging.info('User entered: {user_id_it}')
    bot.send_message(
        message.chat.id, f'Ввод нового номера телефона')
    bot.register_next_step_handler(message, change_new_number)


def change_new_number(message):
    global new_number_it
    new_number_it = message.text
    lg.logging.info('User entered: {new_number_it}')
    cr.update(id=user_id_it, new_number=new_number_it)
    bot.send_message(
        message.chat.id, f'Изменен имеющий контакт')


def delete_contact(message):
    if message.text == '/71':
        lg.logging.info('The user has selected item number 7.1')
        bot.send_message(message.chat.id, f'Ввод фамилии')
        bot.register_next_step_handler(message, delete_surname)

    elif message.text == '/72':
        lg.logging.info('The user has selected item number 7.2')
        bot.send_message(message.chat.id, f'Ввод имени')
        bot.register_next_step_handler(message, delete_name)

    elif message.text == '/73':
        lg.logging.info('The user has selected item number 7.3')
        bot.send_message(message.chat.id, f'Ввод номера телефона')
        bot.register_next_step_handler(message, delete_num)

    else:
        bot.send_message(
            message.chat.id, f'Некорректно. Обратитесь: /help.')


def delete_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(surname=surname_it)}')
    bot.send_message(
        message.chat.id, f'Ввод № записи для удаления')
    bot.register_next_step_handler(message, delete_number)


def delete_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(name=name_it)}')
    bot.send_message(
        message.chat.id, f'Ввод № записи для удаления')
    bot.register_next_step_handler(message, delete_number)


def delete_num(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(number=number_it)}')
    bot.send_message(
        message.chat.id, f'Ввод № записи для удаления')
    bot.register_next_step_handler(message, delete_number)


def delete_number(message):
    global user_id_it
    user_id_it = message.text
    lg.logging.info('User entered: {user_id_it}')
    cr.delete(id=user_id_it)
    bot.send_message(
        message.chat.id, f'Удален выбранный контакт')


print('\nserver start')
print('\nТелефонный справочник')
bot.infinity_polling()
