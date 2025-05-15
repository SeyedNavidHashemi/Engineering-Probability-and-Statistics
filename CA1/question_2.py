import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, binom, poisson


#binomail_distribution
binomail_n = 250
binomial_p = 0.008
x_binomial = np.arange(-2, 6, 1)
y_binomial = [binom.pmf(temp_x, binomail_n, binomial_p) for temp_x in x_binomial]
plt.bar(x_binomial, y_binomial, color='b')

#normal_distribution
normal_mean = 2
normal_var = 1.4
x_normal = np.arange(-2, 6, 0.01)
y_normal = norm.pdf(x_normal, normal_mean, normal_var)
plt.plot(x_normal, y_normal, color = 'r')

#poison_distribution
lambda_poisson = (250 * 0.008)
x_poisson = np.arange(-2, 6, 1)
y_poisson = [poisson.pmf(temp_x, lambda_poisson) for temp_x in x_poisson]
plt.plot(x_poisson, y_poisson, color='black')



#show their graphs
plt.show() 