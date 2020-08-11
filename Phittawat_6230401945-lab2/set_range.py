def set():
    a = {1, 2, 3, 4}
    b = {1, 3, 5, 7}
    c = a.union(b)
    d = a-b
    print("a is", a)
    print("b is", b)
    print("a | b is", c)
    print("a - b is", d)
    zero_twenty = list(range(20))
    print(zero_twenty)
    three_twelve = list(range(3, 13))
    print(three_twelve)
    third_int = list(range(2, 51, 3))
    print(third_int)


if __name__ == '__main__':
    set()