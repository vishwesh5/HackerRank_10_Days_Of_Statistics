from math import sqrt
# Read inputs
n = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

# Get rank array
def getRank(arr):
    arr_str = '  '.join(list(map(str,arr)))
    arr_str = '  '+arr_str+'  '
    sorted_arr = sorted(list(set(arr)))
    for i in range(len(sorted_arr)):
        arr_str = arr_str.replace(' '+str(sorted_arr[i])+' ',' '+str(i+1)+' ')
    arr_str = list(map(int,arr_str.strip().split()))
    return arr_str

# Get mean
def getMean(X):
    n = len(X)
    return sum(X)/n

# Get standard deviation
def getStdDev(X):
    n = len(X)
    mean_X = getMean(X)
    return sqrt(sum([(X[i]-mean_X)**2 for i in range(n)])/n)

# If unique elements
def rxy(X,Y):
    n = len(X)
    return 1 - 6*sum([(X[i]-Y[i])**2 for i in range(len(X))])/(n*(n**2 - 1))

# If not unique elements
def rxyNotUnique(X,Y):
    n = len(X)
    mean_X = getMean(X)
    mean_Y = getMean(Y)
    stdDev_X = getStdDev(X)
    stdDev_Y = getStdDev(Y)
    return sum([(X[i]-mean_X)*(Y[i]-mean_Y) for i in range(n)])/(n*stdDev_X*stdDev_Y)

X_rank = getRank(X)
Y_rank = getRank(Y)
print("%.3f"%(rxy(X_rank,Y_rank)))
# print("%.3f"%(rxyNotUnique(X_rank,Y_rank)))
