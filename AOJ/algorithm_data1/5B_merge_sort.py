
class MergeSort():
    def __init__(self):
        self.count=0

    def merge(self,left,right,count=0):
        merged=[]
        lr,ll=0,0
        while lr<len(right) and ll <len(left):
            merged.append(min(left[ll],right[lr]))
            if left[ll]<right[lr]:
                ll+=1
            else:
                lr+=1
            self.count+=1
        
        if lr<len(right):
            merged.extend(right[lr:])
            self.count+=len(right)-lr

        elif ll<len(left):
            merged.extend(left[ll:])
            self.count+=len(left)-ll
        
        return merged

    def sort(self,arr):
        if len(arr)<=1:
            return arr
        
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        left=self.sort(left)
        right=self.sort(right)
        return self.merge(left,right)
    

if __name__ == "__main__":
    n=int(input())
    S=list(map(int,input().split()))
    count=0
    ms=MergeSort()
    S=ms.sort(S)
    count=ms.count

    print(' '.join(list(map(str, S)))) 
    print(count)