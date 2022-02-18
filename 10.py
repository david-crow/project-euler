# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

print(2 + sum([i for i in range(3, 2000000, 2) if all(i % d for d in range(3, int(i ** 0.5) + 1, 2))]))

### faster...
# n, a = 2000000, [False, False] + [True] * (2000000 - 1)
# for i in [2] + list(range(3, int(n ** 0.5) + 1, 2)):
#     if a[i]:
#         for j in range(i ** 2, n + 1, i): a[j] = False
# print(sum([i * j for i, j in enumerate(a)]))
