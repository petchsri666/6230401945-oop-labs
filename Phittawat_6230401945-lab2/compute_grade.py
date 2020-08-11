def get_info():
    name = str(input("Please Enter the student name:"))
    mark_midterm = False
    while not mark_midterm:
        try:
            mark_midterm = float(input(
                "Please enter the student's midterm exam mark (0-100):"))
            if mark_midterm >= 0 and mark_midterm <= 100:
                mark_midterm2 = (mark_midterm / 2)
            elif mark_midterm:
                print("Please enter a valid exam mark (0-100)")
                mark_midterm = False
        except ValueError:
            print("Please enter a valid exam mark (0-100)")

    mark_final = False
    while not mark_final:
        try:
            mark_final = float(input(
                "Please enter the student's final exam mark (0-100):"))
            if mark_final >= 0 and mark_final <= 100:
                mark_final2 = (mark_final / 2)
                total = mark_final2 + mark_midterm2
                if 80 <= total <= 100:
                    print(name, "has total mark as %.2f" % total,
                          "and grade as A")
                elif 70 <= total < 80:
                    print(name, "has total mark as %.2f" % total,
                          "and grade as B")
                elif 60 <= total < 70:
                    print(name, "has total mark as %.2f" % total,
                          "and grade as C")
                elif 50 <= total < 60:
                    print(name, "has total mark as %.2f" % total,
                          "and grade as D")
                elif total < 50:
                    print(name, "has total mark as %.2f" % total,
                          "and grade as F")
            elif mark_final:
                print("Please enter a valid exam mark (0-100)")
                mark_final = False
        except ValueError:
            print("Please enter a valid exam mark (0-100)")


if __name__ == '__main__':
    get_info()