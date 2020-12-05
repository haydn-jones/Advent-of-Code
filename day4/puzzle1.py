from collections import Counter

with open("day4/input.txt", "r") as f:
    passports = []
    fields = []
    for line in f.readlines():
        line = line.rstrip()

        if len(line) == 0:
            passports.append(dict(fields))
            fields = []
            continue

        for kv in line.split(" "):
            k, v = kv.split(":")
            if k == "cid":
                continue
            fields.append((k, v))
    
    passports.append(dict(fields))

required = Counter(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

valid = 0
for passport in passports:
    if Counter(passport.keys()) == required:
        valid += 1
print(valid)