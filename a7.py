# Задание 1
# class Ball:
#     pass

# ball_1 = Ball()
# print(ball_1)

# Задание 2
# class Ball:
#     def __init__(self, size = 10, color = "red", material = None):
#         self.size = size
#         self.color = color
#         self.material = material

#     def change_size(self, size):
#         self.size = size
    
#     def change_color(self, color):
#         self.color = color
    
#     def change_material(self, material):
#         self.material = material

# ball_1 = Ball()

# print(f"Ball 1:\nsize: {ball_1.size}; color: {ball_1.color}; material: {ball_1.material}")
# ball_1.change_color("pink")
# ball_1.change_size(20)
# ball_1.change_material("wood")

# print(f"\nchange Ball 1:\nsize: {ball_1.size}; color: {ball_1.color}; material: {ball_1.material}")

# Задание 3
# class Ball:
#     def __init__(self, size = 10, color = "red", material = None):
#         self.size = size
#         self.color = color
#         self.material = material

#     def change_size(self, size):
#         self.size = size
    
#     def change_color(self, color):
#         self.color = color
    
#     def change_material(self, material):
#         self.material = material

# class Football(Ball):
#     pass

# ball_1 = Ball()
# print(f"Ball 1:\nsize: {ball_1.size}; color: {ball_1.color}; material: {ball_1.material}\n")

# ball_2 = Football(15, "white", "leather")
# print(f"Ball 2:\nsize: {ball_2.size}; color: {ball_2.color}; material: {ball_2.material};\n")

# Задание 4
# class Ball:
#     def __init__(self, size = 10, color = "red", material = None):
#         self.__size = size
#         self.__color = color
#         self.__material = material

#     def change_size(self, size):
#         self.__size = size
    
#     def change_color(self, color):
#         self.__color = color
    
#     def change_material(self, material):
#         self.__material = material

#     def get_size(self):
#         return self.__size

#     def get_color(self):
#         return self.__color
    
#     def get_material(self):
#         return self.__material


# class Football(Ball):
#     pass

# ball_1 = Ball()
# print(f"Ball 1:\nsize: {ball_1.get_size()}; color: {ball_1.get_color()}; material: {ball_1.get_material()}\n")

# ball_2 = Football(15, "white", "leather")
# print(f"Ball 2:\nsize: {ball_2.get_size()}; color: {ball_2.get_color()}; material: {ball_2.get_material()};\n")



#  Задание 5

# class Ball:
#     def __init__(self, size = 10, color = "red", material = None):
#         self.__size = size
#         self.__color = color
#         self.__material = material

#     def change_size(self, size):
#         self.__size = size
    
#     def change_color(self, color):
#         self.__color = color
    
#     def change_material(self, material):
#         self.__material = material

#     def get_size(self):
#         return self.__size

#     def get_color(self):
#         return self.__color
    
#     def get_material(self):
#         return self.__material

#     def bounce(self):
#         print("Bouncing...")

# class Football(Ball):
#     def bounce(self):
#         print("Football bouncing...")

# ball_1 = Ball()
# ball_1.bounce()
# print(f"Ball 1:\nsize: {ball_1.get_size()}; color: {ball_1.get_color()}; material: {ball_1.get_material()}\n")

# ball_2 = Football(15, "white", "leather")
# ball_2.bounce()
# print(f"Ball 2:\nsize: {ball_2.get_size()}; color: {ball_2.get_color()}; material: {ball_2.get_material()};\n")
