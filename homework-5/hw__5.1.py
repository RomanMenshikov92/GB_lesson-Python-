# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


import os
os.system('cls||clear')

print('Напишите программу, удаляющую из текста все слова, содержащие ""абв"".\n')

text = 'абвер забвение зимбабве незабвен самозабвенность россия москва санкт-петербург'

def delete_word(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = delete_word(text)
print(f'Выведены слова, не содержащие "абв": {text}\n')
