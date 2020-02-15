def binarysearch(A,key):
    left=0
    right=n
    while left<right:
        mid=(left+right)//2
        if A[mid]==key:
            return mid
        #探し物が中央より少ないなら、右端は中央値
        elif key<A[mid]:
            right=mid
        #そうでないなら左端は中央＋１
        # (mid==の時はありえないから)
        else:
            left=mid+1
    return None

n=int(input())
S = list(map(int, input().split()))
q=int(input())
T = list(map(int, input().split()))

ans=0
for t in T:
    # print(binarysearch(S,t))
    if type(binarysearch(S,t))==int:
        ans+=1
    
print(ans)