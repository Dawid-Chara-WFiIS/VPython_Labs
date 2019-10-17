import math


def plot_sin(values):
    f = open("plot.txt", 'w')
    for i in values:
        if i > 0:
            f.write('+' * i + '\n')
        if i < 0:
            f.write('-' * abs(i) + '\n')
        if i == 0:
            f.write(str(0)+'\n')
    f.close()


def main():
    angles = [i*(2*math.pi)/50 for i in range(100)]
    sin_values = [math.sin(i)*50 for i in angles]
    sin_values_int = [int(i) for i in sin_values]
    plot_sin(sin_values_int)


if __name__ == '__main__':
    main()