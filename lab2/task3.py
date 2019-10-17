import random
import math


def in_circle(x, y):
    if math.sqrt(x**2 + y**2) <= 1:
        return True
    else:
        return False


def generate_points(amt, x, y):
    for i in range(amt):
        x.append(random.random()*2 - 1)
        y.append(random.random()*2 - 1)


def main():
    x = []
    y = []
    f = open("res2.txt", "w")
    generate_points(10**6, x, y)
    in_c = 0
    out_c = 0
    i = 0
    while i < 100:
        if in_circle(x[i], y[i]):
            in_c += 1
        i += 1
        est_pi = 4*in_c/i
        f.write(str(i) + ') ' + str(est_pi) + ' ' + str(est_pi/math.pi) + '\n')
    for j in range(3, 7):
        while i < 10**j:
            if in_circle(x[i], y[i]):
                in_c += 1
            i += 1
        est_pi = 4 * in_c / i
        f.write(str(i) + ') ' + str(est_pi) + ' ' + str(est_pi / math.pi) + '\n')

    f.close()


if __name__ == '__main__':
    main()
