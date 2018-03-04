prob_no_more_than_2=0
prob_at_least_2=0
prob_2=0
fact_10=0

def factorial(n):
    if n<= 1:
        return 1
    return n*factorial(n-1)

fact_10=factorial(10)

def nCr(r):
    return fact_10/(factorial(10-r)*factorial(r))

for i in range(0,3):
    tmp = nCr(i)*(0.12**i)*(1-0.12)**(10-i)
    if i==2:
        prob_2=tmp
    prob_no_more_than_2 = prob_no_more_than_2+tmp

prob_at_least_2 = 1 - prob_no_more_than_2 + prob_2

print("%.3f\n%.3f"%(prob_no_more_than_2,prob_at_least_2))
