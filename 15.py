# Starting in the top left corner of a 2×2 grid, 
# and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

# binomial coefficient -- (a + b over b) is ((a + b)! / (a! * b!))

def main():
    return int((f := lambda x : 1 if x < 2 else x * f(x - 1))(40) / ((d := f(20)) * d))

print((main()))
