def getLoopSize(pk):
    subject = 7
    val = 1

    i = 0
    while val != pk:
        val *= subject
        val = divmod(val, 20201227)[1]
        i+=1

    return i

def transformSubject(subject, loopSize):
    val = 1
    for _ in range(loopSize):
        val *= subject
        val = divmod(val, 20201227)[1]
    return val

cPK = 15335876
dPK = 15086442

cLS = getLoopSize(cPK)
dLS = getLoopSize(dPK)

print(transformSubject(cPK, dLS))