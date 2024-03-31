# Задание 1
# import time

# def calc_time(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()

#         res = end - start
#         print(f"\nВремя выполнения: {res} секунд!" )
#         return func
    
#     return wrapper

# @calc_time
# def fibonacci():
#     fib1 = fib2 = 1

#     for _ in range(2, 200):
#         fib1, fib2 = fib2, fib1 + fib2
#         print(fib2, end=" ")


# if __name__ == "__main__":
#     fibonacci()

# Задание 2
# try:
#     with open("f2.txt", "r") as file:
#         data = file.read()
        
#         if not data:
#             raise Exception("файл пустой")
        
#         print(f"Информация из файла:\n{data}")
        
# except Exception as e:
#     print("Ошибка:", e)


# Задание 3
# def sumNumbers():
#     try:
#         num = float(input("Введите число: "))
        
#         print("Результат сложения:", num + 2)
        
#     except ValueError:
#         print("Ошибка: Неподходящий тип данных. Ожидалось число.")

# sumNumbers()


# Задание 4 
# class Log:
#     def __init__(self, func):
#         self.func = func
    
#     def __call__(self, *args, **kwds):
#         print(f"Аргументы: {args}")
#         res = self.func(*args, **kwds)
#         print("Результат: ", res)

#         return res

# @Log
# def sumNum(*args):
#     res = sum(args)
#     return res
# @Log
# def mult(*args):
#     res = 1
#     for n in args:
#         res *= n
#     return res

# sumNum(2,3,5)
# mult(2, 5, 12, 4, 5)


# Задание 5

# class MyException(Exception):
#     def __init__(self, mes):
#         self.mes = mes


# try:
#     user = float(input("Введите положительно число: "))

#     if user < 0:
#         raise MyException("Число не соотвествует условию")
#     else:
#         print(f"Верно! Введено число: {user}")

# except Exception as e:
#     print("Ошибка:", e)