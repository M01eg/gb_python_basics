''' Еще не доделано((
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
        print("Машина повернула %s" %(direction))
    def show_speed(self):
        print("Текущая скорость: %s" % (self.speed))

class TownCar(Car):
    def __init__(self, speed, color, name, False, transmission_type):
        super.__init__(speed, color, name, is_police)
        self.transmission_type = transmission_type
    def show_speed(self):
        print(self.speed)

class SportCar(Car):
    def __init__(self, speed, color, name, False, has_spoiler)
        super.__init__(speed, color, name, is_police)
        self.has_spoiler = has_spoiler

class WorkCar(Car):
    def __init__(self, speed, color, name, False, company_owner)
        super.__init__(speed, color, name, is_police)
        self.company_owner = company_owner
    def show_speed(self):
        print(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name)
        super.__init__(speed, color, name, True)

def task4():
    emp_ivanov = Position("Иван", "Иванов", "Инженер", 50000, 10000)
    print("Создан класс с атрибутами:\n%s" % ([emp_ivanov.__dict__]))
    print("%s. Полный доход: %s" % (emp_ivanov.get_full_name(),
                                    emp_ivanov.get_total_income()))

    emp_petrov = Position("Петр", "Петров", "Менеджер", 40000, 15000)
    print("\nСоздан класс с атрибутами:\n%s" % ([emp_petrov.__dict__]))
    print("%s. Полный доход: %s" % (emp_petrov.get_full_name(),
                                    emp_petrov.get_total_income()))


if __name__ == "__main__":
    task4()
