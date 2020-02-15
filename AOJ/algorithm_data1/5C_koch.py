'''
コッホ曲線をかくプログラミング
'''
from typing import Tuple
from math import cos,sin,pi
def koch(d:int,p1:tuple,p2:Tuple)->float:
    '''
    p1...(x,y)
    s...三角形の一番xが若い頂点
    u...三角形の2番目にxが若い頂点
    t...三角形の3番目にxが若い頂点

    '''
    th=pi*60.0/180
    if d==0:
        return None
    s=((p2[0]*2+p1[0]*1)/3,(p2[1]*2+p1[1]*1)/3)
    t=((p2[0]*1+p1[0]*2)/3,(p2[1]*1+p1[1]*2)/3)
    u=(
        (t[0]-s[0])*cos(th)-(t[1]-s[1])*sin(th)+s[0],
        (t[0]-s[0])*sin(th)+(t[1]-s[1])*cos(th)+s[1]
        )

    koch(n-1,p1,s)
    print(s)
    koch(n-1,s,u)
    print(u)
    koch(n-1,u,t)
    print(t)
    koch(n-1,t,p2)

        


if __name__ == "__main__":
    n=int(input())
    p1=(0,0)
    p2=(100,0)
    print(p1)
    koch(n,p1,p2)
    print(p2)