def main():
    counter = 0
    num = 3
    perfect_numbers = []
    while counter < 4:
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            perfect_numbers.append(num)
            print(num)
            counter += 1

        num += 1


if __name__ == '__main__':
    main()
