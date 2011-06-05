#!/usr/bin/python2

ELIST = range(65, 91) + range(97, 123) + \
    [32, 33, 34, 39, 40, 41, 44, 45, 46, 59] +\
    range(48, 58)

def check_valid(text, key):
    idx = 0
    for t in text:
        if (t^key[idx]) not in ELIST: return False
        idx = (idx+1)%3
    return True

def solve(text):
    key=[]
    for a in range(ord('a'), ord('z')+1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                if check_valid(text, [a,b,c]): key=[a,b,c]; break
            if len(key) !=0 : break
        if len(key) != 0: break        
    print key, map(chr, key)
    sum , i = 0, 0
    for t in text:
        sum += t ^ key[i]
        i = (i+1)%3
    return sum

if __name__ == "__main__":
    f = open("cipher1.txt", "r")
    text = f.read()
    f.close()
    text = text[0:-2]
    text = map(int, text.split(','))
    print solve(text)
