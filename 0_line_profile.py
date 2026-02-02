import math
def is_prime(n):
    if n <= 1:
        return False
    n_sqrt = math.floor(math.sqrt(n)) + 1
    for i in range(2, n_sqrt):
        if n % i == 0:
            return False
    return True

n = 6783858998837822

from line_profiler import LineProfiler
lp = LineProfiler()
lp(is_prime)(n)
lp.print_stats()