def fun(L1, L2, sgn):
    if sgn == '+':
        return [sum(i) for i in zip(L1, L2)]
    elif sgn == '*':
        return [i[0]*i[1] for i in zip(L1, L2)]
    elif sgn == '/':
        try:
            return [i[0] / i[1] for i in zip(L1, L2)]
        except ZeroDivisionError:
            raise ZeroDivisionError("You divided by zero!")
    elif sgn == '**':
        return [i[0] ** i[1] for i in zip(L1, L2)]
    elif sgn == '-':
        return [i[0] - i[1] for i in zip(L1, L2)]
    else:
        print("Not recognized operator")


def main():
    print(fun([1, 2, 3], [3, 4, 5], '**'))


if __name__ == '__main__':
    main()