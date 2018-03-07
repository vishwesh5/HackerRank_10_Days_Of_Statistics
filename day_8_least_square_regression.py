X=[95,85,80,70,60]
Y=[85,95,70,65,70]
x=80
n=5

sum_X=sum(X)
sum_Y=sum(Y)
sum_XY=sum([X[i]*Y[i] for i in range(n)])
sum_Xsq=sum([i**2 for i in X])
mean_X=sum_X/n
mean_Y=sum_Y/n

b=(n*sum_XY-sum_X*sum_Y)/(n*sum_Xsq-sum_X**2)
a=mean_Y-b*mean_X

y=a+b*x

print("%.3f"%(y))
