import mymodule
print(mymodule.greeting("Rickard"))

from mymodule import person1 as pers
print(pers["age"])

import platform
print(dir(platform)) #list all methods i.e. python_build
print(platform.python_build())


import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))