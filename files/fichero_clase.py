import pickle

class Automobile:
    def __init__(self, color, wheels, doors):
        self.color = color
        self.wheels = wheels
        self.doors = doors

    def _getSpecs(self):
        print(
            f'this automobile is {self.color}, has {self.wheels} wheels and {self.doors} doors')
        

car = Automobile('red', 4, 2)


with open('./car.bin', 'wb') as f:
    pickle.dump(car, f)

with open('./car.bin', 'rb') as f:
    obj = pickle.load(f)

print(obj._getSpecs())