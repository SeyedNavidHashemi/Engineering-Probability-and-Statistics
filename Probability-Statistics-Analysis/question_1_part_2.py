import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

def create_some_binomial_distribution_samples(m, n, p):

    array_of_wins = random.choice([0, 1], m * n, p=[1-p, p])
    matrix_of_array = np.mat(array_of_wins)
    matrix_of_array = matrix_of_array.reshape(m, n)
    # print(matrix_of_array)
    list_of_sum = np.sum(matrix_of_array, axis = 1)
    
    practical_exp = np.mean(list_of_sum) 
    practical_var = np.var(list_of_sum)

    return practical_exp, practical_var

m = 5000
n = 50

all_p_exp = list()
all_p_var = list()
all_t_exp = list()
all_t_var = list()

for p in np.arange(0, 1, 0.01):
    p_exp, p_var = create_some_binomial_distribution_samples(m, n, p)
    theo_exp = n * p
    theo_var = n * (p * (1-p))
    all_p_exp.append(p_exp)
    all_p_var.append(p_var)
    all_t_exp.append(theo_exp)
    all_t_var.append(theo_var)
x = np.arange(0, 1, 0.01)

plt.plot(x ,all_p_exp, color='y')
plt.plot(x ,all_p_var, color='r')
plt.plot(x ,all_t_exp, color='b')
plt.plot(x ,all_t_var, color='g')

plt.show()
