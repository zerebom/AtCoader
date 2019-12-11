#bit全探索の問題

# def answer():
#     N = int(input())

#     E = []
#     for n in range(N):
#         A = int(input())
#         for _ in range(A):
#             x, y = list(map(int, input().split()))
#             E.append((n, x - 1, y))

#     ans = 0
#     # すべての証言のパターンについて矛盾がないか考える。矛盾がなければ、人数を数える。
#     # 2**n~-1まで−１ずつ減らしてカウント
#     for k in range((1 << N) - 1, -1, -1):
#         # kの値を２進数に変換し、リストに格納している
#         l = [(k >> i) & 1 for i in range(N)]
#         OK = True
#         # e0...証言者,e1...証言先,e2...証言先の状態。
#         for e0, e1, e2 in E:
#             if (l[e0] == 1 and l[e1] != e2):
#                 OK = False
#                 break
#         if OK:
#             # 矛盾がなければ、現在までのans=max(今までの最大人数,このパターンの正直者数)
#             ans = max(ans, sum(l))

#     return(print("ans:", ans))


# def myanswer():
#     N = int(input())

#     E = []
#     for n in range(N):
#         A = int(input())
#         for _ in range(A):
#             x, y = list(map(int, input().split()))
#             E.append((n, x - 1, y))
#     ans = 0
#     for k in range((1 << N)):
#         status = [(k >> i) & 1 for i in range(N)]
#         no_paradox = True
#         for Xa, Xb, yb in E:
#             if (status[Xa] == 1 and status[Xb] == yb):
#                 no_paradox = False
#                 break
#         if no_paradox:
#             ans = max(ans, sum(l))


# answer()

N = int(input())
E = []
for n in range(N):
    A = int(input())
    for _ in range(A):
        x, y = list(map(int, input().split()))
        E.append((n, x - 1, y))
ans = 0
for k in range((1 << N) - 1, -1, -1):
    status = [(k >> i) & 1 for i in range(N)]
    no_paradox = True
    for Xa, Xb, yb in E:
        if (status[Xa] == 1 and status[Xb] != yb):
            no_paradox = False
            break
    if no_paradox:
        ans = max(ans, sum(status))
print(ans)
