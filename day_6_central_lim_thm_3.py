from math import sqrt
n=100
mu_pop=500
sigma_pop=80
mu_sample=mu_pop
sigma_sample=sigma_pop/sqrt(n)
z_score=1.96

upper_lim = mu_sample+z_score*sigma_sample
lower_lim = mu_sample-z_score*sigma_sample

print("%.2f\n%.2f"%(lower_lim,upper_lim))
