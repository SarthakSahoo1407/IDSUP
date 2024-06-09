import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


mus = [0, 0, 0, -1] 
sigmas = [1, 2, 0.5, 1]  
line_styles = ['-', '--', '-.', ':']  

x = np.linspace(-5, 5, 1000)

for mu, sigma, linestyle in zip(mus, sigmas, line_styles):
    y = norm.cdf(x, loc=mu, scale=sigma)
    plt.plot(x, y, linestyle, label=f'mu={mu}, sigma={sigma}')

plt.title('Normal Cumulative Distribution Functions')
plt.xlabel('x')
plt.ylabel('Cumulative Probability')
plt.legend()

plt.grid(True)
plt.show()
