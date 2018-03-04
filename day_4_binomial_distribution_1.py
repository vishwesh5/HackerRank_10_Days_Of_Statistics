p_boy = 1.09/(1.09+1)
p_girl = 1./(1.09+1)

def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

def nCr(n,r):
    ans= factorial(n)/(factorial(r)*factorial(n-r))
    return ans

prob=0
for i in range(3,7):
    prob = prob+nCr(6,i)*(p_boy**i)*(p_girl**(6-i))

print("%.3f"%(prob))
