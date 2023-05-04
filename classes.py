class Automobile:
    def __init__(self, color, wheels, doors):
        self.color = color
        self.wheels = wheels
        self.doors = doors

    def _getSpecs(self):
        print(
            f'this automobile is {self.color}, has {self.wheels} wheels and {self.doors} doors')


class Car(Automobile):
    def __init__(self, speed, cilinders, color, wheels, doors):
        super().__init__(color, wheels, doors)
        self.speed = speed
        self.cilinders = cilinders

    def _getCar(self):
        print(
            f'this car can go up to {self.speed}km/h and has {self.cilinders} cilinders')


car = Car(8, 6, 'white', 4, 3)
car._getCar()
car._getSpecs()
