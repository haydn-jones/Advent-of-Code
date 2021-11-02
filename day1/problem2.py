import numpy as np

def main():
    masses = np.loadtxt('day1/input2.txt', dtype=np.float32)

    total_fuel = 0
    while np.count_nonzero(masses) > 0:
        masses = (masses // 3) - 2
        masses = masses.clip(min=0)

        total_fuel += sum(masses)

    print(total_fuel)

if __name__ == '__main__':
    main()