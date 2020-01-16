import math
import random
# noinspection PyUnresolvedReferences
from factorial import factorial
TOTAL = 10**6


def in_hypersphere(point):
    if sum([x**2 for x in point]) < 1:
        return True
    else:
        return False


def main():
    point = []
    matched = 0
    f = open('results1.txt', 'w')

    for dim in range(2, 21):
        for i in range(TOTAL):
            for _ in range(dim):
                point.append(random.random()*2 - 1)
            if in_hypersphere(point):
                matched += 1
            point = []

        volume_calc = (2**dim * matched / TOTAL)
        volume_math = (math.pi**(dim/2))/factorial(dim/2)
        f.write('{}) {} {} {}\n'.format(dim, volume_calc, volume_calc/volume_math, matched))
        matched = 0
    f.close()


if __name__ == '__main__':
    main()
