from scipy.optimize import root
from scipy.optimize import minimize
from math import cos

f1 = lambda x : x + cos(x)
f2 = lambda x : x**2 + x + 2
f3 = lambda x : 2*x - 3

the_root = root(f2, 0)
x = the_root.x
print(x)
print(f2(x))

mymin = minimize(f2, 0, method='BFGS')
print(mymin)