import os
from dataclasses import dataclass
from typing import Any

infile: str = input(' Для работы с папками? - нажми 1 \n Для работы с файлами? -  нажми 2 : ')
incomand: str = input('-- Введите требуемую команду -- ')
name_new: str = input('Имя файла/папки: ')
name_delete: str = input('Имя файла/папки: ')


@dataclass
class FileInfo:
    name: str
    size: int
    content: str

@dataclass
class FolderInfo:
    name: str
    size: int
    content: str

class FileManager(object):
    def __init__(self: Any):
        pass

        while True:

            if infile == '1':
                print('= = Перечень команд при работе с папками = =')
                print('New - создать папку')
                print('Delete - удалить папку')
            elif infile == '2':
                print('= = Перечень команд при работе с файлами = =')
                print('New - создать файл')
                print('Delete - удалить файл')

            else:
                print('Выход из программы')

    def open_file(self: Any):
        if incomand == 'New':
            with open(self.open_file, 'w') as file:
                print('Создан')
                file.close()

    def delete_file(self):
        if incomand == 'Delete':
            os.remove()

#if __name__ == '__main__':
#    print(info)