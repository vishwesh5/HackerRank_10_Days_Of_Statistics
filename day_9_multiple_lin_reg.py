import numpy as np
m,n = list(map(int,input().strip().split()))
X=[]
Y=[]
for _ in range(n):
    tmp = list(map(float,input().strip().split()))
    tmp.insert(0,1)
    X.append(tmp[:m+1])
    Y.append([tmp[m+1]])
Y=np.array(Y)
X=np.array(X)
X_T = np.transpose(X)
B = np.dot(np.dot(np.linalg.inv(np.dot(X_T,X)),X_T),Y)
for _ in range(int(input())):
    X_test=[]
    tmp = list(map(float,input().strip().split()))
    tmp.insert(0,1)
    X_test.append(tmp[:m+1])
    Y_test=np.dot(X_test,B)
    print(Y_test[0,0])
