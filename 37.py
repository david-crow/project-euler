# The number 3797 has an interesting property. 
# Being prime itself, it is possible to continuously remove digits from left to right 
# and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def primeSieve(n):
    primes = [False, False] + [True] * (n - 1)

    for i in [2] + list(range(3, int(n ** 0.5) + 1, 2)):
        if primes[i]:
            for j in range(i ** 2, n + 1, i): primes[j] = False

    return primes

def leftTruncatable(s):
    for i in range(1, len(s)):
        if not primes[int(s[i:])]:
            return False
    return True

def rightTruncatable(s):
    for i in range(1, len(s)):
        if not primes[int(s[:-i])]:
            return False
    return True

primes = primeSieve(1000000)
truncatables, n = [], 11

while len(truncatables) < 11:
    if primes[n] and leftTruncatable(str(n)) and rightTruncatable(str(n)):
        truncatables.append(n)
    
    n += 1

print(sum(truncatables))
