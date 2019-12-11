# 幅優先探索
# https://atcoder.jp/contests/atc002/tasks/abc007_3
import numpy as np
from collections import deque
import queue

R, C = map(int, input().split())
sy, sx = map(lambda x: int(x)-1, input().split())
gy, gx = map(lambda x: int(x)-1, input().split())

field = np.array([list(list(input())) for i in range(R)])
used = [[0] * C for i in range(R)]


def queue_bfs(R, C, sy, sx, gy, gx, field, used):
    '''迷路で使用するbfs,
    キューを使うことで、最もスタートに近い点(=歩数が少なく到達できる点)から探しにいける。
    cy,cx...現在の位置
    dy,dx...4方向のうちのどれか
    nx,ny...cx,cyから歩を進めたもの。
    wk...歩いた距離。

    '''
    drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    wk = 0
    q = queue.Queue()
    # 後ろに追加
    q.put((sy, sx, wk))
    cy, cx = sy, sx
    while cy != gy or cx != gx:
        # 先頭から取り出す
        cy, cx, wk = q.get()
        if field[cy][cx] == '#' or used[cy][cx]:
            continue
        used[cy][cx] = 1

        for dx, dy in drc:
            nx, ny = cx + dx, cy + dy
            if field[ny][nx] == '.' and used[ny][nx] == 0:
                q.put((ny, nx, wk + 1))
    return(wk)


print(queue_bfs(R, C, sy, sx, gy, gx, field, used))
