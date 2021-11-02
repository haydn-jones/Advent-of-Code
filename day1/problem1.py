import numpy as np

masses = np.loadtxt('day1/input1.txt', dtype=int)
fuel = (masses // 3) - 2

print(sum(fuel))