'''
 Урок 5
 Задание 2
Создать текстовый файл (не программно), сохранить в нем
несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

def task2():
    file_contents = open("test2.txt").read()

    n_lines = file_contents.count("\n")
    print(f"Количество строк в файле: {n_lines}\n========")

    for i, line in enumerate(file_contents.splitlines()):
        n_words = len(line.split())
        print(f"Количество слов в строке {i+1}: {n_words}")


if __name__ == "__main__":
    task2()
