import numpy as np
N = 100


def generate_room(number_of_people):
    return np.random.randint(1, 366, number_of_people)


def check_birthdays(room, n):
    for i in range(len(room)):
        x = 1
        for k in range(1+i, len(room)):
            if room[i] == room[k]:
                x += 1
            if x == n:
                return True
    return False


def main():
    f = open("results2.txt", 'w')
    for j in [2, 3, 4]:
        f.write("FOR {} people.\n".format(j))
        for i in range(1, 366):
            rooms = np.array([generate_room(i) for _ in range(N)])
            result = np.sum(np.apply_along_axis(check_birthdays, 1, rooms, j))
            f.write("{}) {}\n".format(i, result/N))
    f.close()


if __name__ == '__main__':
    main()
