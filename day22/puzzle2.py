import functools
import numpy as np
from copy import deepcopy

with open("day22/input.txt", "r") as f:
    data = f.read().strip().split("\n\n")

ogDecks = {}
for player in data:
    pID, cards = player.split(":\n")
    pID = pID[7:]
    ogDecks[pID] = [int(v) for v in cards.split("\n")]

def recursiveCombat(decks):
    nCards = sum(len(v) for v in decks.values())
    instances = set()

    while 0 not in [len(v) for v in decks.values()]:
        if (tuple(decks['1']), tuple(decks['2'])) in instances:
            return ('1', np.dot(decks['1'], range(len(decks['1']), 0, -1)))
        instances.add((tuple(decks['1']), tuple(decks['2'])))

        c1, c2 = decks['1'].pop(0), decks['2'].pop(0)


        if c1 <= len(decks['1']) and c2 <= len(decks['2']):
            newDeck = deepcopy(decks)
            newDeck['1'] = newDeck['1'][:c1]
            newDeck['2'] = newDeck['2'][:c2]
            winner = recursiveCombat(newDeck)[0]
        else:
            winner = '1' if c1 > c2 else '2'

        decks[winner].extend([c1, c2] if winner == '1' else [c2, c1])

    if len(decks['1']) == nCards:
        return ('1', np.dot(decks['1'], range(nCards, 0, -1)))
    else:
        return ('2', np.dot(decks['2'], range(nCards, 0, -1)))

out = recursiveCombat(deepcopy(ogDecks))
print(out)