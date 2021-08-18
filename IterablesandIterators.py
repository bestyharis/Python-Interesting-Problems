n = int(input())
arr = map(str, input().split(" ",n-1))
x = int(input())

arr = list(arr)
lastPos = str(arr[n-1])
lastPos = lastPos[0]
arr.pop()
arr.append(lastPos)

import itertools
list1=list(map(list, itertools.combinations(arr,x)))
#print(list1)

size = len(list1)
numbers = 0

for i in range(size):
    if 'a' in list1[i]:
        numbers += 1

#print(numbers)
#print(size)

prob = numbers/size

print("{:.3f}".format(prob))
