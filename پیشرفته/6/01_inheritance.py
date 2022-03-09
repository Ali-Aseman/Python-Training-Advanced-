# inheritance: creating new class from an existing one.
# multiple inheritance
class Creature:

    def __init__(self) -> None:
        print("1")

    def whoisthis(self):
        print("2")

    def eat(self):
        print("3")


class Animal(Creature):
    species = "Animal"

    def __init__(self) -> None:
        super().__init__()
        print("4")

    def whoisthis(self):
        print("5")

    # def eat(self):
    #     print("Animal is eating.")


class EggableAnimal:

    def breed(self):
        print("6")

    def eat(self):
        print("7")


# mro - method resolution order
# left to right
class Bird(Animal, EggableAnimal):

    # class property
    # این ویژگی بین همه نمونه های یکسان است
    # peggy and ostrich and ... each of them has species and the value is the same
    species = "Bird"

    def __init__(self) -> None:
        super().__init__()
        print("8")

    def whoisthis(self):
        print("9")

    def swim(self):
        print("10")

    def fly(self):
        print("11")


class Panguin(Bird):
    # constructor
    def __init__(self) -> None:
        # super(): acess to the parent element(behaviour and properties)
        # به رفتارها و ویژگی های پدر دسترسی پیدا میکنید
        super().__init__()
        print("12")

    def whoisthis(self):
        # super().behaviour()
        super().whoisthis()
        super().swim()
        print("13")

    def run(self):
        print("14")


class Ostrich(Bird):

    def __init__(self) -> None:
        super().__init__()

    def whoisthis(self):
        # super().whoisthis()
        print("15")

    # override - fly behaviour
    def fly(self):
        print("16")


peggy = Panguin()
peggy.whoisthis()
peggy.run()
peggy.swim()
peggy.eat()
print(peggy.species)

ostrich = Ostrich()
ostrich.whoisthis()
ostrich.fly()
print(ostrich.species)
