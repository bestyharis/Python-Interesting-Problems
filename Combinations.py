from itertools import combinations

s , n  = map(str,input().split())

for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        print (''.join(j))