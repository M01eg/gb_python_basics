'''
 Урок 3
 Задание 2
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год
рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def get_user_presentation(surname, name, birth_year, city_of_residence, email, phone):
    print(f"Пользователя зовут {name} {surname}. Он родился в {birth_year} " +
          f"году и в данный момент проживает в городе {city_of_residence}. " +
          f"Связаться с ним можно по телефону {phone} или по e-mail: {email}.")

def task2():
    entered_surname = input("Введите фамилию: ")
    entered_name = input("Введите имя: ")
    entered_birth_year = input("Введите год рождения: ")
    entered_city_of_residence = input("Введите город проживания: ")
    entered_email = input("Введите e-mail: ")
    entered_phone = input("Введите телефон: ")

    get_user_presentation(surname=entered_surname,
                          name=entered_name,
                          birth_year=entered_birth_year,
                          city_of_residence=entered_city_of_residence,
                          email=entered_email,
                          phone=entered_phone)

if __name__ == "__main__":
    task2()
