import numpy as np
N = 100


def generate_room(number_of_people):
    return np.random.randint(1, 366, number_of_people)


def found_matching_bday(room):
    return not np.array_equal(np.unique(room), np.sort(room))


def main():
    f = open("results.txt", "w")
    f.write('1) 0\n')
    for i in range(2, 366):
        rooms = np.array([generate_room(i) for _ in range(N)])
        result = np.sum(np.apply_along_axis(found_matching_bday, 1, rooms))
        f.write("{}): {}\n".format(i, result/N))


if __name__ == '__main__':
    main()