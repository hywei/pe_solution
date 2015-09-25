#!/usr/bin/python2

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def countPair(h):
    lc = map( lambda x: x[0], h)
    np=0
    if lc[0] == lc[1] != lc[2] : np += 1
    if lc[0] != lc[1] == lc[2] != lc[3] : np += 1
    if lc[1] != lc[2] == lc[3] != lc[4] : np += 1
    if lc[2] != lc[3] == lc[4] : np += 1
    return np

def countKind(h):
    lc = map( lambda x: x[0], h)
    nk=0
    if lc[0] == lc[1] == lc[2] != lc[3] :  nk += 1
    if lc[0] != lc[1] == lc[2] == lc[3] != lc[4] : nk += 1
    if lc[1] != lc[2] == lc[3]  == lc[4] : nk += 1
    return nk

def isFlush(h):
    "check hands is Flash or not"
    for s in h:
        if s[-1] != h[0][-1] : return False
    return True

def isStraight(h):
    "check hands is Straight or not"
    for i in range(0, len(h)-1):
        if ord(h[i][0]) - 1 != ord(h[i+1][0]): return False
    return True

def isFullHouse(h):
    lc = map(lambda x: x[0], h)
    return countPair(lc) == countKind(lc) == 1

def is4Kind(h):
    "check hands is Four of Kind"
    return h[0][0] == h[3][0] or h[1][0] == h[4][0]

def convert(h):
    lc = map(lambda x: chr(ord('A') + CARDS.index(x[0:-1])) + x[-1], h)
    lc.sort(reverse=True)
    return lc

def encoding(h):
    lc = map(lambda x: x[0:-1], h)
    if isFlush(h) and isStraight(h) : lc.insert(0, '7')
    elif is4Kind(h):
        if lc[1] == lc[4]: lc[0],lc[4] = lc[4],lc[0]
        lc.insert(0, '6')
    elif isFullHouse(h):
        if lc[0] == lc[1] != lc[2]:
            lc[0], lc[3] = lc[3], lc[0]
            lc[1], lc[4] = lc[4], lc[1]
        lc.insert(0, '5')
    elif isFlush(h): lc.insert(0, '4')
    elif isStraight(h): lc.insert(0, '3')
    elif countKind(h) != 0:
        if lc[1] == lc[2] == lc[3]: lc[0], lc[3] = lc[3], lc[0]
        if lc[2] == lc[3] == lc[4]:
            lc[0], lc[3] = lc[3], lc[0]
            lc[1], lc[4] = lc[4], lc[1]
        lc.insert(0, '2')
    elif countPair(h) != 0:
        np = countPair(h)
        if np == 2:
            if lc[1] == lc[2] and lc[3] == lc[4]:
                lc[0], lc[2] = lc[2], lc[0]
            if lc[0] == lc[1] and lc[3] == lc[4]:
                lc[2], lc[4] = lc[4], lc[2]
        elif np == 1:
            if lc[3] == lc[4]: lc[2], lc[4] = lc[4], lc[2]
            if lc[2] == lc[3]: lc[1], lc[3] = lc[3], lc[1]
            if lc[1] == lc[2]: lc[0], lc[2] = lc[2], lc[0]
        lc.insert(0, chr(ord('0') + np))
        lc.insert(0, '1')
    else: lc.insert(0, '0')        
    return ''.join(lc)
    
if __name__ == "__main__":
    res=0
    f = open("poker.txt", "r")
    lines = f.readlines()
    for line in lines:
        ll = line[0:-2].split(' ')
        h1, h2 = ll[0:5], ll[5:]
        s1, s2 = encoding(convert(h1)), encoding(convert(h2))
        if s1 > s2 : res +=1
    print res
                  
