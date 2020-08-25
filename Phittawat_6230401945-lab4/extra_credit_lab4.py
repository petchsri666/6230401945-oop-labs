list = []
while True:
    try:
        list = str(input("Enter the list of numbers (delimited by a comma):")).split(", ")
        print(list)
        index =  int(input("Enter index:"))
        index1 = list[index]
        print(index1)
    except IndexError:
        print("The list has no element at index", index)
        pass