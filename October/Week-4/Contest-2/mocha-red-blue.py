import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log2, ceil
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from bisect import insort
from collections import Counter
from collections import deque
from heapq import heappush,heappop,heapify
from itertools import permutations,combinations
from itertools import accumulate as ac
from random import randint as ri
mod = int(1e9)+7
#mod = 998244353
 
ip = lambda : int(stdin.readline())
inp = lambda: map(int,stdin.readline().split())
ips = lambda: stdin.readline().rstrip()
out = lambda x : stdout.write(str(x)+"\n")


t = ip()
for _ in range(t):
    n = ip()
    s = ips()
    ans = []
    ch = []
    prev = None
    nex = None
    ct = 0
    for i in s:
        if i == "?":
            ct += 1
        else:
            if ct != 0:
                nex = i
                ch.append([ct,prev,nex])
                ct = 0
                prev = i
                nex = None
            else:
                prev = i
    if ct != 0:
        ch.append([ct,prev,nex])

    
    cur = []
    for i in ch:
        val,prev,nex = i
        if prev == None and nex == None:
            xor = 0
            for j in range(val):
                if xor == 0:
                    cur.append('B')
                else:
                    cur.append("R")
                xor ^= 1
        elif prev == None and nex != None:
            xor = 0
            cur2 = []
            if nex == "B":
                for j in range(val):
                    if xor == 0:
                        cur2.append("R")
                    else:
                        cur2.append("B")
                    xor ^= 1
            else:
                for j in range(val):
                    if xor == 0:
                        cur2.append("B")
                    else:
                        cur2.append("R")
                    xor ^= 1
            cur += cur2[::-1]
        else:
            xor = 0
            if prev == "B":
                for j in range(val):
                    if xor == 0:
                        cur.append("R")
                    else:
                        cur.append("B")
                    xor ^= 1
            else:
                for j in range(val):
                    if xor == 0:
                        cur.append("B")
                    else:
                        cur.append("R")
                    xor ^= 1

    s = list(s)
    pt = 0
    for i in range(n):
        if s[i] == "?":
            s[i] = cur[pt]
            pt += 1

    s = ''.join(s)
    print(s)