def primes_in_range(min, max):
    counter = 0
    for number in range(min, max):
        if not is_prime(number):
            print(str(number) + " is a prime number")
            counter = counter + 1

    print(
        "between "
        + str(min)
        + " and "
        + str(max)
        + " there are "
        + str(counter)
        + " prime numbers"
    )


def is_prime(number):
    for divider in range(2, number):
        if number % divider == 0:
            return True
    return False


low = 100000000
high = low + 100
primes_in_range(low, high)
print("end of run")
