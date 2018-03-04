def getMedian(arr):
    n = len(arr)
    if n%2==0:
        return (arr[n//2]+arr[n//2 - 1])/2.0
    else:
        return arr[(n-1)//2]

def getQ (arr):
    n = len(arr)
    if n%2==0:
        Q1 = getMedian(arr[:n//2])
        Q3 = getMedian(arr[n//2 : ])
    else:
        Q1 = getMedian(arr[:(n-1)//2])
        Q3 = getMedian(arr[(n+1)//2:])
    Q2 = getMedian(arr)
    return (Q1,Q2,Q3)

n = int(input())
arr = sorted(list(map(int,input().strip().split(' '))))
Q1,Q2,Q3 = getQ(arr)
print("%d\n%d\n%d"%(Q1,Q2,Q3))
