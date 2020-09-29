class Student:
    university_name = "Khon Kaen University"

    def __init__(self, name, *course):
        self.name = name
        self.course = course

    def print(self):
        print(f"{self.name} registered courses {self.course}")

    @classmethod
    def set_university_name(cls, uni):
        cls.university_name = uni

    @classmethod
    def get_university_name(cls):
        return cls.university_name


if __name__ == '__main__':
    manee = Student("Manee", "842004")
    mana = Student("Mana", "842004", "842005", "813701")
    chujai = Student("Chujai", "842004", "842005")
    manee.print()
    mana.print()
    chujai.print()
    manee.set_university_name("KKU")
    print(f"These students are in {mana.get_university_name()}")
