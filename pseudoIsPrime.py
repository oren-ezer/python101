import sys


def main(number):
    result = None

    if number % 2 == 0:
        result = "deviding by 2"
    elif number % 3 == 0:
        result = "deviding by 3"
    elif number % 4 == 0:
        result = "deviding by 4"
    elif number % 5 == 0:
        result = "deviding by 5"

    if result is not None:
        # print("the number " + number + " is " + result)
        print("the number is " + result)
    else:
        print("maybe the number is prime?")


if __name__ == "__main__":
    main(int(sys.argv[1]))
