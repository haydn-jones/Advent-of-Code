from itertools import groupby

def meets_criteria(num):
    num = str(num)

    # Find repeating digits
    reps = []
    for k, g in groupby(num):
        reps.append(list(g))
    
    if 2 not in [len(rep) for rep in reps]:
        return False

    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i + 1]):
            return False
    
    return True

valid = 0
for num in range(134792, 675810 + 1):
    if meets_criteria(num):
        valid += 1
print(valid)