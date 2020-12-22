import numpy as np

with open("day22/input.txt", "r") as f:
    data = f.read().strip().split("\n\n")

decks = {}
for player in data:
    pID, cards = player.split(":\n")
    pID = pID[7:]
    decks[pID] = [int(v) for v in cards.split("\n")]

nCards = sum(len(v) for v in decks.values())

while max(len(v) for v in decks.values()) != nCards:
    c1, c2 = decks['1'].pop(0), decks['2'].pop(0)

    if c1 > c2:
        decks['1'].extend([c1, c2])
    else:
        decks['2'].extend([c2, c1])

for k, v in decks.items():
    if len(v) == 0:
        continue
    print(np.sum(np.array(v) * range(1, len(v)+1)[::-1]))