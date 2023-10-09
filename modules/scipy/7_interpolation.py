"""
Interpolation used to add points in data. 
i.e. missing data in datasets

"""

from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1
interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)