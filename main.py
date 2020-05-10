class Animal:
    name = ''
    weight = 0
    feed_status = False
    voice = ''

    def feed(self):
        self.feed_status = True

    def talk(self):
        print(f'{self.name} говорит {self.voice}')


class Goose(Animal):
    egg_status = False
    voice = 'Га-га-га'

    def collect_eggs(self):
        self.egg_status = False
        self.talk()


class Cow(Animal):
    milk_status = False  # доили или нет
    voice = 'Му-му'

    def milk(self):
        self.milk_status = True
        self.talk()


class Sheep(Animal):
    shear_status = False # стригли или нет
    voice = 'Ме-е-е'

    def shear(self):
        self.shear_status = True
        self.talk()


class Chicken(Animal):
    egg_status = True
    voice = 'Пок-пок-пок, куда-ах!'

    def collect_eggs(self):
        self.egg_status = False
        self.talk()


class Goat(Animal):
    milk_status = False  # доили или нет
    voice = 'Ме-е!'

    def milk(self):
        self.milk_status = True
        self.talk()


class Duck(Animal):
    egg_status = False
    voice = 'Кря-кря'

    def collect_eggs(self):
        self.egg_status = True
        self.talk()


def print_every_animal():
    for animal in animals:
        print(f'{animal.__class__.__name__} {animal.name}')


def print_feed_status():
    for animal in animals:
        if not animal.feed_status:
            print(f'{animal.name} хочет есть!')
        else:
            print(f'{animal.name} не хочет есть!')


def feed_hungry_anumals():
    for animal in animals:
        animal.feed()
        animal.talk()


def milk_animals():
    if not cow.milk_status:
        print('Доим корову.')
        cow.milk()
    else:
        print('Корову уже подоили.')

    if not goat1.milk_status and not goat2.milk_status:
        print('Доим коз.')
        goat1.milk()
        goat2.milk()
    elif goat1.milk_status and not goat2.milk_status:
            print(f'Доим козу {goat2.name}, козу {goat1.name} уже доили.')
            goat2.milk()
    elif not goat1.milk_status and goat2.milk_status:
            print(f'Доим козу {goat1.name}, козу {goat2.name} уже доили.')
            goat1.milk()
    else:
        print('Коз уже подоили.')


def collect_all_eggs():
    if not chicken1.egg_status and not chicken2.egg_status:
        print('Собираем яйца у куриц.')
        chicken1.collect_eggs()
        chicken2.collect_eggs()
    elif chicken1.egg_status and not chicken2.egg_status:
            print(f'Собираем яйца у {chicken2.name}, у курицы {chicken1.name} уже собрали!')
            chicken2.collect_eggs()
    elif chicken1.egg_status and not chicken2.egg_status:
            print(f'Собираем яйца у {chicken1.name}, у курицы {chicken2.name} уже собрали!')
            chicken1.collect_eggs()
    else:
        print('Яйца у куриц уже собраны.')

    if not duck.egg_status:
        print('Собираем яйца у утки.')
        duck.collect_eggs()
    else:
        print('Яйца у утки уже собраны.')

    print('У гусей нет яиц, ведь они не гусыни.')


def shear_sheeps():
    if not sheep1.shear_status and not sheep2.shear_status:
        print('Стрижем овец.')
        sheep1.shear()
        sheep2.shear()
    elif sheep1.shear_status and not sheep2.shear_status:
        print(f'Стрижем овцу {sheep2.name}, овца {sheep1.name} уже подстрижена!')
        sheep2.shear()
    elif not sheep1.shear_status and sheep2.shear_status:
        print(f'Стрижем овцу {sheep1.name}, овца {sheep2.name} уже подстрижена!')
        sheep1.shear()
    else:
        print('Овцы уже подстрижены.')


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

    feed_hungry_anumals()
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

    print('Посчитаем суммарный вес всех животных и определим, какое животное имеет самый большой вес.')
    print()
    print(f'Суммарный вес животных: {calculate_sum_weight(animals)}')
    print()
    print(f'Самое тяжёлое животное - {calculate_heaviest_animal(animals)[0]} {calculate_heaviest_animal(animals)[1]}')


goose1 = Goose()  # Серый
goose1.name = 'Серый'
goose1.weight = 7
goose1.sex = 'male'

goose2 = Goose()  # Белый
goose2.name = 'Белый'
goose2.weight = 8
goose2.sex = 'male'

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

chicken2 = Chicken()  # Кукареку
chicken2.name = 'Кукареку'
chicken2.weight = 4

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

main()