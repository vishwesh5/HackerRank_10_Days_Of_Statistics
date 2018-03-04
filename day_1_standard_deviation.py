from math import sqrt
n = int(input().strip())
arr = list(map(int,input().strip().split(' ')))
mean = sum(arr)/n
stdDev = sqrt(sum([(arr[i]-mean)**2 for i in range(n)])/n)
print("%.1f"%(stdDev))
