import numpy as np
from factorial import factorial
TOTAL = 10**6


def in_hypersphere(point):
    """point is a list which elements are coordinates of point in ndim"""
    if np.sqrt(np.sum(point**2)) < 1:
        return 1
    else:
        return 0


def main():
    f = open('results2.txt', 'w')
    for dim in range(2, 21):
        points = np.random.random((TOTAL, dim)) * 2 - 1
        matched = np.sum(np.sum(points**2, axis=1) < 1)
        volume_calc = (2 ** dim * matched / TOTAL)
        volume_math = (np.pi**(dim/2))/factorial(dim/2)
        f.write('{}) {} {} {}\n'.format(dim, volume_calc, volume_calc / volume_math, matched))
    f.close()


if __name__ == '__main__':
    main()