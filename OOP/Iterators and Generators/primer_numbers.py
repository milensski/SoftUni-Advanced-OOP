def get_primes(int_list):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    for number in int_list:
        if is_prime(number) and number > 0:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
