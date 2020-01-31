'''
 Урок 7
 Задание 1

Реализовать класс Matrix (матрица). Обеспечить
перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков)
для формирования матрицы.

Подсказка: матрица — система некоторых математических
величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str()
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для
реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна
быть новая матрица.
Подсказка: сложение элементов матриц выполнять
поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
'''

from abc import ABC, abstractmethod

class Clothing(ABC):
    @abstractmethod
    def calculate_material_expenses(self):
        pass

class Coat(Clothing):
    def __init__(self, name, v):
        self._name = name
        self._v = v
    def calculate_material_expenses(self):
        return self._v/6.5 + 0.5
    @property
    def coat_name(self):
        return self._name
        

class Costume(Clothing):
    def __init__(self, name, h):
        self._name = name
        self._h = h
    def calculate_material_expenses(self):
        return 2 * self._h + 0.3
    @property
    def costume_name(self):
        return self._name


def task2():
    brown_jacket = Coat("Коричневая куртка", 55)
    print(f"{brown_jacket.coat_name}...")
    material_needed = round(brown_jacket.calculate_material_expenses(), 2)
    print(f"Потребуется ткани: {material_needed} м^2")

    blue_jeans_costume = Coat("Голубой джинсовый костюм", 100)
    print(f"{blue_jeans_costume.coat_name}...")
    material_needed = round(blue_jeans_costume.calculate_material_expenses(), 2)
    print(f"Потребуется ткани: {material_needed} м^2")


if __name__ == "__main__":
    task2()
