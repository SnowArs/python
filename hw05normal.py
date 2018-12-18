import os
import sys
import shutil

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл ")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    
def make_dir():
    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def copy_file():
    try:
        filename = sys.argv[2]
    except IndexError:
        filename = None
    if not filename:
        print("Необходимо указать имя файла вторым параметром")
        print(os.listdir("."))
        return
    if os.path.isfile(filename):
        newfile = filename + '.copy'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("файл", newfile, " был успешно скопирован")
            return True
        else:
            print("возникл проблемы при копировании файла", newfile)
            return False
        
def delete_file():
    try:
        filename = sys.argv[2]
    except IndexError:
        filename = None
    if not filename:
        print("Необходимо указать имя файла для удаления вторым параметром")
        print(os.listdir("."))
        return
    if os.path.isfile(filename):
        os.remove(filename)
    if not os.path.exists(filename):
        print("файл", filename, "был удален")

def change_dir():
    try:
        getdir = sys.argv[2]
    except IndexError:
        getdir = None
    if not getdir:
        print("Необходимо указать имя дериктории вторым параметром")
        print(os.listdir("."))
        print(os.getcwd())
        return
    os.chdir(getdir)
    print("Вы перешли в директорию -", os.getcwd())

def path_dir():
    print("Полный путь к вашей директории - ", os.getcwd())
    
def ping():
    print("pong")

def create_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.mkdir(dir_path)

def delete_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.exists(dir_path):
        os.rmdir(dir_path)
    else:
        print('Такой папки не существует')

def main():
    answer = 'y' 

    while answer != 'n':	
        
        if answer == 'y' :
            print("[1] - переход в директорию")
            print("[2] - Просмотр  содержимого текущей папки")
            print("[3] - создать папку")
            print("[4] - удалить папку")
           

            do = int(input("подскажите, что бы вы хотели сделать: "))

            if do == 1:
                print(os.listdir())
                dir_name  = input("в какую папку вы хотите перейти? ")
                os.chdir(dir_name)
                print(os.listdir())
            elif do == 2:
                print("Список файлов и папок")
                print(os.listdir())

            elif do == 3:
                print(os.listdir())
                dir_name  = input("давайте создадим директорию, введите название ")
                create_dir(dir_name) 
                print(os.listdir())
                
            elif do == 4:
                print(os.listdir())
                dir_name  = input("давайте удалим директорию, введите название ")
                delete_dir(dir_name)
                print(os.listdir())
                           
        elif answer == 'n':
                print("До свидания")
                
        answer = input("Хотите поработать? (y/n) ")

if __name__ == "__main__":
    main()
