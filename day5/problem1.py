import numpy as np

def evaluate_intcode_new(intcode):
    i = 0
    while i < len(intcode):
        if intcode[i] == 99:
            break
        if []
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
def evaluate_intcode(intcode, noun=None, verb=None):
    intcode = np.copy(intcode)

    if noun != None:
        intcode[1] = noun
    if verb != None:
        intcode[2] = verb

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

    return intcode

def main():
    intcode = np.loadtxt('day2/input1.txt', dtype=int, delimiter=",")

    for noun in range(100):
        for verb in range(100):
            result = evaluate_intcode(intcode, noun=noun, verb=verb)[0]

            if result == 19690720:
                print(100 * noun + verb)
                break

if __name__ == "__main__":
    main()