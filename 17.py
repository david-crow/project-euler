# If the numbers 1 to 5 are written out in words: 
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?

# NOTE: Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

print(3 + sum([(d := [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8, 6] + [0] * 9 + [6] + [0] * 9 + [5] + [0] * 9 + [5] + [0] * 9 + [5] + [0] * 9 + [7] + [0] * 9 + [6] + [0] * 9 + [6] + [0] * 9 + [7] + [0] * 899 + [11])[i] * (d[i] != 0) + (d[i] == 0) * (((d[i] == 0) * (d[100] + d[i // 100] + 3 * (i % 100 != 0)) * (i > 100)) + (d[(i % 100) // 10 * 10] * (i % 100 > 20) if i > 100 else d[i // 10 * 10] * (i > 20)) + ((d[(i % 100) % 10] if (i % 100) > 20 else d[i % 100]) if i > 100 else (d[i % 10] if i > 20 else d[i]))) for i in range(1001)]))
