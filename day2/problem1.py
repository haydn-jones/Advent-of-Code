import numpy as np

intcode = np.loadtxt('day2/input1.txt', dtype=int, delimiter=",")
intcode[1] = 12
intcode[2] = 2

i = 0
while i < len(intcode):
    if intcode[i] == 99:
        break
    
    op   = intcode[i + 0]
    src1 = intcode[i + 1]
    src2 = intcode[i + 2]
    dest = intcode[i + 3]

    if op == 1:
        res = intcode[src1] + intcode[src2]
    elif op == 2:
        res = intcode[src1] * intcode[src2]
    
    intcode[dest] = res
    i += 4

print(intcode[0])