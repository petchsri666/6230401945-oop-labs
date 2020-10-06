class Vehicle:

    def __init__(self, name, speed, milegde):
        self.name = name
        self.__speed = speed
        self.miledge = milegde

    def set_speed(self, speed):
        self.__speed = speed

    def __str__(self):
        return f"Name: {self.name} :speed {self.__speed} mileage: {self.miledge}"


class Car(Vehicle):
    def __init__(self, name, __speed, miledge, num_doors):
        self.num_doors = num_doors
        super(Car, self).__init__(name, __speed, miledge)

    def __str__(self):
        return f"{super().__str__()} num doors: {self.num_doors}"


class Bus(Vehicle):
    def __init__(self, name, __speed, miledge, capacity):
        self.capacity = capacity
        super(Bus, self).__init__(name, __speed, miledge)

    def __str__(self):
        return f"{super().__str__()} capacity: {self.capacity}"


if __name__ == '__main__':
    car = Car("Ferrari Spider", 90, 150000, 2)
    bus = Bus("School Volvo", 12, 200000, 100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)