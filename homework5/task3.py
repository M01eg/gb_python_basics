'''
 Урок 5
 Задание 3
Создать текстовый файл (не программно), построчно
записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

def task3():
    n_employees = 0
    salary_overall = 0
    with open("test3.txt", encoding="utf-8") as f:
        print(f"Оклад менее 20000 рублей у следующих сотрудников: ")
        for line in f:
            name, salary = line.split()
            salary = int(salary)
            if salary < 20000:
                print(name)
            # Добавляем в счетчики
            n_employees += 1
            salary_overall += salary

    print(f"Средняя зарплата по компании: {salary_overall/n_employees}")


if __name__ == "__main__":
    task3()
