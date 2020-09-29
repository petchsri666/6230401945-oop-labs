class student:
    def __init__(self, name, *course):
        self.name = name
        self.course = course


if __name__ == '__main__':
    manee = student("Manee", "842004")
    mana = student("Mana", "842004", "842005", "813701")
    chujai = student("Chujai", "842004", "842005")
    print(f"{manee.name} registered courses {manee.course}")
    print(f"{mana.name} registered courses {mana.course}")
    print(f"{chujai.name} registered courses {chujai.course}")