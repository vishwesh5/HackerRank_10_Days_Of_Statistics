from math import exp,erf,sqrt,pi
mu=20
sigma=2

def stdNormalDist(x):
    return exp(-x**2 / 2.0)/sqrt(2*pi)

def cummulativeNorm(x,mu,sigma):
    return 0.50*(1+erf((x-mu)/(sigma*sqrt(2))))

# less than 19.5 hr
print("%.3f"%(cummulativeNorm(19.5,mu,sigma)))

# between 20 to 22 hr
print("%.3f"%(cummulativeNorm(22,mu,sigma)-cummulativeNorm(20,mu,sigma)))
