def index(a):
    m=0
    ind=0
    for i in range(len(a)):
        if a[i]>m:
            m=a[i]
            ind=i
    return ind
t=input()
while(t>0):
    t-=1
    a=map(int,raw_input().split())
    n=input()
    count=0
    for i in range(n):
        k=index(a)
        if a[k]>=1:
            count+=a[k]
            a[k]-=1
        else:break
    print count