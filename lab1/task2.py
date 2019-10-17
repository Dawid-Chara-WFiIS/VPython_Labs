def main():
    while True:
        answer = input()
        if answer == "the end":
            return 0
        try:
            answer = int(answer)
        except ValueError:
            raise ValueError("Please type proper integer!")
        if answer % 2 == 0:
            print("Number you typed is even.")
        else:
            print("Number you typed is odd.")


if __name__ == "__main__":
    main()

