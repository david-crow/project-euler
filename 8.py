# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

n = open("resources/8.txt", "r").read()
print(max([int(n[i + 0]) * int(n[i + 1]) * int(n[i + 2]) * int(n[i + 3]) * int(n[i + 4]) * int(n[i + 5]) * int(n[i + 6]) * int(n[i + 7]) * int(n[i + 8]) * int(n[i + 9]) * int(n[i + 10]) * int(n[i + 11]) * int(n[i + 12]) for i in range(988)]))
