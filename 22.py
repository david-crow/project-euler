# Using names.txt (right click and 'Save Link/Target As...'), 
# a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

names = [n[1:-1] for n in open("resources/22.txt", "r").read().split(",")]
print(sum([(i + 1) * sum(dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 27)))[l] for l in name) for i, name in enumerate(sorted(names))]))

### shorter...
# print(sum([(i + 1) * sum(dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 27)))[l] for l in name) for i, name in enumerate(sorted(["LIST","OF","NAMES"]]))]))