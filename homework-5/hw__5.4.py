# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import os
os.system('cls||clear')

print('Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.')

import os.path

def textAfterEncoding(strDecode):
    strEncode = ''
    count = 1
    symbol = strDecode[0]
    for i in range(1, len(strDecode)):
        if strDecode[i] == symbol:
            count += 1
        else:
            strEncode = strEncode + str(count) + symbol
            symbol = strDecode[i]
            count = 1
            strEncode = strEncode + str(count) + symbol
    return strEncode


def textAfterDecoding(strEncode):
    strDecode = ''
    symbol_amount = ''
    for i in range(len(strEncode)):
        if strEncode[i].isdigit():
            symbol_amount += strEncode[i]
        else:
            strDecode += strEncode[i] * int(symbol_amount)
        symbol_amount = ''
    print(strDecode)
    return strDecode

directory = './Семинары/homework-5/'
filename1 = "file_HW_5.4-Text_after_Encoding.txt"
filename2 = "file_HW_5.4-Text_after_Decoding.txt"
file_path = os.path.join(directory, filename1)
file_path_0 = os.path.join(directory, filename2)
if not os.path.isdir(directory):
    os.mkdir(directory)
with open(file_path, 'w') as data:
    data.write('TTTTTUUUUUUUUUUPPAAAAAAAAAACCCCCC')

with open(file_path, 'r') as data:
    string = data.readline()

with open(file_path, 'r') as file:
    strDecode = file.read()

with open(file_path_0, 'w') as file:
    strEncode = textAfterEncoding(strDecode)
    file.write(strEncode)

print(f'\nТекст после декодировки: {strDecode}')
print(f'\nТекст после кодирования: {textAfterEncoding(strDecode)}')
print(f'\nКоэффициент сжатия: {round(len(strDecode) / len(strEncode), 1)}\n')