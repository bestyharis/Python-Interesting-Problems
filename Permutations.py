arr1,x = map(str,input().split())
x = int(x)

#arr1=list(arr1)

from itertools import permutations
arr1 = list(permutations(arr1,x))
arr1.sort()

for i in range(len(arr1)):
    str1 = ""
    for j in range(len(arr1[i])) :
        str1 += str(arr1[i][j])
    print(str1)

