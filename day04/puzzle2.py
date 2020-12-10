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
for p in passports:
    if Counter(p.keys()) != required:
        continue

    if int(p["byr"]) > 2002 or int(p["byr"]) < 1920:
        continue
    if int(p["iyr"]) > 2020 or int(p["iyr"]) < 2010:
        continue
    if int(p["eyr"]) > 2030 or int(p["eyr"]) < 2020:
        continue

    if "cm" in p["hgt"]:
        val = int(p["hgt"][:-2])
        if val < 150 or val > 193:
            continue
    elif "in" in p["hgt"]:
        val = int(p["hgt"][:-2])
        if val < 59 or val > 76:
            continue
    else:
        continue

    if (p["hcl"][0] !="#") or (len(p["hcl"])-1 != 6) or not p["hcl"][1:].isalnum():
        continue

    if p["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        continue

    if not p["pid"].isnumeric() or len(p["pid"]) != 9:
        continue

    valid += 1

print(valid)