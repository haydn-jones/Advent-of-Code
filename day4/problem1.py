def meets_criteria(num):
    num = str(num)

    # Check for double digit / decrease digit
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            break
    else:
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