N=int(input())
A,B=list(map(str,input().split()))

s=''
for a,b in zip(A,B):
    s+=a
    s+=b
print(s)
