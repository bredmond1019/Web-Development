from time import perf_counter
import math

primes = [2, 3]

def isPrime(n):
    for prime in primes:
        if prime <= math.sqrt(n):
            if n % prime == 0:
                return False
        return True

def find_prime_number(seconds):

    start_time = perf_counter()
    current_time = 0

    n = 1
    while current_time - start_time < seconds:

        potential_primes = [6*n + 1, 6*n - 1]

        for potential_prime in potential_primes:
            if isPrime(potential_prime):
                primes.append(potential_prime)

        n += 1
        current_time = perf_counter()

    print(primes[-1])
    return None

find_prime_number(5) 