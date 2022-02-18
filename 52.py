# It can be seen that the number, 125874, and its double, 251748, 
# contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, 
# such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

n = 2
while True:
    if all(s == set(str(n)) for s in [set(str(n * 2)), set(str(n * 3)), set(str(n * 4)), set(str(n * 5)), set(str(n * 6))]):
        break
    n += 1
print(n)
