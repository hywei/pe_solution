#!/usr/bin/python2

from itertools import permutations

def sum(p):
    idx = p.index(min(p[0:5]))
    lp = []
    for i in range(idx, idx+5):
        lp.append(p[i%5]);
        lp.append(p[i%5 + 5])
        if i%5 == 4: lp.append(p[5])
        else : lp.append(p[i%5+6])
    return int("".join(map(str,  lp)))

def solve():
    lp = list(permutations(range(1, 11), 10))
    
    max_v = -1
    for p in lp:
        n, flag = p[0] + p[5] + p[6], True
        for i in range(1, 5):
            _n = p[i] + p[i+5]
            if i == 4: _n += p[5]
            else: _n += p[i+6]
            if _n != n:
                flag = False; break
        if flag:
            s = sum(p);
            if max_v < s and len(str(s)) == 16: max_v = s
    print len(str(max_v))
    return max_v

if __name__ == "__main__":
    print solve()
