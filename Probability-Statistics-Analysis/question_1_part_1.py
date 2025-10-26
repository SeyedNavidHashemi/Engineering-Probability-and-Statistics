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

m = int(input())
n = int(input())
p = float(input())
prac_exp, prac_var= create_some_binomial_distribution_samples(m, n, p)
theo_exp = n * p
theo_var = n * p * (1 - p)

print("Practical Expectation = ", prac_exp)
print("Practical Variance = ", prac_var)
print("Theory Expectation = ", theo_exp)
print("Theory Variance = ", theo_var)
