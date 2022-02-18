# Euler discovered the remarkable quadratic formula: n^2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. 
# However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
# and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

# The incredible formula n^2 - 79n + 1601 was discovered, 
# which produces 80 primes for the consecutive values 0 <= n <= 79. 
# The product of the coefficients, -79 and 1601, is -126479.

# Consider quadratics of the form n^2 + an + b, where |a| < 1000 and |b| <= 1000, 
# where |n| is the modulus/absolute value of n (e.g., |11| = 11 and |-4| = 4).

# Find the product of the coefficients a and b for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, starting with n = 0.

from operator import itemgetter

def primeSieve(n):
    primes = [False, False] + [True] * (n - 1)

    for i in [2] + list(range(3, int(n ** 0.5) + 1, 2)):
        if primes[i]:
            for j in range(i ** 2, n + 1, i): primes[j] = False

    return primes

def main():
    def isPrime(n):
        if n < 2:
            return False
        return primes[n]

    n = 1000
    primes = primeSieve(100000)
    coefficients = []

    for a in range(-n + 1, n):
        for b in range(-n, n + 1):
            counter = 0

            while isPrime(counter * counter + a * counter + b):
                counter += 1

            coefficients.append((a, b, counter))

    longest_chain = max(coefficients,key=itemgetter(2))
    print(longest_chain[0] * longest_chain[1])

main()
