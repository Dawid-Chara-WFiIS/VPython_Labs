def my_sum(li):
    s=0
    for i in li:
        s+=i
    return s


def my_prod(li):
    s = 1
    while li:
        s *= li.pop()
    return s


def main():
    print(my_sum(list(range(10))))
    print(my_prod(list(range(1, 5))))


if __name__ == "__main__":
    main()
