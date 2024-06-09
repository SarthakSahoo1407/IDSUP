import numpy as np
import matplotlib.pyplot as plt


mus = [0, 0, 0, -1] 
sigmas = [1, 2, 0.5, 1] 
line_styles = ['-', '--', '-.', ':']  


x = np.linspace(-5, 5, 1000)

for mu, sigma, linestyle in zip(mus, sigmas, line_styles):
    y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))
    plt.plot(x, y, linestyle, label=f'mu={mu}, sigma={sigma}')

plt.title('Normal Probability Density Functions')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()

plt.grid(True)
plt.show()
