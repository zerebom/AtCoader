N = int(input())


class Hash():
    '''
    簡単な辞書をリストで実装
    '''

    def __init__(self, M=10000000):
        self.M = M
        self.hash = [None] * M

    def h1(self, key:int) -> int:
        return key % self.M

    def h2(self, key:int) -> int:
        # 衝突が起きたときに、別の要素に飛ぶための関数
        return 1 + (key % (self.M - 1))

    def h(self, key:int, i)->int:
        return (self.h1(key) + i * self.h2(key)) % self.M

    def add(self, key:int) -> None:
        i = 0
        while True:
            j = self.h(key, i)
            # 値が入ってないところを見つければOK
            if self.hash[j] == None:
                self.hash[j] = key
                return j
            else:
                i += 1

    def find(self, key:int) -> bool:
        i = 0
        while True:
            j = self.h(key, i)
            # 値が入ってないところを見つければOK
            if self.hash[j] == key:
                return j
            elif self.hash[j] == None or i >= self.M:
                return None
            # 別の値が違ったらハッシュ値を変えてリスタート
            else:
                i += 1


def getChar(ch:str)->int:
    if ch == 'A':
        return 1
    elif ch == 'C':
        return 2
    elif ch == 'G':
        return 3
    elif ch == 'T':
        return 4
    else:
        return 0


def str2key(key:str)->int:
    # ハッシュキーを手に入れる
    sum = 0
    for k in key:
        sum += getChar(k)
        # *5すれば、４進法で桁が上がるから
        sum *= 5
    return sum


h = Hash()
for i in range(N):
    f, key = list(map(str, input().split()))
    key = str2key(key)
    if f == 'insert':
        h.add(key)
    elif f == 'find':
        if h.find(key)==None:
            print('no')
        else:
            print('yes')
        # print(h.find(key))
        # print(type(h.find(key)) == str)
