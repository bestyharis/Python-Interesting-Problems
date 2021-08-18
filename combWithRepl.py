from itertools import combinations, combinations_with_replacement

s , n  = map(str,input().split())

for j in combinations_with_replacement(sorted(s), int(n)):
    print (''.join(j))