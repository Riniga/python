"""
Export to pMatlab
"""

from scipy import io
import numpy as np

arr = np.arange(10)
print(arr)

io.savemat('modules\\scipy\\arr.mat', {"vec": arr})
mydata = io.loadmat('modules\\scipy\\arr.mat',squeeze_me=True)

print(mydata)
print(mydata["vec"])
