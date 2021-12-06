# Couldn't get recursion in python fast enough so I switched to rust. See part2.rs
from collections import defaultdict

with open("input.txt", "r") as f:
    line = f.readlines()[0]
    data = [int(x) for x in line.strip().split(",")]

def step(fish, cur_step, max_steps):
    delta = -fish - 1
    if (cur_step - delta) > max_steps:
        return 1
    else:
        return step(6, cur_step-delta, max_steps) + step(8, cur_step-delta, max_steps)

unique_count = defaultdict(int)
for x in data:
    unique_count[x] += 1

sums = 0
for fish, count in unique_count.items():
    sums += step(fish, 0, 256) * count

print(sums)