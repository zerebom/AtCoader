# UnionFind
# 状態を持つなら、クラスで書いたほうが良い
# https://atcoder.jp/contests/atc001/tasks/dfs_a
# https://atcoder.jp/contests/atc001/submissions/8651660


class UnionFind:
    def __init__(self, N: int):
        self.root = list(range(N + 1))
        self.size = [1] * (N + 1)

    def find_root(self, x: int):
        """根を探す"""
        root = self.root
        while root[x] != x:
            # 自分の親ノードの親はどこか再起で探しに行く->経路圧縮
            root[x] = root[root[x]]
            x = root[x]
        return x

    def unite(self, x: int, y: int):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return

        # ランクを気にして結合する
        sx, sy = self.size[x], self.size[y]
        if sx < sy:
            self.root[x] = y
            self.size[y] += sx
        else:
            self.root[y] = x
            self.size[x] += sy


if __name__ == "__main__":
    N, Q = map(int, input().split())
    uf = UnionFind(N)
    answer = []

    for i in range(Q):
        p, x, y = map(int, input().split())
        if p == 0:
            uf.unite(x, y)
        else:
            answer.append('Yes' if uf.find_root(x) == uf.find_root(y) else 'No')

    print('\n'.join(answer))

# if __name__ == "__main__":
#     N, Q = map(int, input().split())
#     global par
#     # 親ノード。par[i]=iで自身の値を持っているつまり根)
#     par = list(range(N))

#     for i in range(Q):
#         p, x, y = map(int, input().split())
#         if p == 0:
#             unite(x, y)
#         else:
#             print('x,y:', par[x], par[y])
#             if same(x, y):
#                 print('Yes')
#             else:
#                 print('No')
