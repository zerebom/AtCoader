# 幅優先探索
# https://atcoder.jp/contests/atc002/tasks/abc007_3
import numpy as np
from collections import deque
import queue

H, W = map(int, input().split())
input_field = np.array([["#"] * (W + 2)] + [list("#" + input() + "#") for _ in range(H)] + [["#"] * (W + 2)])


# field = np.array([list(list(input())) for i in range(H)])
used = [[0] * (W+2) for i in range(H+2)]


def queue_bfs(H, W, sy, sx, field, used):
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
    max_wk=0
    while np.sum(np.array(used))!=((W+2)*(H+2)):
        print(np.sum(np.array(used)),(W*H))
        # 先頭から取り出す
        cy, cx, wk = q.get()
        
        if field[cy][cx] == '#' or used[cy][cx]:
            continue
        used[cy][cx] = 1

        for dx, dy in drc:
            nx, ny = cx + dx, cy + dy
            if field[ny][nx] == '.' and used[ny][nx] == 0:
                q.put((ny, nx, wk + 1))
        max_wk=max(max_wk,wk)
    return(max_wk)

for x in range(W+2):
    for y in range(H+2):
        if input_field[y,x]=='.':
            print(queue_bfs(H, W, y, x,input_field, used))


