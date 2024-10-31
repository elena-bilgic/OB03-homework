class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} makes a sound")

    def eat(self):
        print(f"{self.name} eats")

class Mammal(Animal):
    def __init__(self, name, age, family):
        super().__init__(name, age)
        self.family = family

    def make_sound(self):
        print(f"{self.name} roars")

class Bird(Animal):
    def __init__(self, name, age, wings):
        super().__init__(name, age)
        self.wings = wings

    def make_sound(self):
        print(f"{self.name} tweets")

class Reptile(Animal):
    def __init__(self, name, age, eye_color):
        super().__init__(name, age)
        self.eye_color = eye_color

    def make_sound(self):
        print(f"{self.name} says Tsssssss")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

animals = [Mammal("Lion", "10", "Feline"), Bird("Sparrow", "5", "small"), Reptile("Cobra", "7", "Yellow")]
animal_sound(animals)

class Zoo():
    def add_animal(self, animal):
        print(f"{animal.name} added to the zoo")

    def add_employee(self, employee):
        print(f"{employee.name} added to the zoo staff")

class Employee():
    def __init__(self, name):
        self.name = name

employee = Employee("John")
zoo = Zoo()
zoo.add_animal(animals[0])
zoo.add_employee(employee)

class ZooKeeper():
    def __init__(self, name):
        self.name = name
    def feed_animal(self, animal):
        print(f"{animal.name} is being fed by {self.name} the Zookeeper")

class Vet():
    def __init__(self, name):
        self.name = name
    def heal_animal(self, animal):
        print(f"{animal.name} is being healed by {self.name} the Vet")

zoo_keeper = ZooKeeper("Shane")
vet = Vet("James")
zoo_keeper.feed_animal(animals[1])
vet.heal_animal(animals[2])

