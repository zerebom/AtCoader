N,Q = list(map(int, input().split()))
S=list(str(input()))
ACs=[]
for i in range(len(S)-1):
    if S[i]=='A' and S[i+1]=='C':
        ACs.append(i)
ACs=set(ACs)
for q in range(Q):
    l,r = list(map(int, input().split()))
    lr=set(range(l-1,r-1))
    print(len(lr&ACs))


