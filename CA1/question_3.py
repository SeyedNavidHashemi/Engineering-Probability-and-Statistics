import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

#normal_distribution
normal_mean = 80
normal_std = 12
x_normal = np.arange(44, 116, 0.01)
y_normal_pdf = norm.pdf(x_normal, normal_mean, normal_std)
y_normal_cdf = norm.cdf(x_normal, normal_mean, normal_std)
# plt.plot(x_normal, y_normal_pdf, color = 'g')
plt.plot(x_normal, y_normal_cdf, color = 'b')

#first_part
print("first question:")
for x in np.arange(44, 116, 0.01):
    if norm.cdf(x, normal_mean, normal_std) >= 0.9:
        print("x = ", x)
        break
#second_part
print("second question:")
for x in np.arange(44, 116, 0.01):
    if norm.cdf(x, normal_mean, normal_std) >= 0.75:
        print("x is in range(80, ", x, ")")
        break
#third_part 
print("third question:")
result = norm.cdf(90, normal_mean, normal_std) - norm.cdf(80, normal_mean, normal_std)
print("answer = Fx(90) - Fx(80) = ", result)
# plt.show()