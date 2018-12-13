import os
import sys
import shutil

answer = 'y' 

while answer != 'n':	
    if answer == 'y' :
        print("[1] - создам 10 дирректорий")
        print("[2] - удалю 10 директорий")
        print("[3] - выведу список папок")
        print("[4] - продублирую указанный файл")
        
        do = int(input("подскажите, что бы вы хотели сделать: "))
        if do == 1:
            i = 1
            dirn = input("Введите имя директории для создания: ")
            while i < 10:
                dir_name = dirn + str(i)
                dir_path = os.path.join(os.getcwd(), dir_name)
                os.mkdir(dir_path)
                i += 1
            print(os.listdir())
        elif do == 2:
            i = 1
            dirn = input("Введите имя директории для удаления: ")
            while i < 10:
                dir_name = dirn + str(i)
                dir_path = os.path.join(os.getcwd(), dir_name)
                os.rmdir(dir_path)
                i += 1
            print(os.listdir())
        elif do == 3:
            print(os.listdir())
        elif do == 4:
            print("Создаем копию файла из списка", os.listdir())
            filename = input("введите имя файла: ")
            newfile = filename + ".dupl"
            shutil.copy(filename, newfile)
            if os.path.exists(newfile):
                print("файл", newfile, " был успешно скопирован")
            else:
                print("возникл проблемы при копировании файла", newfile)
    elif answer == 'n':
            print("До свидания")

    answer = input("Хотите поработать? (y/n) ")


