from math import exp,erf,sqrt,pi
mu=2.4
sigma=2.0
n=100
mu_N=n*mu
sigma_N=sqrt(n)*sigma


def cummulativeNorm(x,mu,sigma):
    return 0.50*(1+erf((x-mu)/(sigma*sqrt(2))))

# less than 250 tickets
print("%.4f"%(cummulativeNorm(250,mu_N,sigma_N)))
