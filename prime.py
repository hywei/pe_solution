#!/usr/bin/python2

from bisect import bisect


def isPrime(num):
    sq_num = int(num**0.5)
    for i in range(2, sq_num+1):
        if num % i == 0: return False;        
    return True

def isInPrimes(num, pv):

    """ check $num if in $pv or not """
    i = bisect(pv, num)
    return (True if i<=len(pv) and pv[i-1] == num else False)


def getPrimes(n, m=2):
    
    """ get all primes <=$n and >= $m"""
    return filter(isPrime, range(m, n+1));

def calPrimes(n, m=2):
    """ calculate primes <=$n and >=$m with sieve"""
    nl = range(2, n+1)
    pl = []

    for x in nl:
        if x == -1: continue
        for i in range(2, n):
            if x*i > n: break
            nl[x*i-2] = -1
        if x >=m: pl.append(x)
    return pl

def loadPrimes(file_name):
    """ load primes from a file """
    f = open(file_name, 'r')
    lines = f.readlines()
    pnum = int(lines[0])
    pr = lines[1].split(' ')
    pr = map(int, pr)
    return pr

if __name__ == "__main__":
    # test

    pv = getPrimes(100, 5)
    print pv

    pv2 = calPrimes(999, 100)
    print pv2
    if isInPrimes(90, pv):
        print "Yes"
    else: print "No"
