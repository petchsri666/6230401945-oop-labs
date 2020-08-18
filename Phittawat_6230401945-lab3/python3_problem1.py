def squaresum():
    a = 1
    numbers = 200
    b = 0
    while b < numbers:
        b = b + (a * a)
        a += 1
        if b >= numbers:
            print("The final total is", b)
            break


if __name__ == '__main__':
    squaresum()
