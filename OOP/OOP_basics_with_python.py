class Dog:
    attr1 = "mammal"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print('{} says gaau gaau gaau'.format(self.name))

Rodger = Dog('KiKi')
Rodger.speak()
