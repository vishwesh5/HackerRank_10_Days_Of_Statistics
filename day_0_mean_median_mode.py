n = int(input())
arr = list(map(int,input().strip().split(' ')))
# mean
mean = sum(arr)/float(n)
# median
arr_sorted=sorted(arr)
if n%2 == 0: # even
    median = (arr_sorted[n//2]+arr_sorted[n//2 - 1])/2.0
else: # odd
    median = arr_sorted[(n-1)/2]
# mode
def getmode(arr):
    most = max(list(map(arr.count,arr)))
    return sorted(list(set(filter(lambda x:arr.count(x)==most,arr))))[0]
mode = getmode(arr)
# print results
print("%.1f"%(mean))
print("%.1f"%(median))
print("%d"%(mode))
