# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

print(sum([int(n[0]) for n in [(str(i), bin(i)[2:]) for i in range(1000000)] if (len(n[0]) == 1 or n[0][:len(n[0]) // 2] == n[0][-(len(n[0]) // 2):][::-1]) and (len(n[1]) == 1 or n[1][:len(n[1]) // 2] == n[1][-(len(n[1]) // 2):][::-1])]))
