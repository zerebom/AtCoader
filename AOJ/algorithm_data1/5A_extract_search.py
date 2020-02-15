from typing import List
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = list(map(int, input().split()))

#bit演算子をやろうとしたやつ
# for n in range((1<<len(N))-1,-1,-1):
#     status=[(n>>i)&1 for i in range(N)]
#     Q[status]

def solve(i:int,m:int,A:List)->bool:
    '''i番目の要素だけで
    与えられた整数mが作れるかどうか'''
    n=len(A)
    #0...与えられた整数が作れた（m-要素の引き算=0)
    if m==0:
        return True
    #全部の要素について調べたけどダメだった。
    if i>=n:
        return False
    #選んだ場合、i+1の要素でm-A[i]ができれば良い
    res=solve(i+1,m,A) or solve(i+1,m-A[i],A)
    return res

def solve2(i:int,m:int)->bool:
    '''i番目の要素だけで
    与えられた整数mが作れるかどうか'''
    n=len(A)
    #0...与えられた整数が作れた（m-要素の引き算=0)
    if m==0:
        return True
    #全部の要素について調べたけどダメだった。
    if i>=n:
        return False
    #選んだ場合、i+1の要素でm-A[i]ができれば良い
    res=solve2(i+1,m) or solve2(i+1,m-A[i])
    return res

if __name__ == "__main__":
    for l in L:
        if solve2(0,l):
            print('yes')
        else:
            print('no')