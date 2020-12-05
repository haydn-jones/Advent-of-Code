from math import ceil, inf

def partition(string, minVal, maxVal):
    for i in string:
        if i == 'F' or i == "L":
            half = ceil((maxVal - minVal) / 2)
            maxVal -= half
        else:
            half = ceil((maxVal - minVal) / 2)
            minVal += half

    return maxVal

def getSeatID(string):
    row, seat = string[:-3], string[-3:]
    row  = partition(row,  0, 127)
    seat = partition(seat, 0, 7)

    seatID = row * 8 + seat

    return seatID

with open("day5/input.txt", "r") as f:
    boardingPasses = [line.strip() for line in f.readlines()]

seatIDs = []
for p in boardingPasses:
    seatIDs.append(getSeatID(p))

seatIDs = sorted(seatIDs)

for i in range(len(seatIDs) -1):
    if seatIDs[i+1] == (seatIDs[i]+2):
        print(seatIDs[i]+1)
        break