# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
happiness = 0
for i in sc_ar :
    happiness += int((i in A) - (i in B))
    
print(happiness)