# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

print(([2] + [i for i in range(3, 200000, 2) if all(i % d for d in range(3, int(i ** 0.5) + 1, 2))])[10000])
