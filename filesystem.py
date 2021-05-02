"""
CASE: 6
Kuleshov Roman - 70%
Yudachev Nikita -30%
"""

import os


def main():
    while True:
        print(
f'''Текущая директория: {os.getcwd()}
1. Просмотр каталога
2. На уровень вверх
3. На уровень вниз
4. Количество файлов и каталогов
5. Размер текущего каталога (в байтах)
6. Поиск файла
7. Выход из программы''')
        n_command = input('Введите пункт меню:')
        command = acceptCommand(n_command)
        runCommand(command)
        if command == 7:
            print('Работа программы завершена')
            break


def acceptCommand(n_command):
    lst = ['1', '2', '3', '4', '5', '6', '7']
    while n_command not in lst:
        n_command = input('Некорректный ввод. Пожалуйста, повторите попытку')
    return int(n_command)


def runCommand(command):
    if command == 2:
        return moveUp()
    if command == 3:
        currentDir = input('Введите путь к данному каталогу:')
        return moveDown(currentDir)
    if command == 4:
        path = str(input('Введите путь к данному каталогу:'))
        print('Количество файлов и каталогов:', countFiles(path))
    if command == 5:
        path = str(input())
        print('Размер текущего каталога:', countBytes(path), '(в байтах)')
    if command == 6:
        path = str(input('Введите путь к данному каталогу:'))
        target = str(input('Введите название файла:'))
        if findFiles(target, path) == []:
            print('Файл не найден')
        else:
            print(findFiles(target, path))


def moveUp():
    os.chdir('../')


def moveDown(currentDir):
    while True:
        try:
            os.chdir(os.getcwd() + '/' + currentDir)
            break
        except FileNotFoundError:
            currentDir = input('Некорректный ввод. Введите еще раз:')
            return moveDown(currentDir)


def countFiles(path):
    k = 0
    if os.path.isdir(path):
        for i in os.listdir(path):
            if os.path.isdir(path + '/' + i):
                k += countFiles(path + '/' + i)
            else:
                k += 1
    return k


def countBytes(path):
    k = 0
    if os.path.isdir(path):
        for i in os.listdir(path):
            if os.path.isdir(path + '/' + i):
                k += countBytes(path + '/' + i)
            else:
                k += os.path.getsize(path + '/' + i)
    return k


def findFiles(target, path):
    k = []
    if os.path.isdir(path):
        for i in os.listdir(path):
            if os.path.isdir(path + '/' + i):
                k.extend(findFiles(target, path + '/' + i))
            elif target.lower() in i.lower():
                k.append(path + '/' + i)
    return k


main()
