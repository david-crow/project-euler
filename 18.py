# By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
# the maximum total from top to bottom is 23.
    # 3
    # 7 4
    # 2 4 6
    # 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
    # it cannot be solved by brute force, and requires a clever method! ;o)

triangle_2d = [list(map(int, r.split())) for r in open("resources/18.txt", "r").read().split("\n")]
triangle_1d = [i for j in triangle_2d for i in j]

for i in range(len(s := triangle_2d) - 2, -1, -1): s[i] = [s[i][j] + max(s[i + 1][j], s[i + 1][j + 1]) for j in range(len(s[i]))]
print(s[0][0])
