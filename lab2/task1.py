from math import pi


def calc_pi(acc):
    result = 0.0
    for n in range(acc):
        result += (-1.0) ** n / (2.0 * n + 1.0)
    return 4 * result


def main():
    with open("res.txt", "w") as f:
        for i in range(1, 101):
            est_pi = calc_pi(i)
            f.write(str(i) + ' ' + str(est_pi) + ' ' + str(est_pi/pi) + '\n')
        for i in range(3, 8):
            est_pi = calc_pi(10**i)
            f.write(str(10**i) + ' ' + str(est_pi) + ' ' + str(est_pi/pi) + '\n')

    f.close()


if __name__ == '__main__':
    main()
