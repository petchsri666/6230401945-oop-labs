class Pet:

    def __init__(self, name):
        self.name = name

    def show_info(self):
        return print(f"I'm {self.name}")
    
    def move(self):
        return print(f"moving...")


class Cat(Pet):

    def __init__(self, name, owner, color):
        self.owner = owner
        self.color = color
        super(Cat, self).__init__(name)
    
    def move(self):
        return print(f"Cat likes to walk more than run")

    def show_info(self):
        super(Cat, self).show_info()
        return print(f" and is   {self.color}"
                     f"\n belonging to  {self.owner}")


class Dog(Pet):

    def __init__(self, name, owner, color):
        self.owner = owner
        self.color = color
        super(Dog, self).__init__(name)

    def move(self):
        return print(f"Cat likes to walk more than run")

    def show_info(self):
        super(Dog, self).show_info()
        return  print(f" and is   {self.color}"
                      f"\n belonging to   {self.owner}")

    def eat_cat(self,  cat):
        return print(f"Dog {self.name} eats cat {cat.name}")


if __name__ == '__main__':
    pet1 = Pet("Seenual")
    pet1.show_info()
    pet1.move()
    cat1 = Cat("Dell", "Pete", "white")
    cat1.show_info()
    cat1.move()
    dog1 = Dog("Pete", "Petezaza", "Korean")
    dog1.show_info()
    dog1.move()
    dog1.eat_cat(cat1)