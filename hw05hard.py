import os
import sys
import shutil
import hw05normal

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл ")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    


do = {
    "help": hw05normal.print_help,
    "mkdir": hw05normal.make_dir,
    "ping": hw05normal.ping,
    "cp": hw05normal.copy_file,
    "rm": hw05normal.delete_file,
    "cd": hw05normal.change_dir,
    "ls": hw05normal.path_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

##try:
##    filename = sys.argv[2]
##except IndexError:
##    filename = None

try:
    getdir = sys.argv[2]
except IndexError:
    getdir = None
    
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
