# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

print([i for i in [str(w) for w in sorted(list(set([i * j for i in range(100, 1000) for j in range(100, 1000)])), reverse=True)] if i[:len(i) // 2] == i[-(len(i) // 2):][::-1]][0])
