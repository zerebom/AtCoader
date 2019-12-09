#A - 深さ優先探索
# https://atcoder.jp/contests/atc001/tasks/dfs_a
import numpy as np
H, W = map(int, input().split())

s = np.array([list(map(str, list(input()))) for i in range(H)])
print(s.shape)

reached = np.zeros((H, W))


def recursive_dfs():
    """
    迷路を探索するdfs.
    すべての位置で４方向探索するので全部見れる。returnしても戻ってこれる"""
    def search(x, y):
        # print(x, y)
        if(x < 0 or x >= W or y < 0 or y >= W or s[x, y] == '#'):
            return
        if(reached[x, y]):
            return

        reached[x, y] = True
        search(x + 1, y)
        search(x - 1, y)
        search(x, y - 1)
        search(x, y + 1)

    # 初期位置の取得
    st = np.argwhere(s == 's')
    sx, sy = st[0, 0], st[0, 1]

    search(sx, sy)

    # ゴール位置の取得
    g = np.argwhere(s == 'g')
    gx, gy = g[0, 0], g[0, 1]

    # print(reached)
    if reached[gx, gy]:
        print('Yes')
    else:
        print('No')


def stack_dfs():
    stack = []
    while stack:
        x, y = stack[-1, 0], stack[-1, 1]
        if not reached[x, y]:
            reached[x, y] = True
            remove_stack = True

# https://atcoder.jp/contests/atc001/submissions/8788066
def iterative_dfs(field):
    sr, sc = 0, 0
    for i, row in enumerate(field):
        if "s" in row:
            sr, sc = i, row.index("s")

    drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [(sr, sc)]

    while stack:
        cr, cc = stack.pop()
        for dr, dc in drc:
            nr, nc = cr + dr, cc + dc
            if field[nr][nc] == "#":
                continue
            if field[nr][nc] == "g":
                return "Yes"
            stack.append((nr, nc))
            field[nr][nc] = "#"
    return "No"


print(iterative_dfs(input_field))
