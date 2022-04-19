import os


while True:
    _infile: str = input(' Для работы с папками? - нажми 1 \n Для работы с файлами? -  нажми 2 :')
    if _infile == '1':
        print('= = Перечень команд при работе с папками = =')
        print('New - создать папку')
        print('Delete - удалить папку')
        print('List- список файлов в указанной папке')
        print('Save - сохранить')
        print('Data - информация о папке')
    elif _infile == '2':
        print('= = Перечень команд при работе с файлами = =')
        print('Save - сохранить')
        print('New - создать файл')
        print('Delete - удалить файл')
        print('Data - информация о файле')
    else:
        print('Выход из программы')
    _incomand: str = input('-- Введите требуемую команду -- ')
    if _incomand == 'New':
        name_new: str = input('Имя файла/папки: ')
        with open(name_new, 'w') as file:
            print('Создан')
            file.close()
    if _incomand == 'Delete':
        name_delete = input('Имя файла/папки: ')
        os.remove(name_delete)
