# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Чередников Максим Евгеньевич
- ИНО ЗБ ПОАС 22-1

| Задание | Сам_раб |
| ------ | ------ | 
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |


знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
- Текст задания: Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
- Оформленный код: 
```python
class Ball:
    pass

ball_1 = Ball()
print(ball_1)

```
- Скрины консоли:<br> ![Меню](https://github.com/koiiok97/pi2024/blob/Tema_8/t7/1.png)


## Самостоятельная работа №2
- Текст задания: Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
- Оформленный код: 
```python
class Ball:
    def __init__(self, size = 10, color = "red", material = None):
        self.size = size
        self.color = color
        self.material = material

    def change_size(self, size):
        self.size = size
    
    def change_color(self, color):
        self.color = color
    
    def change_material(self, material):
        self.material = material

ball_1 = Ball()

print(f"Ball 1:\nsize: {ball_1.size}; color: {ball_1.color}; material: {ball_1.material}")
ball_1.change_color("pink")
ball_1.change_size(20)
ball_1.change_material("wood")

print(f"\nchange Ball 1:\nsize: {ball_1.size}; color: {ball_1.color}; material: {ball_1.material}")
```
- Скрины консоли:<br> ![Меню](https://github.com/koiiok97/pi2024/blob/Tema_8/t7/2.png)

  
## Самостоятельная работа №3
- Текст задания: Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли
- Оформленный код: 
```python
class Ball:
    def __init__(self, size = 10, color = "red", material = None):
        self.size = size
        self.color = color
        self.material = material

    def change_size(self, size):
        self.size = size
    
    def change_color(self, color):
        self.color = color
    
    def change_material(self, material):
        self.material = material

class Football(Ball):
    pass

ball_1 = Ball()
print(f"Ball 1:\nsize: {ball_1.size}; color: {ball_1.color}; material: {ball_1.material}\n")

ball_2 = Football(15, "white", "leather")
print(f"Ball 2:\nsize: {ball_2.size}; color: {ball_2.color}; material: {ball_2.material};\n")

```
- Скрины консоли:<br> ![Меню](https://github.com/koiiok97/pi2024/blob/Tema_8/t7/3.png)


## Самостоятельная работа №4
- Текст задания: Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли
- Оформленный код: 
```python
class Ball:
    def __init__(self, size = 10, color = "red", material = None):
        self.__size = size
        self.__color = color
        self.__material = material

    def change_size(self, size):
        self.__size = size
    
    def change_color(self, color):
        self.__color = color
    
    def change_material(self, material):
        self.__material = material

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color
    
    def get_material(self):
        return self.__material


class Football(Ball):
    pass

ball_1 = Ball()
print(f"Ball 1:\nsize: {ball_1.get_size()}; color: {ball_1.get_color()}; material: {ball_1.get_material()}\n")

ball_2 = Football(15, "white", "leather")
print(f"Ball 2:\nsize: {ball_2.get_size()}; color: {ball_2.get_color()}; material: {ball_2.get_material()};\n")

```
- Скрины консоли:<br> ![Меню](https://github.com/koiiok97/pi2024/blob/Tema_8/t7/4.png) 


## Самостоятельная работа №5
- Текст задания: Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
- Оформленный код: 
```python
class Ball:
    def __init__(self, size = 10, color = "red", material = None):
        self.__size = size
        self.__color = color
        self.__material = material

    def change_size(self, size):
        self.__size = size
    
    def change_color(self, color):
        self.__color = color
    
    def change_material(self, material):
        self.__material = material

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color
    
    def get_material(self):
        return self.__material

    def bounce(self):
        print("Bouncing...")

class Football(Ball):
    def bounce(self):
        print("Football bouncing...")

ball_1 = Ball()
ball_1.bounce()
print(f"Ball 1:\nsize: {ball_1.get_size()}; color: {ball_1.get_color()}; material: {ball_1.get_material()}\n")

ball_2 = Football(15, "white", "leather")
ball_2.bounce()
print(f"Ball 2:\nsize: {ball_2.get_size()}; color: {ball_2.get_color()}; material: {ball_2.get_material()};\n")

```

- Скрины консоли:<br> ![Меню](https://github.com/koiiok97/pi2024/blob/Tema_8/t7/5.png)


