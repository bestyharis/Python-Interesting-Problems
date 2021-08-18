arr1 = map(int, input().split())
arr2 = map(int, input().split())

arr1 = list(arr1)
arr2 = list(arr2)

prodList =[]
'''
for i in range(len(arr1)):
    for j in range(len(arr2)):
        prodList.append([arr1[i],arr2[j]])
'''


'''
Need to Use itertools
'''

from itertools import product
prodList=list(product(arr1, arr2))

'''
for i in range(len(prodList)):
    print(prodList[i])
'''
print(*prodList,sep=" ")
