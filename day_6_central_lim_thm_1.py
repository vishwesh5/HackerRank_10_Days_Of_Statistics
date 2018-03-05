from math import exp,erf,sqrt,pi
mu=205
sigma=15
n=49
mu_N=n*mu
sigma_N=sqrt(n)*sigma


def cummulativeNorm(x,mu,sigma):
    return 0.50*(1+erf((x-mu)/(sigma*sqrt(2))))

# less than 9800 pounds
print("%.4f"%(cummulativeNorm(9800,mu_N,sigma_N)))
