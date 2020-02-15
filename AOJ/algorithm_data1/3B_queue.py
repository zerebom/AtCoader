from queue import Queue
# from queue import LifoQueue as Stack


N,q = list(map(int,input().split()))

Q=Queue()
for i in range(N):
    Q.put(list(map(str,input().split())))


ans=[]

time=0
while len(ans)!=N:
    p,t=Q.get()
    t=int(t)
    if t-q>0:
        Q.put([p,str(t-q)])
        time+=q
    else:
        time+=t
        ans.append((p,time))

for p,t in ans:
    print(p,t)

    



