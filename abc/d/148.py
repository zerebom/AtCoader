N = int(input())
l = list(map(int, input().split()))

tmp=0
for i in l:
    if i==tmp+1:
        tmp+=1

if tmp==0:
    print(-1)
else:
    print(N-tmp)