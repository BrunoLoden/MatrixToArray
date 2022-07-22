# import random as r
# print((r.random()))

# cook your dish here
t_n=int(input())

for i in range(t_n):

    p,q = map(int,input().split())

    a=(p+q)
    
    
    if(a%4==0 or (a-1)%4==0):
            print("BOB")
    else:
            print("ALICE")
    

    