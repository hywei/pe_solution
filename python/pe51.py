#!/usr/bin/python2


from prime import *
from itertools import combinations

def replace(s, bl, ch):
    ls = list(s)
    for i in range(0, len(ls)):
        if i in bl: ls[i] = ch
    return ''.join(ls)
        

def countPrimeNumber(s, bl, pv):
    pnum=0
    for ch in map(chr, range(48, 58)):
        s_ = replace(s, bl, ch)
        if s_[0] != '0' and isInPrimes(int(s_), pv): pnum +=1
    return pnum


def getBits(s, ch):
    r = []
    for i in range(0, len(s)):
        if s[i] == ch : r.append(i)
    return r

def solve(n):
    pv = loadPrimes("primes_10000000.txt")
    psv = map(str, pv)
    for s in psv:
        for ch in ['0', '1', '2']:
            bl = getBits(s, ch)
            for i in range(1, len(bl)+1):
                lc = list(combinations(bl, i))
                for t in lc:
                    if countPrimeNumber(s, list(t), pv) >= n: return s

    return -1
        

if __name__ == "__main__":
    #test
    res = solve(8)
    print res
