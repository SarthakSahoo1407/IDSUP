import math
import random
import matplotlib.pyplot as plt
n = 100
p = 0.75
num_points = 100
def generate_binomial_samples(n, p, num_points):
    samples = []
    for _ in range(num_points):
        sample = sum(1 for _ in range(n) if random.random() < p)
        samples.append(sample)
    return samples
binomial_samples = generate_binomial_samples(n, p, num_points)
mean = n * p
std_dev = math.sqrt(n * p * (1 - p))

# Generate x values for the normal approximation
x = [i for i in range(n + 1)]
def normal_approximation(x, mean, std_dev):
    return [1 / (std_dev * math.sqrt(2 * math.pi)) * math.exp(-(i - mean)**2 / (2 * std_dev**2)) for i in x]
normal_approximation_values = normal_approximation(x, mean, std_dev)
plt.hist(binomial_samples, bins=20, density=True, alpha=0.5, color='blue', label='Binomial Samples')
plt.plot(x, normal_approximation_values, color='red', label='Normal Approximation')

plt.title('Binomial Distribution vs Normal Approximation')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend()
plt.show()
