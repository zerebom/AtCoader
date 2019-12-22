# TLE(lr&ACsが重そう)



def ans():
    '''
    文字列のある時点でACが何回出たかをメモする。
    そしてr-lとして答えを出す。
    こうするとsumとかしないので早い
    sumはO(N)なので注意
    '''
    N, Q = list(map(int, input().split()))
    S = list(str(input()))
    questions = [tuple(map(int, input().split())) for _ in range(Q)]
    ACs = [0] * N

    for i in range(len(S)-1):
        if S[i] == 'A' and S[i + 1] == 'C':
            ACs[i + 1] = ACs[i] + 1
        else:
            ACs[i + 1] = ACs[i]

    for q in questions:
        print(ACs[q[1]-1] - ACs[q[0]-1])


def myans():
    '''
    ACが出現する場所を抑えておいて、
    range内に何回出てくるか探索
    '''
    N, Q = list(map(int, input().split()))
    S = list(str(input()))
    questions = [tuple(map(int, input().split())) for _ in range(Q)]
    ACs = [0] * N
    for i in range(len(S) - 1):
        if S[i] == 'A' and S[i + 1] == 'C':
            ACs[i] = 1

    for q in questions:
        print(ACs[q[0] - 1:q[1] - 1])

ans()
