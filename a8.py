# Задание 1
class Tomato:
    # словарь, содержит стадии созревания
    states = {0: "отсутсвует", 1: "цветение", 2: "зеленый", 3: "красный"}

    def __init__(self, index):
        # динамическое свойство
        self._index = index 
        # динамическое свойство
        self._state = self.states[0]
    
    # метод для созревания 
    def grow(self):
        # если не последняя стадия
        if self._state != self.states[len(self.states) - 1]: 
            # увеличиваем текущую стадию на 1
            self._state = self.states[list(self.states.values()).index(self._state)+1] 

    # метод для проверки зрелости помидора
    def is_ripe(self):
        return self._state == "красный" # если последняя стадия -> True

class TomatoBush:
    def __init__(self, count):
        # список помидоров на кусте
        self.tomatoes = [Tomato(i) for i in range(1, count + 1)]
    
    # перемодит помидора на другую стадию
    def grow_all(self):
        for t in self.tomatoes:
            t.grow()

    # проверяем все ли помидоры созрели
    def all_are_ripe(self):
        # все помидоры на кусте созрели -> True
        return all(t.is_ripe() for t in self.tomatoes)

    # очищаем куст
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # работа садовода
    def work(self):
        self._plant.grow_all()
        print("Ухаживаем за кустами...")
    
    # сбор урожая
    def harvest(self):
        # если все помидоры созрели
        if self._plant.all_are_ripe():
            print("Собираем урожай...\nУрожай собран")
        else:
            print("Урожай не созрел!")
        
    def knowledge_base(self):
        print(f"Справка по садоводу:\nИмя: {self.name}\n")
        

bush = TomatoBush(5)
gardener = Gardener("Иван", bush)
gardener.knowledge_base()

gardener.work()
gardener.work()

gardener.harvest()

gardener.work()
gardener.work()

gardener.harvest()