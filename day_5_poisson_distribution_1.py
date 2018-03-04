e = 2.718
def factorial (n):
    if n<=1:
        return 1
    return n*factorial(n-1)
k = 5
fact_k = factorial(k)
l = 2.5
prob = (e**(-1*l))*(l**k)/fact_k
print("%.3f"%(prob))
