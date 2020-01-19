N = int(input())
X,L=[],[]

for i in range(N):
    x,l = list(map(int, input().split()))
    X.append([x,l])
X.sort(key=lambda x:x[0],reverse=False)
# print(X)
ans=N
for i in range(1,N):
    if i>=2 and X[i-2][0]+X[i-2][1]>X[i-1][0]-X[i-1][1]:
        # print('a',i)
        continue

    if X[i-1][0]+X[i-1][1]>X[i][0]-X[i][1]:
        # print('b',i)
        ans-=1

print(ans)
