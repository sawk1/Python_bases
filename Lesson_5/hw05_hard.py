# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <dir_name> - меняет текущую директорию на одну из внутренних
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# ИСПОЛЬЗОВАТЬ МОДУЛИ SYS, OS, SHUTIL

# python with_args.py param1 param2 param3
import os
import sys
import shutil
#print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('ping - тестовый ключ')


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def copy_scrypt():
    file_path = os.path.join(os.getcwd(), dir_name)
    print (file_path)
    file_name=file_path.split('/')[-1:][0][0:len(file_path.split('/')[-1:][0])-3]
    newfile=file_name+'(copy).py'
    shutil.copy(file_path,newfile)

def remove_file():
    file_path = os.path.join(os.getcwd(), dir_name)
    approval = input('вы уверены? y/n ')
    if approval == 'y' or 'Y':
        os.remove(file_path)
    else:
        exit()

def change_directory():
    file_path = os.path.join(os.getcwd(), dir_name)
    os.chdir(file_path)
    print (file_path)

def ls():
    print (os.getcwd())


def ping():
    print("pong")

do = { 'cp': copy_scrypt,
       'rm':remove_file,
       'cd': change_directory,
       'ls':ls,
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
