#  Define p-value and write a python program to find the two-sided p-value with and without continuity correction when the values of x(observed no. of heads), mean and standard deviation are 110, 100, 5  respectively.

# The p-value is a measure used in hypothesis testing to determine the statistical significance of observed data. It represents the probability of obtaining test results at least as extreme as the observed results, under the assumption that the null hypothesis is true. In other words, it indicates how likely it is to observe the given data if the null hypothesis is correct.

import scipy.stats as stats

def two_sided_p_value(x, mean, std_dev, use_continuity_correction=True):
    z_score = (x - mean) / std_dev
    if use_continuity_correction:
        return 2 * stats.norm.cdf(-abs(z_score))  
    else:
        return 2 * stats.norm.cdf(-abs(z_score))


x = 110
mean = 100
std_dev = 5
p_value_with_correction = two_sided_p_value(x, mean, std_dev, use_continuity_correction=True)
print("Two-sided p-value with continuity correction:", p_value_with_correction)
p_value_without_correction = two_sided_p_value(x, mean, std_dev, use_continuity_correction=False)
print("Two-sided p-value without continuity correction:", p_value_without_correction)
