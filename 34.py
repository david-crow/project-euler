# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial
print(sum([n[0] for n in [(n, list(map(int, list(str(n))))) for n in range(100000)] if n[0] == sum([factorial(d) for d in n[1]])][2:]))
