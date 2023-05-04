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


""" car = Car(8, 6, 'white', 4, 3)
car._getCar()
car._getSpecs() """



class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def _getInfo(self):
        print(f'the student name is {self.name} and grade is {self.grade}')

    def _didApprove(self):
        if self.grade >= 3:
            return print(f'the student {self.name} has approved with grade {self.grade}')
        print(f'the student {self.name} has not approved with grade {self.grade}')


jake = Student('Jake', 4)
carl = Student('Carl', 2.9)


jake._getInfo()
jake._didApprove()

carl._getInfo()
carl._didApprove()