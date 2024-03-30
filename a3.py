# Задание 1
# from datetime import datetime # подключаем модуль datetime
# from math import sqrt # подключаем функцию sqrt из модулю math


# def main(**kwargs): # функция, которая принимает аргументы
#     for key in kwargs.items(): # проходимся циклом по кортежам ключ-значение
#         result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) # делаем вычисления 
#         print(result) # выводим результат


# if __name__ == '__main__': # точка входа
#     start_time = datetime.now() # получаем текущее время
#     main( # запускаем функцию, передаем аргументы
#         one =[10, 3],
#         two =[5, 4],
#         three =[15, 13],
#         four =[93, 53],
#         five =[133, 15],
#     )

#     time_costs = datetime.now() - start_time # расчет затраченного времени

#     print(f"Время выполнения программы - {time_costs}") # выводим время выполнения программы

# Задание 2
# from random import randint

# def dice():
#     rand = randint(1,6)
#     print(f"Выпало {rand}")

#     if rand >=5:
#         print("Вы победили")
#     elif rand >=3:
#         print("Бросаем кубик еще раз...")
#         dice()
#     else:
#         print("Вы проиграли")

# if __name__ == '__main__': 
#     dice()

# Задание 3
# from datetime import datetime
# from time import sleep

# for _ in range(5):
#     print("Текущее время:",datetime.now().time())
#     sleep(1)


# Задание 4
# from random import randint
# def av(*args):
#     for arg in args:
#         print(f"значение: {arg}")
#     return sum(args) / len(args)
    
# if __name__ == '__main__':
#     args = [randint(0, 100) for _ in range(int(input("Введите кол-во аргументов: ")))]
#     print("Среднее арифметическое: ", av(*args))

# Задание 5
import a3_1

if __name__ == '__main__':
    a = float(input("Сторона a: "))
    b = float(input("Сторона b: "))
    c = float(input("Сторона c: "))

    s = a3_1.area(a, b, c)

    print(f"Площадь треугольника: {s}")
