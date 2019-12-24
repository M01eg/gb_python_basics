'''
 Урок 2
 Задание 1
Создать список и заполнить его элементами различных
типов данных. Реализовать скрипт проверки типа данных
каждого элемента. Использовать функцию type() для проверки
типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
'''

def task1():
    superlist = [42, 3.14, True, "USSR", {"login": "Dragon", "password": "SecretWord123"}]

    print(isinteger(superlist[0]))
    print(isfloat(superlist[1]))
    print(isboolean(superlist[2]))
    print(isstring(superlist[3]))
    print(isdictionary(superlist[4]))

    print(isinteger(superlist[4]))
    print(isfloat(superlist[3]))
    print(isboolean(superlist[2]))
    print(isstring(superlist[1]))
    print(isdictionary(superlist[0]))



def isinteger(elem):
    return type(elem) == int

def isfloat(elem):
    return type(elem) == float

def isboolean(elem):
    return type(elem) == bool
    
def isstring(elem):
    return type(elem) == str

def isdictionary(elem):
    return type(elem) == dict


if __name__ == "__main__":
    task1()
