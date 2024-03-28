import math
# number of lattice combination for two directions is equal to binomial coeffeicient of x + y, x
dimensions = (20,20)
print(math.comb(dimensions[0]+dimensions[1], dimensions[0]))