# Задание 1
# checks = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666, 5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928, 5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]
# checks.sort()
# vis = []
# for elem in checks:
#     if elem not in vis:
#         vis.append(elem)

# vis2 = {}
# for elem in checks:
#     vis2[elem] = vis2.get(elem, 0) + 1
# print(vis2)
# mx_c = 0
# mx_vis = 0
# for key, value in vis2.items():
#     if value > mx_c:
#         mx_c = value
#         mx_vis = key

# print(mx_vis)

# print(f"\nВыдано чеков: {len(checks)}")
# print(f"Кол-во разных людей посетивших ресторан: {len(vis)}")
# print(f"Болше всех посетил ресторан: {mx_vis} - {mx_c} раз")


# Задание 2
# res = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
# res.sort()

# print(f"Три лучших результата: {res[:3]}")
# print(f'Три худших результата: {res[-3:]}')
# print(f"Все результаты начиная с 10: {res[10:]}")

# Задание 3
# from math import sqrt
# one = [12, 25, 3, 48, 71] 
# two = [5, 18, 40, 62, 98] 
# three = [4, 21, 37, 56, 84]

# one_max, one_min = max(one), min(one)
# two_max, two_min = max(two), min(two)
# three_max, three_min = max(three), min(three)

# def area(a, b, c):
#     p = (a + b + c) / 2
#     return sqrt(p * (p - a) * (p - b) * (p - c))

# print(f"Площадь треугольника из максимальных сторон: {area(one_max, two_max, three_max)}")
# print(f"Площадь треугольника из минимальных сторон: {area(one_min, two_min, three_min)}")


# Задание 4
# u1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
# u2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
# u3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
# def upd(u):
#     mass = []
#     for e in u:
#         if e == 2:
#             continue
#             # print("элемент удален")
#         elif e == 3:
#             mass.append(4)
#             # print("элемент изменен")
#         else:
#             mass.append(e)
#     return mass


# u1 = upd(u1)
# u2 = upd(u2)
# u3 = upd(u3)
# print(u1)
# print(u2)
# print(u3)

# Задание 5
# list_1 = [1, 1, 3, 3, 1]
# list_2 = [5, 5, 5, 5, 5, 5, 5]
# list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

# def create_sets(*lists):
#     for list in lists:
#         new_set = set()
#         for num in list:
#             if num not in new_set:
#                 new_set.add(num)
#             else:
#                 new_set.update([str(num) * i for i in range(2, list.count(num)+1)])
            
#     return new_set

# print(create_sets(list_1))
# print(create_sets(list_2))
# print(create_sets(list_3))