n = int(input()) # read input
arr = list(map(int,input().strip().split(' '))) # read array
w = list(map(int,input().strip().split(' '))) # read weights
mean_w = sum([w[i]*arr[i] for i in range(n)])/sum(w) # calculated weighted mean
print("%.1f"%(mean_w)) # print result
