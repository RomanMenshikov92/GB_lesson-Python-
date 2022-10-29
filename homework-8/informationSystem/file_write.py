import os.path
          
def writing_scv(data):
    directory = '../Семинары/homework-8/informationSystem'
    filename = 'information system(DateBase).csv'
    file_0 = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open(file_0, 'a', encoding='utf-8') as file:
        file.write(data)
