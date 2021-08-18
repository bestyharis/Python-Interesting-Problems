from itertools import combinations
def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

def solve (N, M, A, B):
    # Write your code here
    countM = 0
    countN = 0
    list1 = []
    list2 = []
    denominator = 1
    
    
    for i in range(1,M):
        x = list(combinations(A,i))
        for j in x:
            list1.append(j)

    for i in range(1,N+2):
        y = list(combinations(B,i))
        for j in y:
            list2.append(j)
    


    denominator = len(list1) * len(list2)
    
    numerator = 0
    for i in list1:
        for j in list2:
            if(sum(i) == sum(j)):
                numerator = numerator+1

    a= modInverse(denominator,1000000007)
    result = (numerator*a) % 1000000007
    
    return(result)
    pass

N = int(input())
M = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

out_ = solve(N, M, A, B)
print (out_)