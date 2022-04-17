import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import self as self


@dataclass
class FileInfo:
    name: str
    size: int
    content: str


class FolderInfo:
    name: str
    size: int
    folder: list

while True:
    come: str = input(' Для работы с папками? - нажми 1 \n Для работы с файлами? -  нажми 2 : ')
    if come == '1':
        print('= = Перечень команд при работе с папками = =')
        print('New - создать папку')
        print('Delete - удалить папку')
        print('List- список файлов в указанной папке')
        print('Save - сохранить')
        print('Data - информация о папке')
    elif come == '2':
        print('= = Перечень команд при работе с файлами = =')
        print('Save - сохранить')
        print('New - создать файл')
        print('Delete - удалить файл')
        print('Data - информация о файле')
    else:
        print('Выход из программы')
    manage: str = input('-- Введите требуемую команду -- ')
    if manage == 'New':
        name_new: str = input('Имя файла/папки: ')
        with open(name_new, 'w') as file:
            print('Создан')
            file.close()
    if manage == 'Delete':
        name_delete = input('Имя файла/папки: ')
        os.remove(name_delete)
    #if manage == 'Data':
       # name_data: str = input('Имя файла/папки: ')
        #with open(name_data, 'r') as file:
            #file.read(self.name_data)


