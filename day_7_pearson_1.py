from math import sqrt

# Read inputs
n = int(input())
X = list(map(float,input().strip().split(' ')))
Y = list(map(float,input().strip().split(' ')))

# Calculate mean
mean_X = sum(X)/n
mean_Y = sum(Y)/n

# Calculate standard deviation
stdDev_X = sqrt(sum([(X[i]-mean_X)**2 for i in range(n)])/n)
stdDev_Y = sqrt(sum([(Y[i]-mean_Y)**2 for i in range(n)])/n)

# Calculate Pearson correlation coefficient
r_xy = sum([(X[i]-mean_X)*(Y[i]-mean_Y) for i in range(n)])/(n*stdDev_X*stdDev_Y)

# Print output
print("%.3f"%(r_xy))
