import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, binom, poisson


#binomail_distribution
binomail_n = 7072
binomial_p = 0.45
x_binomial = np.arange(3000, 3400, 1)
y_binomial = [binom.pmf(temp_x, binomail_n, binomial_p) for temp_x in x_binomial]
plt.bar(x_binomial, y_binomial, color='r')

#normal_distribution
normal_mean = 3182.59
normal_var = 41.84
x_normal = np.arange(3000, 3400, 0.01)
y_normal = norm.pdf(x_normal, normal_mean, normal_var)
plt.plot(x_normal, y_normal, color = 'g')

#poison_distribution
lambda_poisson = (7072 * 0.45)
x_poisson = np.arange(3000, 3400, 1)
y_poisson = [poisson.pmf(temp_x, lambda_poisson) for temp_x in x_poisson]
plt.plot(x_poisson, y_poisson, color='b')





plt.show() 