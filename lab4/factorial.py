from math import pi, sqrt


def factorial(number):
    """returns number! , number must be integer or float like x.5 where x is integer
    returns -1 if you passed wrong number"""
    if number > 0:
        if number % 1 == 0:
            return number * factorial(number-1)
        elif number % 1 == 0.5:
            if number == 0.5:
                return sqrt(pi)/2
            else:
                return number * factorial(number - 1)
    else:
        return 1


def main():
    for i in range(0, 20):
        print(factorial(i+0.5))


if __name__ == '__main__':
    main()
