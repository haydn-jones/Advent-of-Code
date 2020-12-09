with open("day9/input.txt", "r") as f:
    data = [int(line.strip()) for line in f.readlines()]

def subsetsum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target == (nums[i] + nums[j]):
                return True
    return False

for i in range(26, len(data)):
    if subsetsum(data[i-25:i], data[i]) == False:
        print(data[i])
        exit(0)