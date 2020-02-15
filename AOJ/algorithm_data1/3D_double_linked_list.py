class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinekdList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new = Cell(value)
        
        #番兵。ここを起点にデータが追加されていく
        tmp = self.head

        # Noneなら=初めてinsertが呼ばれたなら
        if not tmp:
            # 今のセルを連結する
            new.next = new
            new.prev = new
            self.head = new
            return None

        #tmp(None)がnewと一致するまで
        while not tmp == self.head:
            tmp = tmp.next
        
        #つながってたやつを切り離してnewを挿入する
        #一個前から見た、次が今になる
        tmp.prev.next = new
        #newの過去は、今の過去
        new.prev = tmp.prev
        new.next = tmp
        tmp.prev = new
    
    def delete(self,value):
        tmp=self.head
