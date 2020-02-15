class Card():
    def __init__(self,suit:str,value:int):
        self.suit=suit
        self.value=value
    
class QuickSort():
    def __init__(self,A):
        self.A=A

    def partition(self, p, r):
        x = self.A[r].value
        i = p - 1
        for j in range(p, r):
            # 小さい値があればそれより左に移動させる
            if self.A[j].value <= x:
                # 添字iも大きくする
                i += 1
                self.A[i], self.A[j] = self.A[j], self.A[i]
        self.A[i + 1], self.A[r] = self.A[r], self.A[i + 1]
        return  i + 1

    def sort(self,p,r):
        if q<r:
            q=self.partition(p,r)
            self.sort(p,q-1)
            self.sort(q+1,r)

            

