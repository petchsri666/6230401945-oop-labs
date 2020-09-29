class Numbers:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def get_factors(cls, x):
        cls.x = x

    @classmethod
    def display_factors(cls, x):
        if x % 2 == 0:
            numberdivide = x / 2
            return f"Factor of {x} is {numberdivide} and {numberdivide}"
        elif x % 2 > 0:
            numbershare_1 = (x / 2) + 0.5
            numbershare_2 = (x / 2) - 0.5
            return f"Factor of {x} is {numbershare_1} and {numbershare_2}"

    @staticmethod
    def is_valid_divisor(x):
        if x == 0:
            return f"{x} is not a valid divisor"
        elif x > 0:
            return f"{x} is valid divisor"


if __name__ == '__main__':
    print(f"3 + 5 is {Numbers(3, 5).add()}")
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(8))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
