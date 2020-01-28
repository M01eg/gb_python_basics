'''
 Урок 6
 Задание 2
Реализовать класс Road (дорога), в котором определить
атрибуты: length (длина), width (ширина). Значения
данных атрибутов должны передаваться при создании
экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна. Использовать
формулу: длинаширинамасса асфальта для покрытия одного
кв метра дороги асфальтом, толщиной в 1 см*число см
толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''

class Road:
    ASPHALT_MASS = 25
    ASPHALT_THICKNESS = 5

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calculate_mass(self):
        return (self._width * self._length *
                self.ASPHALT_MASS * self.ASPHALT_THICKNESS) / 1000


def task2():
    main_road = Road(20, 5000)
    print( "Для покрытия всего дорожного полотна "
          f"понадобится {main_road.calculate_mass()} т асфальта")


if __name__ == "__main__":
    task2()
