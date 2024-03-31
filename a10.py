# Задание 1
# def fib(n):
#     a, b = 1, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
# for num in fib(200):
#     print(num)


# Задание 2
# def fib(n):
#     a, b = 1, 1
#     with open("fib.txt", "w") as file:
#         for _ in range(n):
#             file.write(str(a) + "\n")
#             yield a
#             a, b = b, a + b

# with open("fib.txt", "w") as file:
#     for num in fib(200):
#         print(num)
