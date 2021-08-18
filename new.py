operation=int(input('enter the operation you want to perform (1-add, 2-sub, 3-mutiple, 4-division ----)'))
a =int( input('enter 1st number'))
b= int(input(' enter 2nd number'))

if operation == 1:
    print(a+b)
elif operation==2:
    print(a-b)
elif operation==3:
    print(a*b)
elif operation==4:
    if b != 0 : 
        print(a/b)
    else :
        print("Division by zero")
else: 
    print('operation not possible')