class Animal:
    name = ''
    weight = 0
    feed_status = False  # кормили или нет
    voice = ''

    def feed(self):
        self.feed_status = True

    def talk(self):
        print(f'{self.name} говорит {self.voice}')


class DairyAnimal(Animal):
    milk_status = False  # доили или нет

    def milk(self):
        self.milk_status = True
        self.talk()


class WoolAnimal(Animal):
    shear_status = False  # стригли или нет

    def shear(self):
        self.shear_status = True
        self.talk()


class EggAnimal(Animal):
    egg_status = False  # собрали яйца, или нет

    def collect_eggs(self):
        self.egg_status = True
        self.talk()

class Cow(DairyAnimal):
    voice = 'Му-му'


class Goat(DairyAnimal):
    voice = 'Ме-е!'


class Sheep(WoolAnimal):
    voice = 'Ме-е-е'


class Goose(EggAnimal):
    voice = 'Га-га-га'


class Chicken(EggAnimal):
    voice = 'Пок-пок-пок, куда-ах!'


class Duck(EggAnimal):
    voice = 'Кря-кря'


def print_every_animal():
    for animal in animals:
        print(f'{animal.__class__.__name__} {animal.name}')


def print_feed_status():
    for animal in animals:
        if not animal.feed_status:
            print(f'{animal.name} хочет есть!')
        else:
            print(f'{animal.name} не хочет есть!')


def feed_hungry_animals():
    for animal in animals:
        if not animal.feed_status:
            print(f'Покормили {animal.name}.')
            animal.feed()
            animal.talk()


def milk_animals():
    print('Начинаем доить животных.')
    for animal in dairy_animals:
        if not animal.milk_status:
            animal.milk()
            print(f'Подоили {animal.name}.')
        else:
            print(f'{animal.name} уже доили.')


def collect_all_eggs():
    print('Начинаем собирать яйца.')
    for animal in egg_animals:
        if not animal.egg_status:
            animal.collect_eggs()
            print(f'Собрали яйца у {animal.name}.')
        else:
            print(f'У {animal.name} нет яиц.')


def shear_sheeps():
    print('Начинаем стричь животных.')
    for animal in whool_animals:
        if not animal.shear_status:
            animal.shear()
            print(f'Подстригли {animal.name}.')
        else:
            print(f'{animal.name} уже подстрижен.')


def calculate_sum_weight(animals):
    sum_weight = 0
    for animal in animals:
        sum_weight += animal.weight
    return sum_weight


def calculate_heaviest_animal(animals):
    weight = 0
    name = ''
    animal_class = ''
    for animal in animals:
        if animal.weight > weight:
            weight = animal.weight
            name = animal.name
            animal_class = animal.__class__.__name__
    return animal_class, name


def main():
    print('Добро пожаловать на ферму!')
    print('Вы видите следующих животных:')
    print_every_animal()
    print()

    print_feed_status()
    print()
    print('Животные голодны! Давайте накормим их.')

    feed_hungry_animals()
    print()
    print_feed_status()
    print()
    print('Отлично!')

    print('Теперь нужно подоить корову и коз, подстричь овец, собрать яйца у кур, овец и гусей.')
    milk_animals()
    print()
    collect_all_eggs()
    print()
    shear_sheeps()
    print()

    print('Посчитаем суммарный вес всех животных и определим, какое животное имеет самый большой вес.\n')
    print(f'Суммарный вес животных: {calculate_sum_weight(animals)}\n')
    print(f'Самое тяжёлое животное - {calculate_heaviest_animal(animals)[0]} {calculate_heaviest_animal(animals)[1]}')


goose1 = Goose()  # Серый
goose1.name = 'Серый'
goose1.weight = 7
goose1.egg_status = True  # Яйца собраны

goose2 = Goose()  # Белый
goose2.name = 'Белый'
goose2.weight = 8

cow = Cow()  # Манька
cow.name = 'Манька'
cow.weight = 250

sheep1 = Sheep()  # Барашек
sheep1.name = 'Барашек'
sheep1.weight = 115

sheep2 = Sheep()  # Кудрявый
sheep2.name = 'Кудрявый'
sheep2.weight = 125

chicken1 = Chicken()  # Ко-Ко
chicken1.name = 'Ко-ко'
chicken1.weight = 3
chicken1.feed_status = True  # накормили

chicken2 = Chicken()  # Кукареку
chicken2.name = 'Кукареку'
chicken2.weight = 4
chicken2.feed_status = True  # накормили

goat1 = Goat()  # Рога
goat1.name = 'Рога'
goat1.weight = 60

goat2 = Goat()  # Копыта
goat2.name = 'Копыта'
goat2.weight = 66

duck = Duck()  # Кряква
duck.name = 'Кряква'
duck.weight = 5

animals = [goose1, goose2, cow, sheep1, sheep2, chicken1, chicken2, goat1, goat2, duck]

dairy_animals = [cow, goat1, goat2]
whool_animals = [sheep1, sheep2]
egg_animals = [goose1, goose2, chicken1, chicken2, duck]

main()