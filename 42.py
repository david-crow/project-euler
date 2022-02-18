# The nth term of the sequence of triangle numbers is given by tn = 1/2 * n * (n+1); 
# so the first ten triangle numbers are:
    # 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position 
# and adding these values we form a word value. For example, 
# the word value for SKY is 19 + 11 + 25 = 55 = t10. 
# If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), 
# a 16K text file containing nearly two-thousand common English words, 
# how many are triangle words?

import string

words = [word[1:-1] for word in open("./resources/42.txt").read().split(",")]
letter_scores = {l : i + 1 for i, l in enumerate(string.ascii_uppercase)}
scoring = lambda w : sum([letter_scores[l] for l in w])
word_scores = {word : scoring(word) for word in words}
triangles = [n * (n + 1) // 2 for n in range(1, 20)] # max score is RESPONSIBILITY = 192
triangle_words = [word for word in words if word_scores[word] in triangles]
print(len(triangle_words))
