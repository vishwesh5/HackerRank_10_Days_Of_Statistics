def prob_n(n):
    return (2./3)**(n-1)*(1./3)

prob=0
for i in range(1,6):
    prob=prob+prob_n(i)

print("%.3f"%(prob))
