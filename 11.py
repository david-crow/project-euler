# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

grid_2d = [list(map(int, line.split())) for line in open("resources/11.txt", "r").readlines()]
print(max([max((g := [i + [0, 0, 0] for i in grid_2d] + [[0] * 23] * 3)[i][j] * g[i][j+1] * g[i][j+2] * g[i][j+3], g[i][j] * g[i+1][j] * g[i+2][j] * g[i+3][j], g[i][j] * g[i+1][j+1] * g[i+2][j+2] * g[i+3][j+3], g[i][j] * g[i-1][j+1] * g[i-2][j+2] * g[i-3][j+3]) for i in range(20) for j in range(20)]))
