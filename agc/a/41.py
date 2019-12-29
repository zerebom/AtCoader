#https://linus-mk.hatenablog.com/entry/2019/05/26/234642
#pythonのfloat(double)は2^56->10^16乗程度しか精度が出ない。
#int(a/2)
N,A,B = list(map(int, input().split()))
diff = B-A

if diff %2 == 0:
    # print(int(diff/2))ではダメ
    print(diff//2)
else:
    edge=min(N-B,A-1)
    if diff==1:
        print(edge+1)
    else:
        after=(diff-1)//2
        print(edge+after+1)
