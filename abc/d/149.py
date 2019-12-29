N, K = list(map(int, input().split()))
R, S, P = list(map(int, input().split()))
T = list(str(input()))
Te=[]
for t in T:
    if t=='r':
        Te.append(P)
    elif t=='s':
        Te.append(R)
    else:
        Te.append(S)
te=['r','s','p']
ans=0
for i in range(N):
    if K>i:
        ans+=Te[i]
    else:
        if T[i-K]==T[i]:
            #未来がない時はなんでも良い
            if i+K>=N:
                T[i]='null'
            else:
            #現在でも未来でもない手を代入
                te.remove(T[i])
                try:
                    te.remove(T[i+K])
                except:
                    pass
                T[i]=te[0]
                te=['r','s','p']
        else:
            ans+=Te[i]
print(ans)

