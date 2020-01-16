import random
import time
n = 18


def main():
    print(' ' * (n - 2) + "START\n" + '-' * (n * 2 + 3))
    position = 0
    counter = 0
    steps = (-1, 1)
    print('|' + ' ' * (n + position) + '*' + ' ' * (n - position) + '|' + str(position))
    while True:
        position += random.choice(steps)
        counter += 1
        if position > 0:
            print('|' + ' ' * (n + position) + '*' + ' ' * (n - position) + '|' + '+' + str(position))
        else:
            print('|' + ' ' * (n + position) + '*' + ' ' * (n - position) + '|' + str(position))
        time.sleep(0.01)
        if abs(position) == n:
            print("Number of coin flips: {}".format(counter))
            break


if __name__ == '__main__':
    main()