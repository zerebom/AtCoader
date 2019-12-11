#A - 深さ優先探索
# https://atcoder.jp/conte2sts/atc001/tasks/dfs_a
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


h, w = map(int, input().split())
# 入力の外側を囲う用に#をつけてて頭がいい
input_field = [["#"] * (w + 2)] + [list("#" + input() + "#") for _ in range(h)] + [["#"] * (w + 2)]


# xとy逆だった…
def iterative_dfs(field):
    sx, sy = 0, 0
    for i, row in enumerate(field):
        if "s" in row:
            sx, sy = i, row.index("s")
    # 進む方向
    drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 最初はスタートをスタックしておく
    stack = [(sx, sy)]

    while stack:
        cx, cy = stack.pop()
        for dx, dy in drc:
            nx, ny = cx + dx, cy + dy
            if field[nx][ny] == "#":
                continue
            if field[nx][ny] == "g":
                return "Yes"
            # 壁でもゴールでも無ければスタックに追加。
            stack.append((nx, ny))
            # 通ったところは壁にしてしまう。
            field[nx][ny] = "#"
    return "No"


print(iterative_dfs(input_field))
