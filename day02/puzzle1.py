with open("day2/input.txt", "r") as f:
    lines = f.readlines()

nValid = 0
for line in lines:
    val, let, pw = line.split(" ")

    let=let[0]

    low  = int(val.split("-")[0])
    high = int(val.split("-")[1])
    
    occurs = sum([l == let for l in pw])
    if low <= occurs <= high:
        nValid+=1

print(nValid)