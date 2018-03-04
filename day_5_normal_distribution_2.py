from math import exp,erf,sqrt,pi
mu=70
sigma=10

def stdNormalDist(x):
    return exp(-x**2 / 2.0)/sqrt(2*pi)

def cummulativeNorm(x,mu,sigma):
    return 0.50*(1+erf((x-mu)/(sigma*sqrt(2))))

# more than 80
print("%.2f"%((1-cummulativeNorm(80,mu,sigma))*100))

# more than 60
print("%.2f"%((1-cummulativeNorm(60,mu,sigma))*100))

# less than 60
print("%.2f"%((cummulativeNorm(60,mu,sigma))*100))
