"""
Statistical Significance, 
check if data is has a reason and not randomly or by chance

- Hypothesis is an assumption about a parameter in population.
- Null Hypothesis - assumes that the observation is not statistically significant.

alpha-value: Level of significance
p-value:     How close to extreme data is
If p value <= alpha we reject the null hypothesis and say that the data is statistically significant
"""

import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import describe

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

# Two tailed test
res = ttest_ind(v1, v2)
print(res)

res = describe(v1)
print(res)

