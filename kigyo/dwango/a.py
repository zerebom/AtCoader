N = int(input())
musics,minutes=[],[]

for i in range(N):
    music,minute = list(map(str, input().split()))
    musics.append(music)
    minutes.append(int(minute))

X = str(input())

Xidx=musics.index(X)
print(sum(minutes[Xidx+1:]))
