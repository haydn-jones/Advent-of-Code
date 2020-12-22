import numpy as np
import pandas as pd
from scipy.ndimage import correlate
import itertools

transIter = itertools.product(range(4), ["NO", "UD", "LR"])

with open("day20/input.txt", "r") as f:
    tiles = f.read().strip().split("\n\n")
    tiles = [t.split("\n") for t in tiles]

tileDict = {}
for tile in tiles:
    id_  = tile[0]
    id_  = id_.split(" ")[1][:-1]
    fTile = np.array([np.array(list(l)) for l in tile[1:]])

    tileDict[id_] = fTile

#            Top         Left       Bottom          Right               
sides = [np.s_[0, :], np.s_[:, 0], np.s_[-1, :], np.s_[:, -1]]

matches = {k: [] for k in tileDict.keys()}
for id1, tile1 in tileDict.items():
    for id2, tile2 in tileDict.items():
        if id1 == id2:
            continue
        
        for i1, s1 in enumerate(sides):
            for i2, s2 in enumerate(sides):
                if np.array_equal(tile1[s1], tile2[s2]) or np.array_equal(tile1[s1], tile2[s2][::-1]):
                    matches[id1].append((id2, i1, i2))

corners = []
for k, v in matches.items():
    if len(v) == 2:
        corners.append(k)

start = None
for edge in corners:
    msides = [m[1] for m in matches[edge]]
    start = edge
    if 3 in msides and 2 in msides: # Top right
        break

# Create array
sideLen = int(np.sqrt(len(tileDict)))
arr = pd.DataFrame([list(list() for j in range(sideLen)) for i in range(sideLen)])

def transform(tile, r, flip):
    trans = tile
    if flip == "LR":
        trans = np.fliplr(tile)
    if flip == "UD":
        trans = np.flipud(tile)
    return np.rot90(trans, r)

def matchTransform(refEdge, p, slice_):
    for r in range(4):
        pRot = np.rot90(p, r)[slice_]
        pUD  = np.rot90(np.flipud(p), r)[slice_]
        pLR  = np.rot90(np.fliplr(p), r)[slice_]

        if np.array_equal(pRot, refEdge):
            return (r, "NO")
        if np.array_equal(pLR,  refEdge):
            return (r, "LR")
        if np.array_equal(pUD,  refEdge):
            return (r, "UD")
    
    return False

toPlace = list(tileDict.keys())
for r in range(sideLen):
    for c in range(sideLen):
        if r == 0 and c == 0:
            arr.loc[r, c] = (start, 0, "NO") # 0 rotations, no flip transform
            toPlace.remove(start)
            continue
        
        if c != 0:
            ref = arr.loc[r, c-1]
            rS  = np.s_[:, -1]
            cS  = np.s_[:, 0]
        else:
            ref = arr.loc[r-1, c]
            rS  = np.s_[-1, :]
            cS    = np.s_[0, :]


        refEdge = transform(tileDict[ref[0]], ref[1], ref[2])[rS]
        possibs = [m[0] for m in matches[ref[0]] if m[0] in toPlace]
        for pID in possibs:
            p = tileDict[pID]
            match = matchTransform(refEdge, p, cS)
            if match != False:
                break
        
        toPlace.remove(pID)
        arr.loc[r, c] = (pID, *match)

tArr = [list(list() for j in range(sideLen)) for i in range(sideLen)]
for r in range(arr.shape[0]):
    for c in range(arr.shape[1]):
        tID, rot, flip = arr.loc[r, c]
        tTrans = transform(tileDict[tID], rot, flip)
        tArr[r][c] = tTrans[1:-1, 1:-1]

block = np.block(tArr)
iBlock = np.zeros(block.shape)
iBlock[block == "#"] = 1

mask = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
    [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
])

for trans in transIter:
    out = correlate(iBlock, transform(mask, *trans), mode='constant')
    max_ = out.max()
    if max_ == np.sum(mask):
        break

print(np.sum(iBlock) - np.sum(out[out==np.sum(mask)]))