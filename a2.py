# Тема 3

# Задание 1
# res = 1
# for _ in range(2):
#     res *= 5
#     res += 1
# print(res)


# Задание 2
# t = "Hello World"
# for i in range(len(t) - 1, -1, -1):
#     print(t[i])

# Задание 3
# num = int(input("Введите число от 0 до 10: "))
# if num >= 0 and num <= 10:
#     if num <= 3:
#         print("Число в диапазоне от 0 до 3.")
#     elif num <= 6:
#         print("Число в диапазоне от 4 до 6.")
#     else:
#         print("Число в диапазоне от 6 до 10.")
# else:
#     print("Не правильно!")


# Задание 4
# text = input("Введите предложение на английском языке: ").lower()
# print(len(text))
# print(text)
# print(f"Кол-во гласных a, e, i, o, u:" , text.count("a") + text.count("e") + text.count("i") + text.count("i") + text.count("o") + text.count("u"))
# if "ugly" in text:
#     print(text.replace("ugly", "beauty"))

# if text[0:3] == "the":
#     print("Предложение начинается на 'The'")
# if text[len(text)-3:len(text)] == "end":
#     print("Предложение заканчивается на 'end'")


# Задание 5

string = 'hello'
memory = ' world'
values = [0, 2, 4, 6, 8, 10]
counter = 0

while counter != 10:
    
    if counter in values:
        print(string + memory)
        print(string)
    counter += 1
string = string + ' world'
memory = string
print(memory)

