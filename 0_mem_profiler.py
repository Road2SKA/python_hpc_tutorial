from memory_profiler import profile
import numpy as np

# use del to free memory

@profile
def test():
    a = np.random.rand(1000,1000)
    x = a**2
    b = np.random.rand(1000,1000)
    c = a*b
    d = np.random.rand(1000,1000)
    return c*d

test()
