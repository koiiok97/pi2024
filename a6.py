# Задание 1
# with open("text.txt", "r") as file:
#     words = file.read().split()

# words_count = {}
# for key in words:
#     if key not in words_count:
#         words_count[key] = 1
#     else:
#         words_count[key] += 1

# mx_word = sorted(words_count.items(),key=lambda x: x[1], reverse=True)[0]

# print("Количество слов в тексте: ",len(words))
# print(f"Часто встречающееся слово: {mx_word[0]}, встречается {mx_word[1]} раз")

# Задание 2
# with open("expenses.txt", "a") as file:
#     while True:
#         try:
#             n = input("наименование: ")
            
#             if "done" in n :
#                 break
#             v = int(input("расход: "))

#             file.write(f"{n} - {v} \n")
#         except:
#             print("error")

# print("\nВаши расходы: ")
# with open("expenses.txt", "r") as file:
#         print(file.read())

# Задание 3
# with open('input.txt', 'r') as file:
#     text = file.read()


#     let = sum(1 for e in text if e.isalpha())
#     words = len(text.split())
#     lines = text.count("\n") + 1

#     print(f"{let} letters")
#     print(f"{words} words")
#     print(f"{lines} lines")


# Задание 4
# user = input("Введите текст: ").lower()

# with open("input2.txt", "r") as file: 
#     ban_words = file.read().split()

# words = user.split()
# for i, word  in enumerate(words):
#     for ban_word in ban_words:
#         if ban_word in word:
#             new_word = ""
#             for c in word:
#                 if c in ban_word:
#                     new_word += "*"
#                 else:
#                     new_word += c

#             words[i] = new_word
            
# res = ' '.join(words)
# print(user,"\n")
# print(res)

# Задание 5
# from random import randint
# with open("temperatures.txt", "w") as file:
#     for _ in range(10):
#         file.write(str(randint(10, 30)) + " ")

# with open("temperatures.txt", "r") as file:
#     numbers = file.read().split()

#     print("Множества: " + ' '.join(numbers))

#     numbers = [int(e) for e in numbers]
#     print(f"Среднее значение: {sum(numbers) / len(numbers)}" )
