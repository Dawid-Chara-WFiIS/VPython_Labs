def produce_triplets(a, b, power):
    for i in a:
        for j in b:
            if i < j:
                k = (i**power + j**power)**(1/power)
                if k % 1 == 0:
                    print("({}, {}, {})".format(i, j, int(k)))



def main():
    a = list(range(1, 101))
    b = list(range(1, 101))
    for i in range(2, 7):
        print("Producing triplets for power of {}".format(i))
        produce_triplets(a, b, i)


if __name__ == '__main__':
    main()
