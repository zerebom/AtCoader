i = int(input())
W = list(map(int, input().split()))

if i-len(set(W))==0:
    print('YES')
else:
    print('NO')