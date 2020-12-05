with open("day2/input.txt", "r") as f:
    lines = f.readlines()

nValid = 0
for line in lines:
    val, let, pw = line.split(" ")

    let=let[0]

    i1 = int(val.split("-")[0])
    i2 = int(val.split("-")[1])
    
    if (pw[i1-1] == let) ^ (pw[i2-1] == let):
        nValid+=1

print(nValid)