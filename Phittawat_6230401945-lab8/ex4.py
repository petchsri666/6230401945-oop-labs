class ComEnStudent:

    def __init__(self, name, courses):
        self.name = name
        self.courses = []
        self.courses.extend(courses)

    def __str__(self):
        return f"{self.name} has taken these courses:{self.courses}"

    def take_courses(self, *take_courses):
        self.courses.extend(take_courses)

    def make_content_type(self, content):
        self.content = content


class CoEStudent(ComEnStudent):

    def __init__(self,name , courses):
        super(CoEStudent, self).__init__(name, courses)

    def __str__(self):
        return super(CoEStudent, self).__str__()


class DMEStudent(ComEnStudent):

    def __init__(self, name, courses):
        super(DMEStudent, self).__init__(name, courses)

    def __str__(self):
        return super(DMEStudent, self).__str__() + f"\n specialized in creating content type:{self.content}"


if __name__ == '__main__':
    com_students = []
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Pete", ["EN555555"])
    manee.take_courses("EN813702", "EN811301", "EN811302")
    mana.take_courses("TANBOII")
    mana.make_content_type("VDO Editor")
    com_students.append(manee)
    com_students.append(mana)
    for com_student in com_students:
        com_student.take_courses("SC401206")
        print(com_student)
