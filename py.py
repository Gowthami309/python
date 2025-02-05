# 1
n=0
while n<100:
    n=n+1
    print(n)
#2
#using while loop
n=101
while n>0:
    n=n-1
    print(n)

#using for loop
for i in range(100,0,-1):
    print(i)

    #3
num=1234
rev_num=0
while num!=0:
    digit=num%10
    rev_num=rev_num*10+digit
    num//=10
print(rev_num)