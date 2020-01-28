'''
 Урок 6
 Задание 4
Реализуйте базовый класс Car. У данного класса должны
быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self, direction):
        print("Машина повернула %s" %(direction)) #налево/направо
    def show_speed(self):
        print("Текущая скорость: %s км/ч" % (self.speed))

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    def show_speed(self):
        if (self.speed > 60):
            print("Внимание! Скорость превышена на %s км/ч" % (self.speed - 60))
        super().show_speed()

class SportCar(Car):
    def __init__(self, speed, color, name, has_spoiler):
        super().__init__(speed, color, name, False)
        self.has_spoiler = has_spoiler

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    def show_speed(self):
        if (self.speed > 40):
            print("Внимание! Скорость превышена на %s км/ч" % (self.speed - 40))
        super().show_speed()

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

def task4():
    ivanov_car = TownCar(70, "Серый", "Иванов")
    print("\nГородская машина Иванова:")
    ivanov_car.go()
    ivanov_car.turn("налево")
    ivanov_car.turn("направо")
    ivanov_car.show_speed()
    ivanov_car.stop()

    petrov_car = SportCar(70, "Красный", "Петров", True)
    print("\nСпорткар Петрова:")
    petrov_car.go()
    petrov_car.turn("налево")
    petrov_car.show_speed()
    petrov_car.stop()


if __name__ == "__main__":
    task4()
