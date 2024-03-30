# Задание 1
# user = input("Введите последовательность чисел через пробел: ")

# numbers = user.split()

# u_list = list(numbers)
# u_tulpe = tuple(numbers)

# print(f"Список: {u_list}")
# print(f"Кортеж: {u_tulpe}")

# Задание 2
# def rm(tlp, val):
#     if val in tlp:
#         el_index = int(tlp.index(val))
#         new_tulpe = tlp[:el_index] + tlp[el_index+1:]
#         return new_tulpe
#     else:
#         return tlp


# print(rm((1, 2, 3), 1))
# print(rm((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3) )
# print(rm((2, 4, 6, 6, 4, 2), 9))

# Задание 3
# from random import randint

# s = ''.join(str(randint(0, 9)) for _ in range(16))
# print(s)
# def ct(s):
#     n_dict = {}
#     for el in s:
#         n_dict[int(el)] = s.count(el)

#     n_dict = sorted(n_dict.items(), key=lambda x: x[1], reverse=True)
#     print(dict(n_dict))
#     print(dict(sorted(n_dict[:3])))

# ct(s)

# Задание 4
# def empl(tlp, id):
#     if id in tlp: 
#         start = tlp.index(id) 
        
#         if tlp.count(id) > 1:
#             end = tlp.index(id, start + 1) 
#         else:
#             end = len(tlp)
#         return tlp[start:end + 1]

#     else:
#         return ()


# print(empl((1,2,3), 8))
# print(empl((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(empl((1,2,8, 5, 1, 2, 9), 8))


# Задание 5
# from random import randint

# numbers = [[randint(0, 99) for _ in range(5)] for _ in range(5)]

# print("Матрица: ")
# for el in numbers:
#     print(el)
# print("\nМинимальное значение в матрице: ", min(sorted(min(numbers))))
# print("Минимальное значение в матрице: ", max(sorted(max(numbers))))
 