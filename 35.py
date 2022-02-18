# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

primes, unprimes = [2], set()
for i in range(3, 1000000, 2):
    if i in unprimes: continue
    for j in range(i * 3, 1000000, i * 2): unprimes.add(j)
    primes.append(i)
print(len([rotations[0] for rotations in [[int("".join(str(n)[i:] + str(n)[:i])) for i in range(len(list(str(n))))] for n in [2, 5] + [p for p in primes if all(n not in str(p) for n in "024685")]] if all(rotation in primes for rotation in rotations)]))
